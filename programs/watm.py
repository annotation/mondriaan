import json
from textwrap import dedent

from tf.core.files import initTree, unexpanduser as ux
from tf.parameters import OTYPE, OSLOTS


TT_NAME = "watm"
RKD_URL_BASE = "https://rkd.nl/explore/images/"

NS_TF = "tf"
NS_TEI = "tei"
NS_NLP = "nlp"
NS_TT = "tt"

NS_FROM_OTYPE = dict(
    page=NS_TF,
    file=NS_TF,
    folder=NS_TF,
    letter=NS_TF,
    chapter=NS_TF,
    chunk=NS_TF,
    word=NS_TF,
    char=NS_TF,
    token=NS_NLP,
    sentence=NS_NLP,
)

KIND_NODE = "node"
KIND_EDGE = "edge"
KIND_ELEM = "element"
KIND_PI = "pi"
KIND_ATTR = "attribute"
KIND_FMT = "format"
KIND_ANNO = "anno"


class WATM:
    def __init__(self, app, skipMeta=False):
        self.app = app
        self.skipMeta = skipMeta
        api = app.api
        self.L = api.L
        self.E = api.E
        self.Es = api.Es
        self.F = api.F
        self.Fs = api.Fs
        self.slotType = self.F.otype.slotType
        self.otypes = self.F.otype.all
        self.info = app.info
        self.repoLocation = app.repoLocation

        Fall = api.Fall
        Eall = api.Eall
        excludedFeatures = {OTYPE, OSLOTS, "after", "str"}
        self.nodeFeatures = [f for f in Fall() if f not in excludedFeatures]
        self.edgeFeatures = [f for f in Eall() if f not in excludedFeatures]

    def makeText(self):
        F = self.F
        slotType = self.slotType
        skipMeta = self.skipMeta

        text = []
        tlFromTf = {}

        self.text = text
        self.tlFromTf = tlFromTf

        for s in F.otype.s(slotType):
            if skipMeta and F.is_meta.v(s):
                continue

            after = F.after.v(s) or ""

            if F.empty.v(s):
                value = after
            else:
                value = f"{F.str.v(s)}{after}"

            text.append(value)
            t = len(text) - 1
            tlFromTf[s] = t

    def mkAnno(self, kind, ns, body, target):
        """Make an annotation and return its id.

        Parameters
        ----------
        kind: string
            The kind of annotation.
        ns: string
            The namespace of the annotation.
        body: string
            The body of the annotation.
        target: string  or tuple of strings
            The target of the annotation.
        """
        annos = self.annos
        aId = f"a{len(annos):>06}"
        annos.append((kind, aId, ns, body, target))
        return aId

    def makeAnno(self):
        E = self.E
        Es = self.Es
        F = self.F
        Fs = self.Fs
        nodeFeatures = self.nodeFeatures
        edgeFeatures = self.edgeFeatures
        slotType = self.slotType
        otypes = self.otypes
        skipMeta = self.skipMeta

        tlFromTf = self.tlFromTf

        annos = []
        text = self.text
        self.annos = annos

        wrongTargets = []

        for otype in otypes:
            isSlot = otype == slotType

            for n in F.otype.s(otype):
                if isSlot:
                    if skipMeta and F.is_meta.v(n):
                        continue
                    t = tlFromTf[n]
                    target = f"{t}-{t + 1}"
                    self.mkAnno(KIND_NODE, NS_TF, n, target)
                else:
                    ws = E.oslots.s(n)
                    if skipMeta and (F.is_meta.v(ws[0]) or F.is_meta.v(ws[-1])):
                        continue
                    start = tlFromTf[ws[0]]
                    end = tlFromTf[ws[-1]]
                    if end < start:
                        wrongTargets.append((otype, start, end))

                    target = f"{start}-{end + 1}"
                    aId = self.mkAnno(
                        KIND_PI, NS_TEI, otype[1:], target
                    ) if otype.startswith("?") else self.mkAnno(
                        KIND_ELEM, NS_FROM_OTYPE.get(otype, NS_TEI), otype, target
                    )
                    tlFromTf[n] = aId
                    self.mkAnno(KIND_NODE, NS_TF, n, aId)

        for feat in nodeFeatures:
            ns = Fs(feat).meta["conversionCode"]
            parts = feat.split("_", 2)

            if len(parts) >= 2 and parts[0] == "rend":
                for (n, val) in Fs(feat).items():
                    if not val or (skipMeta and F.is_meta.v(n)):
                        continue
                    prop = parts[1]
                    t = tlFromTf[n]
                    target = f"{t}-{t + 1}" if F.otype.v(n) == slotType else t
                    self.mkAnno(KIND_FMT, ns, prop, target)
            elif len(parts) == 2 and parts[0] == "is" and parts[1] == "note":
                for (n, val) in Fs(feat).items():
                    if not val or (skipMeta and F.is_meta.v(n)):
                        continue
                    t = tlFromTf[n]
                    target = f"{t}-{t + 1}" if F.otype.v(n) == slotType else t
                    self.mkAnno(KIND_FMT, ns, "note", target)
            else:
                for (n, val) in Fs(feat).items():
                    if skipMeta and F.is_meta.v(n):
                        continue
                    t = tlFromTf.get(n, None)
                    if t is None:
                        continue
                    target = f"{t}-{t + 1}" if F.otype.v(n) == slotType else t
                    aId = self.mkAnno(KIND_ATTR, ns, f"{feat}={val}", target)

        for feat in edgeFeatures:
            ns = Es(feat).meta["conversionCode"]

            for (fromNode, toNodes) in Es(feat).items():
                if skipMeta and F.is_meta.v(fromNode):
                    continue
                fromT = tlFromTf.get(fromNode, None)
                if fromT is None:
                    continue
                targetFrom = (
                    f"{fromT}-{fromT + 1}" if F.otype.v(fromNode) == slotType else fromT
                )

                if type(toNodes) is dict:
                    for (toNode, val) in toNodes.items():
                        if skipMeta and F.is_meta.v(toNode):
                            continue
                        toT = tlFromTf.get(toNode, None)
                        if toT is None:
                            continue

                        targetTo = (
                            f"{toT}-{toT + 1}" if F.otype.v(toNode) == slotType else toT
                        )
                        target = f"{targetFrom}->{targetTo}"
                        aId = self.mkAnno(KIND_EDGE, ns, f"{feat}={val}", target)
                else:
                    for toNode in toNodes:
                        if skipMeta and F.is_meta.v(toNode):
                            continue
                        toT = tlFromTf.get(toNode, None)
                        if toT is None:
                            continue
                        target = f"{fromT}->{toT}"
                        aId = self.mkAnno(KIND_EDGE, ns, feat, target)

        extra = {}
        extra.update(self.getArtWorksUrl())

        for (n, value) in extra.items():
            t = tlFromTf[n]
            target = f"{t}-{t + 1}" if F.otype.v(n) == slotType else t
            aId = self.mkAnno(KIND_ANNO, NS_TT, str(value), target)

        if len(wrongTargets):
            print(f"WARNING: wrong targets, {len(wrongTargets)}x")
            for (otype, start, end) in wrongTargets:
                sega = text[start]
                segb = text[end - 1]
                print(f"{otype:>20} {start:>6} `{sega}` > {end - 1} `{segb}`")

    def getArtWorksUrl(self):
        A = self.app
        F = self.F
        query = dedent(
            """
            rs type=artwork-m key~[1-9]
            """
        )
        artworksWithRef = A.search(query)
        return {r[0]: f"{RKD_URL_BASE}{F.key.v(r[0])}" for r in artworksWithRef}

    def writeAll(self):
        app = self.app
        info = self.info
        text = self.text
        annos = self.annos

        baseDir = self.repoLocation
        version = app.version
        resultDir = f"{baseDir}/{TT_NAME}/{version}"
        textFile = f"{resultDir}/text.json"
        annoFile = f"{resultDir}/anno.json"

        self.textFile = textFile
        self.annoFile = annoFile

        initTree(resultDir, fresh=True)

        with open(textFile, "w") as fh:
            json.dump(dict(_ordered_segments=text), fh, ensure_ascii=False, indent=1)

        with open(annoFile, "w") as fh:
            annoStore = {}
            for (kind, aId, ns, body, target) in annos:
                annoStore[aId] = (kind, ns, body, target)
            json.dump(annoStore, fh, ensure_ascii=False, indent=1)

        info(f"Text file: {len(text):>7} segments to {ux(textFile)}", tm=False)
        info(f"Anno file: {len(annos):>7} annotations to {ux(annoFile)}", tm=False)
