# Project and Participating Institutes

[Mondrian edit project](https://www.huygens.knaw.nl/en/projecten/mondrian-edit-project/).

We refer to institutes participating in this project by means of the following 
acronyms:

*   [RKD](https://rkd.nl/en/)
*   [Huygens](https://www.huygens.knaw.nl/en/)
*   [HuC](https://huc.knaw.nl)

# Data provenance

## Textual data

The source files, TEI-XML files, are provided by `Huygens`.

The conversion involves these steps:

*   TEI to TF, i.e. [Text-Fabric](https://github.com/annotation/text-fabric)
*   TF + Spacy to TF, i.e. we have used Spacy to detect word and sentence
    boundaries in the plain text, which we have imported in the TF dataset.

The details of this workflow can be found in the notebook
[convertExpress](https://nbviewer.jupyter.org/github/annotation/mondriaan/blob/master/programs/convertExpress.ipynb).

*   TF to WATM, i.e. Web Annotation Text Model. A files with text segments
    and a file with annotations to these segments. This step retains all
    information that is present in the TF data.

This is done in
[watmFromTf](https://nbviewer.jupyter.org/github/annotation/mondriaan/blob/master/programs/watmFromTf.ipynb)
which also contains extensive testing of that conversion against information
loss.

Both notebooks can be used to *reproduce* the results from scratch.

See
[transcription](docs/transcription.md)
for a detailed account of how the resulting TF data is modelled.

## Image data

For now, the images are thumbnails obtained from the `RKD` website,
see
[getImages](https://nbviewer.org/github/annotation/mondriaan/blob/master/programs/getImages.ipynb)
to see how we did that.

# Authors and contributors

*   Piet Mondriaan (original author)
*   Leo Jansen (`Huygens` digital editions)
*   Wietse Coppes (`RKD` research and development, conservator Mondriaan archives)
*   Peter Boot (`Huygens` researcher and content specialist)
*   Beatrice Nava (`Huygens` innovator digital editions)
*   Sabine Craft-Giepmans (`RKD` head research and development)
*   Reinier van 't Zelfde (`RKD` information architect)
*   Mariken Teeuwen
    (`Huygens` head digital editions, professor at Leiden university)
*   Hennie Brugman (`HuC` software architect, team leader Text)
*   Hayco de Jong (`HuC` data modeller and software developer in team Text)
*   Bram Buitendijk (`HuC` senior software developer in team Text)
*   Sebastiaan van Daalen (`HuC` interface developer in team Text)
*   Dirk Roorda (`Huc` data modeller and software developer in team Text)





# Corpus annotation - mondriaan

## author

Piet Mondriaan


## title

Letters


## language

nl


## converter

Dirk Roorda (Text-Fabric)


## sourceFormat

TEI


## descriptionTf

Critical edition


## institute1

HuC (Humanities Cluster) Amsterdam


## institute2

Huygens Instituut Amsterdam


## institute3

RKD (Nederlands Instituut voor Kunstgeschiedenis) Den Haag


## contributors1

Hennie Brugman, Hayco de Jong, Bram Buitendijk, Sebastiaan van Daalen, Dirk Roorda


## contributors2

Leo Jansen, Peter Boot, Beatrice Nava, Mariken Teeuwen


## contributors3

"Wietse Coppes, Sabine Craft-Giepmans, Reinier van 't Zelfde"


## version

0.8.5


## teiVersion

2023-05-11


## schema

TEI + MD


## Conversion

Converted from TEI to Text-Fabric

## See also

*   [transcription](transcription.md)
