import os
from tf.convert.tei import TEI


AUTHOR = "Piet Mondriaan"
TITLE = "Letters"
INSTITUTES = dict(
    RKD=dict(
        name="Nederlands Instituut voor Kunstgeschiedenis",
        place="Den Haag",
        contributors=[
            "Wietse Coppes",
            "Sabine Craft-Giepmans",
            "Reinier van 't Zelfde",
        ],
    ),
    Huygens=dict(
        name="Huygens Instituut",
        place="Amsterdam",
        contributors=["Leo Jansen", "Peter Boot", "Beatrice Nava", "Mariken Teeuwen"],
    ),
    HuC=dict(
        name="Humanities Cluster",
        place="Amsterdam",
        contributors=[
            "Hennie Brugman",
            "Hayco de Jong",
            "Bram Buitendijk",
            "Sebastiaan van Daalen",
            "Dirk Roorda",
        ],
    ),
)
COLLABORATORS = dict()

GENERIC = dict(
    author=AUTHOR,
    title=TITLE,
    language="nl",
    converter="Dirk Roorda (Text-Fabric)",
    sourceFormat="TEI",
    descriptionTf="Critical edition",
)
for (i, (acro, info)) in enumerate(sorted(INSTITUTES.items())):
    i1 = i + 1
    GENERIC[f"institute{i1}"] = acro
    GENERIC[f"institute_name{i1}"] = info["name"]
    GENERIC[f"institute_place{i1}"] = info["place"]
    GENERIC[f"institute_contributors{i1}"] = ", ".join(info["contributors"])

APP_CONFIG = dict(
    provenanceSpec=dict(
        doi="10.5281/zenodo.nnnnnn",
    )
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
    tfVersion="0.8.2pre",
    appConfig=APP_CONFIG,
)

T.run(os.path.basename(__file__))
