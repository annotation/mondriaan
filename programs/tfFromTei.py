import os
from tf.convert.tei import TEI


TEST_SET = set(
    """
    19160204_BLES_0083.xml
    """.strip().split()
)
TEST_SET = set(
    """
    18920227_HMKR_0001.xml
    """.strip().split()
)

AUTHOR = "Piet Mondriaan"
TITLE = "Letters"
INSTITUTE = "KNAW/Huygens Amsterdam"

GENERIC = dict(
    author=AUTHOR,
    title=TITLE,
    institute=INSTITUTE,
    language="nl",
    converters="Dirk Roorda (Text-Fabric)",
    sourceFormat="TEI",
    descriptionTf="Critical edition",
)

APP_CONFIG = dict(
    provenanceSpec=dict(
        doi="10.5281/zenodo.nnnnnn",
    )
)

ABOUT_TEXT = """
# CONTRIBUTORS

Researcher: Mariken Teeuwen

Editors: Peter Boot et al.
"""

TRANSCRIPTION_TEXT = """

The TEI has been validated and polished
before generating the TF data.
"""

DOC_MATERIAL = dict(
    about=ABOUT_TEXT,
    transcription=TRANSCRIPTION_TEXT,
)

HY = "\u2010"  # hyphen


def transform(text):
    return text.replace(",,", HY)


T = TEI(
    schema="MD",
    # sourceVersion="2023-01-31",
    sourceVersion="2023-03-20",
    # sourceVersion="2023-04-04",
    testSet=TEST_SET,
    wordAsSlot=True,
    sectionModel=dict(model="I", levels=["folder", "letter", "chunk"]),
    generic=GENERIC,
    transform=transform,
    tfVersion="0.8",
    appConfig=APP_CONFIG,
    docMaterial=DOC_MATERIAL,
    force=False,
)

T.run(os.path.basename(__file__))
