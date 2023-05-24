import types
from tf.advanced.app import App

from tf.advanced.find import loadModule

KNOWN_RENDS = {'italic', 'super', 'small_caps', 'sup', 'center', 'bold', 'h6', 'below', 'h2', 'spat', 'h3', 'ul', 'h4', 'large', 'above', 'italics', 'underline', 'i', 'sc', 'spaced', 'smallcaps', 'h1', 'h5', 'b', 'sub', 'margin'}


def fmt_layout(app, n, **kwargs):
    return app._wrapHtml(n)


class TfApp(App):
    def __init__(app, *args, **kwargs):
        app.fmt_layout = types.MethodType(fmt_layout, app)
        super().__init__(*args, **kwargs)
        app.rendFeatures = tuple(
            (f, f[5:]) for f in app.api.Fall() if f.startswith("rend_")
        )
        app.isFeatures = tuple(f for f in app.api.Fall() if f.startswith("is_"))

        app.image = loadModule("image", *args)
        app.image.getImagery(app, app.silent, checkout=kwargs.get("checkout", ""))
        app.reinit()

    def _wrapHtml(app, n):
        rendFeatures = app.rendFeatures
        isFeatures = app.isFeatures
        api = app.api
        F = api.F
        Fs = api.Fs
        material = f'{F.str.v(n) or ""}{F.after.v(n) or ""}'
        rClses = " ".join(
            f"r_{r}" if r in KNOWN_RENDS else "r_"
            for (fr, r) in rendFeatures
            if Fs(fr).v(n)
        )
        iClses = " ".join(ic for ic in isFeatures if Fs(ic).v(n))
        if rClses or iClses:
            material = f'<span class="{rClses} {iClses}">{material}</span>'
        return material

    # GRAPHICS Support

    def getGraphics(app, isPretty, n, nType, outer):
        result = ""

        if True:
            theGraphics = app.image.getImages(
                app,
                n,
                kind=nType,
                _asString=True,
                warning=False,
            )
            if theGraphics:
                result = f"<div>{theGraphics}</div>" if isPretty else f" {theGraphics}"

        return result

    def imagery(app, objectType, kind):
        return set(app._imagery.get(objectType, {}).get(kind, {}))

