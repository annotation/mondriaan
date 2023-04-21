import os
from tf.convert.tei import TEI


AUTHOR = "Piet Mondriaan"
TITLE = "Letters"
INSTITUTE = "RKD Den Haag; KNAW/HuCHuygens Amsterdam"

GENERIC = dict(
    author=AUTHOR,
    title=TITLE,
    institute=INSTITUTE,
    language="nl",
    projectleaders="Hennie Brugman, Mariken Teeuwen",
    converters="Dirk Roorda (Text-Fabric)",
    editors="Wietse Coppes; Leo Jansen",
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

Authors and contributors

*   Piet Mondriaan (original author)
*   Leo Jansen (editor)
*   Wietse Coppes (editor)
*   Peter Boot (content specialist)
*   Sabine Craft-Giepmans (RKD data architect)
*   Reinier van 't Zelfde (RKD data architect)
*   Mariken Teeuwen (Huygens researcher)
*   Hennie Brugman (HuC software architect)
*   Hayco de Jong (HuC data modeller and software developer)
*   Bram Buitendijk (HuC senior software developer)
*   Sebastiaan van Daalen (HuC interface developer)
*   Dirk Roorda (Huc data modeller and software developer)
tors: Peter Boot et al.
"""

TRANSCRIPTION_TEXT = """

The TEI has been validated and polished
before generating the TF data.

The initial TF data has been fed into Spacy to detect tokens and sentences,
and the result has been integrated into a new version of the TF data.
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
    sourceVersion="2023-03-20",
    # sourceVersion="2023-04-04",
    testSet=None,
    wordAsSlot=False,
    sectionModel=dict(model="I", levels=["folder", "letter", "chunk"]),
    generic=GENERIC,
    transform=transform,
    tfVersion="0.8.1pre",
    appConfig=APP_CONFIG,
    docMaterial=DOC_MATERIAL,
    force=False,
)

T.run(os.path.basename(__file__))
