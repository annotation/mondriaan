import types
from tf.advanced.app import App

# INSERT import

KNOWN_RENDS = {'italics', 'h1', 'spaced', 'sc', 'below', 'h2', 'h6', 'above', 'super', 'center', 'h4', 'smallcaps', 'ul', 'b', 'italic', 'small_caps', 'h5', 'sup', 'margin', 'h3', 'large', 'underline', 'bold', 'i', 'sub', 'spat'}


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

    # INSERT init

    def _wrapHtml(app, n):
        rendFeatures = app.rendFeatures
        isFeatures = app.isFeatures
        api = app.api
        F = api.F
        Fs = api.Fs
        material = F.ch.v(n) or ""
        rClses = " ".join(
            f"r_{r}" if r in KNOWN_RENDS else "r_"
            for (fr, r) in rendFeatures
            if Fs(fr).v(n)
        )
        iClses = " ".join(ic for ic in isFeatures if Fs(ic).v(n))
        if rClses or iClses:
            material = f'<span class="{rClses} {iClses}">{material}</span>'
        return material

    # INSERT extra

