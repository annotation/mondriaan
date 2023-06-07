import os
from glob import glob
from shutil import copyfile
import yaml

from tf.advanced.helpers import dh
from tf.advanced.repo import checkoutRepo
from tf.core.timestamp import AUTO, TERSE, VERBOSE

LOCAL_IMAGE_DIR = "illustrations"

ARTWORK_TO = "{}"
ARTWORK_EXT = "jpg"
ARTWORK_LABEL = "artwork-m"
ARTWORK_URL_BASE = "https://rkd.nl/explore/images"
ARTWORK_TITLE = "visit this artwork on the RKD site"
ARTWORK_META = "images.yaml"


def imageCls(app, n):
    api = app.api
    F = api.F
    nType = F.otype.v(n)
    ref = F.ref.v(n)
    typ = F.type.v(n)

    key = None

    if nType == "rs":
        ref = F.ref.v(n)
        if ref and typ == ARTWORK_LABEL:
            key = ref.split("#")[1]
    elif nType == "artwork":
        key = F.id.v(n)
        typ = ARTWORK_LABEL

    if key is None:
        return (nType, None, None, None)

    key = key.removeprefix("a")
    return (nType, typ, key, f"{key}.{ARTWORK_EXT}")


def getImages(
    app,
    ns,
    kind=None,
    warning=True,
    _asString=False,
):
    if type(ns) is int or type(ns) is str:
        ns = [ns]
    result = []
    for n in ns:
        (nType, kind, identifier, fileName) = imageCls(app, n)
        if kind:
            imagery = app._imagery.get(kind, {})
            image = imagery.get(fileName, None)
            if image is None:
                thisImage = (
                    (f"<span><b>no {kind}</b>" f" <code>{fileName}</code></span>")
                    if warning
                    else ""
                )
            else:
                theImage = _useImage(app, image, kind, n)
                thisImage = (
                    f'<img src="{theImage}" class="graphic_img" />'
                )

            meta = app._imageMeta.get(identifier, {})
            artist = ", ".join(meta.get("artist", []))
            desc = ", ".join(meta.get("description", []))
            medium = ", ".join(meta.get("artMedium", []))
            surface = ", ".join(meta.get("artworkSurface", []))

            if artist:
                sep = "," if desc else "."
                artist = f"{artist}{sep} "
            if desc:
                desc = f"<i>{desc}</i>. "
            if medium:
                sep = "" if surface else "."
                medium = f"{medium}{sep} "
            if surface:
                surface = f"on {surface}. "

            title = f'title="{ARTWORK_TITLE}"'
            url = f"{ARTWORK_URL_BASE}/{identifier}"
            target = 'target="_blank"'
            link = f"""<a {target} href="{url}" {title}>RKD {identifier}►</a>"""
            caption = (
                (
                    f"""<span class="graphic_caption">"""
                    f"""{artist}{desc}{medium}{surface}{link}</span>"""
                )
            )

            thisResult = (thisImage if thisImage else "") + caption
        else:
            thisResult = (
                f"<span><b>no image</b> for <code>{nType}</code>s</span>"
                if warning
                else ""
            )
        result.append(thisResult)
    if not warning:
        result = [image for image in result if image]
    if not result:
        return ""
    resultStr = '</div><div class="graphic_item">'.join(result)
    html = (
        '<div class="graphic_set">'
        f'<div class="graphic_item">'
        f"{resultStr}</div></div>"
    ).replace("\n", "")
    if _asString:
        return html
    dh(html)
    if not warning:
        return True


def _useImage(app, image, kind, node):
    _browse = app._browse
    aContext = app.context

    (imageDir, imageName) = os.path.split(image)
    (base, ext) = os.path.splitext(imageName)
    localBase = aContext.localDir if _browse else app.curDir
    localDir = f"{localBase}/{LOCAL_IMAGE_DIR}"

    if not os.path.exists(localDir):
        os.makedirs(localDir, exist_ok=True)

    localImageName = f"{kind}-{node}{ext}"
    localImagePath = f"{localDir}/{localImageName}"
    if not os.path.exists(localImagePath) or os.path.getmtime(image) > os.path.getmtime(
        localImagePath
    ):
        copyfile(image, localImagePath)
    base = "/local/" if _browse else ""
    return f"{base}{LOCAL_IMAGE_DIR}/{localImageName}"


def getImagery(app, silent, checkout=""):
    aContext = app.context
    org = aContext.org
    repo = aContext.repo
    graphicsRelative = aContext.graphicsRelative

    (imageRelease, imageCommit, imageLocal, imageBase, imageDir) = checkoutRepo(
        app.backend,
        app._browse,
        org=org,
        repo=repo,
        folder=graphicsRelative,
        version="",
        checkout=checkout,
        withPaths=True,
        keep=True,
        silent=silent,
    )
    if not imageBase:
        app.api = None
        return

    app.imageDir = f"{imageBase}/{org}/{repo}/{graphicsRelative}"

    with open(f"{app.imageDir}/{ARTWORK_META}") as fh:
        app._imageMeta = yaml.load(fh, Loader=yaml.FullLoader)

    app._imagery = {}
    for (dirFmt, ext, kind) in ((ARTWORK_TO, ARTWORK_EXT, ARTWORK_LABEL),):
        srcDir = dirFmt.format(app.imageDir)
        filePaths = glob(f"{srcDir}/*.{ext}")
        images = {}

        for filePath in filePaths:
            fileName = os.path.split(filePath)[1]
            images[fileName] = filePath

        app._imagery[kind] = images

        if silent in {VERBOSE, AUTO, TERSE}:
            dh(f"Found {len(images)} {kind}s<br>")
