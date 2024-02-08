# DEF import
from tf.advanced.find import loadModule
# END DEF

# DEF init
        app.image = loadModule("image", *args)
        app.image.getImagery(app, app.silent, checkout=kwargs.get("checkout", ""))
        app.reinit()
# END DEF

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

# DEF extra
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
# END DEF
