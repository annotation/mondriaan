import json
from tf.core.files import initTree, unexpanduser as ux


TT_NAME = "watm"


class WATM:
    def __init__(self, app):
        self.app = app
        api = app.api
        self.L = api.L
        self.E = api.E
        self.F = api.F
        self.Fs = api.Fs
        self.slotType = self.F.otype.slotType
        self.otypes = self.F.otype.all
        self.info = app.info
        self.repoLocation = app.repoLocation

        Fall = api.Fall
        excludedFeatures = {"otype", "after", "str"}
        self.features = [f for f in Fall() if f not in excludedFeatures]

    def makeText(self):
        F = self.F
        slotType = self.slotType

        text = []
        tlFromTf = {}

        self.text = text
        self.tlFromTf = tlFromTf

        for s in F.otype.s(slotType):
            if F.is_meta.v(s):
                continue

            if F.empty.v(s):
                value = ""
            else:
                after = F.after.v(s) or ""
                value = f"{F.str.v(s)}{after}"

            text.append(value)
            t = len(text) - 1
            tlFromTf[s] = t

    def mkAnno(self, kind, body, target):
        annos = self.annos
        aId = f"a{len(annos):>06}"
        annos.append((kind, aId, body, target))
        return aId

    def makeAnno(self, extra):
        E = self.E
        F = self.F
        Fs = self.Fs
        features = self.features
        slotType = self.slotType
        otypes = self.otypes

        tlFromTf = self.tlFromTf

        annos = []
        text = self.text
        self.annos = annos

        wrongTargets = []

        kind1 = "node"
        kind2 = "element"
        kind3 = "attribute"
        kind4 = "format"
        kind5 = "anno"

        for otype in otypes:
            isSlot = otype == slotType

            for n in F.otype.s(otype):
                if isSlot:
                    if F.is_meta.v(n):
                        continue
                    t = tlFromTf[n]
                    target = f"{t}-{t + 1}"
                    self.mkAnno(kind1, n, target)
                else:
                    ws = E.oslots.s(n)
                    if F.is_meta.v(ws[0]) or F.is_meta.v(ws[-1]):
                        continue
                    start = tlFromTf[ws[0]]
                    end = tlFromTf[ws[-1]]
                    if end < start:
                        wrongTargets.append((otype, start, end))

                    target = f"{start}-{end + 1}"
                    aId = self.mkAnno(kind2, otype, target)
                    tlFromTf[n] = aId
                    self.mkAnno(kind1, n, aId)

        for feat in features:
            parts = feat.split("_", 2)
            if len(parts) >= 2 and parts[0] == "rend":
                for (n, val) in Fs(feat).items():
                    if not val or F.is_meta.v(n):
                        continue
                    prop = parts[1]
                    t = tlFromTf[n]
                    target = f"{t}-{t + 1}" if F.otype.v(n) == slotType else t
                    self.mkAnno(kind4, prop, target)
            elif len(parts) == 2 and parts[0] == "is" and parts[1] == "note":
                for (n, val) in Fs(feat).items():
                    if not val or F.is_meta.v(n):
                        continue
                    t = tlFromTf[n]
                    target = f"{t}-{t + 1}" if F.otype.v(n) == slotType else t
                    self.mkAnno(kind4, "note", target)
            else:
                for (n, val) in Fs(feat).items():
                    if F.is_meta.v(n):
                        continue
                    t = tlFromTf.get(n, None)
                    if t is None:
                        continue
                    target = f"{t}-{t + 1}" if F.otype.v(n) == slotType else t
                    aId = self.mkAnno(kind3, f"{feat}={val}", target)

        for (n, value) in extra.items():
            t = tlFromTf[n]
            target = f"{t}-{t + 1}" if F.otype.v(n) == slotType else t
            aId = self.mkAnno(kind5, str(value), target)

        if len(wrongTargets):
            print(f"WARNING: wrong targets, {len(wrongTargets)}x")
            for (otype, start, end) in wrongTargets:
                sega = text[start]
                segb = text[end - 1]
                print(f"{otype:>20} {start:>6} `{sega}` > {end - 1} `{segb}`")

    def writeAll(self):
        info = self.info
        text = self.text
        annos = self.annos

        baseDir = self.repoLocation
        resultDir = f"{baseDir}/{TT_NAME}"
        textFile = f"{resultDir}/text.json"
        annoFile = f"{resultDir}/anno.json"

        self.textFile = textFile
        self.annoFile = annoFile

        initTree(resultDir, fresh=True)

        with open(textFile, "w") as fh:
            json.dump(dict(_ordered_segments=text), fh, ensure_ascii=False, indent=1)

        with open(annoFile, "w") as fh:
            annoStore = {}
            for (kind, aId, body, target) in annos:
                annoStore[aId] = (kind, body, target)
            json.dump(annoStore, fh, ensure_ascii=False, indent=1)

        info(f"Text file: {len(text):>7} segments to {ux(textFile)}", tm=False)
        info(f"Anno file: {len(annos):>7} annotations to {ux(annoFile)}", tm=False)
