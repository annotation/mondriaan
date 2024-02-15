import sys

from tf.core.helpers import console

from tf.app import use
from tf.convert.tei import TEI
from tf.convert.addnlp import NLPipeline
from tf.convert.watm import WATM
from tf.core.files import dirNm, getLocation, abspath
from tf.core.timestamp import DEEP, TERSE

# from tf.advanced.helpers import dm


HELP = """Convert the corpus data.

USAGE

python make.py tasks

Converts data from TEI files

FLAGS

--help
    Print this help text

--silent
    To run a bit more silent

ARGS

tfversion
    Any arg that contains a . is considered to be the tf version number.
    If no version is passed, we resort to the hard coded default.

TASKS

tf
    Produce text-fabric data
watm
    Produce text/anno repo data
all
    Shorthand for: tf watm
"""

TASKS = set(
    """
    tf
    watm
""".strip().split()
)

TF_VERSION = "0.0.0test"


class Make:
    def __init__(self, tfVersion):
        self.tfVersion = tfVersion

        self.good = True
        self.silent = False

        repoBase = dirNm(dirNm(abspath(__file__)))
        (self.backend, self.org, self.repo, self.relative) = getLocation(
            targetDir=repoBase
        )

    def produceTf(self):
        good = self.good
        silent = self.silent

        if not good:
            if not silent:
                console("Skipping 'produce TF' because of an error condition")
            return

        tfVersion = self.tfVersion
        verbose = -1 if silent else 0
        loadVerbose = DEEP if silent else TERSE

        Tei = TEI(verbose=verbose, tei=0, tf=f"{tfVersion}pre")

        console("Checking TEI ...")

        if not Tei.task(check=True, verbose=verbose, validate=True):
            self.good = False
            return

        console("Converting TEI to TF ...")

        if not Tei.task(convert=True, verbose=verbose):
            self.good = False
            return

        console("Loading TF ...")

        if not Tei.task(load=True, verbose=verbose):
            self.good = False
            return

        if not silent:
            console("Set up TF-app ...")

        if not Tei.task(app=True, verbose=verbose):
            self.good = False
            return

        console("Add tokens and sentences ...")

        org = self.org
        repo = self.repo
        backend = self.backend

        Apre = use(
            f"{org}/{repo}:clone", backend=backend, checkout="clone", silent=loadVerbose
        )
        NLP = NLPipeline(lang="it", ner=True, parser=True, verbose=verbose, write=True)
        NLP.loadApp(Apre)
        NLP.task(plaintext=True, lingo=True, ingest=True)

        if not NLP.good:
            self.good = False
            return

        if not silent:
            console("Set up TF-app ...")

        if not Tei.task(apptoken=True, verbose=-1):
            self.good = False
            return

        if not Tei.task(load=True, verbose=-1):
            self.good = False
            return

    def produceWatm(self):
        good = self.good
        silent = self.silent

        if not good:
            if not silent:
                console("Skipping 'produce WATM' because of an error condition")
            return

        console("Producing WATM")

        backend = self.backend
        org = self.org
        repo = self.repo

        if not silent:
            console("Loading TF ...")

        loadVerbose = DEEP if silent else TERSE

        A = use(
            f"{org}/{repo}:clone", backend=backend, checkout="clone", silent=loadVerbose
        )

        WA = WATM(A, "tei", skipMeta=False, silent=silent)
        WA.makeText()
        WA.makeAnno()
        WA.writeAll()
        WA.testAll()

    def run(self, tasks, silent):
        self.silent = silent

        for task in TASKS:
            if task not in tasks:
                continue

            if task == "tf":
                self.produceTf()

            elif task == "watm":
                self.produceWatm()

        return 0 if self.good else 1


def main(cargs=sys.argv[1:]):
    if "--help" in cargs:
        console(HELP)
        return 0

    unrecognized = set()
    tasks = set()
    silent = False
    version = None

    for carg in cargs:
        if carg == "--silent":
            silent = True
        elif carg == "all":
            for task in TASKS:
                tasks.add(task)
        elif carg in TASKS:
            tasks.add(carg)
        elif "." in carg:
            version = carg
        else:
            unrecognized.add(carg)

    if version is None:
        console(f"No version for the TF data given. Using default: {TF_VERSION}")
    else:
        console(f"Using TF version: {version}")

    if len(unrecognized):
        console(HELP)
        console(f"Unrecognized arguments: {', '.join(sorted(unrecognized))}")
        return -1

    if len(tasks) == 0:
        console("Nothing to do")
        return 0

    Mk = Make(version)

    return Mk.run(tasks, silent)


if __name__ == "__main__":
    sys.exit(main())
