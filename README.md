[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

![mondriaan](docs/images/logo.png)
![rkd](docs/images/rkd.png)
![huygens](docs/images/huygens.png)
![huc](docs/images/huc.png)
![tf](docs/images/tf-small.png)

# Piet Mondriaan - Letters

Selected Letters of Mondriaan in Text-Fabric.

In this repository we prepare a "Proeftuin* of 14 letters of
[Mondriaan](https://rkd.nl/en/explore/artists/56854)
for the application of data science.

The source files, TEI-XML files, are provided by the Huygens Institute.

They have been converted to
[Text-Fabric](https://github.com/annotation/text-fabric)
representation.

The result can be readily loaded into Python programs for further processing.

See

* [about](docs/about.md)
  for the provenance of the data;
* [transcription](docs/transcription.md)
  for how the resulting data is modelled;
* [tutorial](https://nbviewer.org/github/annotation/mondriaan/blob/master/tutorial/start.ipynb)
  to get started with computing;
* [getImages](https://nbviewer.org/github/annotation/mondriaan/blob/master/programs/getImages.ipynb)
  to see how we got the images;

## Who and what

Several memory institutions and their associated developers are working to make
rich datasets available to the public and researchers.

The Mondriaan Letters collection is such a dataset for which active development is
taking place.

The participating institutes are:

*   [RKD](https://rkd.nl/en/)
*   [Huygens Institute](https://www.huygens.knaw.nl/en/)
*   [Humanities Cluster](https://huc.knaw.nl)

We make a test bed for the data transformations from the original TEI through
Text-Fabric to Web Annotations, the format that will drive the resulting website.

In this repository you can see and follow and reproduce the whole chain.

## Disclaimer

As the badge above indicates: this is work in progress.
Although we use this repository to develop an official website to publish the letters
by Mondriaan, nothing that you see here is a promise of what that website will
look like.

## Status

*   2023-04-21
    Source data, Text-Fabric data and Web annotation data all present,
    the pipeline works.
    The conversion aims at conserving all information that is present in the source
    throughout all stages in the pipeline.
    Later we should discuss which elements should be rendered and in what ways,
    and with what controls on the interface.

*   2023-04-12
    Initial content, the source data is not yet present, hence the programs do not yet
    work in this context. They do work in another repo, but that repo is not 
    accessible.

## Quick start

*   if you do not have
    [Python](https://www.python.org)
    installed, install it.

*   if you do not have
    [Text-Fabric](https://github.com/annotation/text-fabric)
    installed, install it by opening a terminal/command line and saying:

    ``` sh
    pip install 'text-fabric[all]'
    ```

    or, if you have it already, check whether an upgrade is available:

    ``` sh
    pip install --upgrade 'text-fabric[all]'
    ```

*   Start the Text-Fabric browser, from the command line:

    ``` sh
    text-fabric annotation/mondriaan
    ```

    This will fetch the corpus and open a browser window where you can leaf through the
    texts and make queries. 
    Corpus information and Help are provided in the left side bar.

*   Alternatively, you can work in a Jupyter notebook:

    ``` sh
    pip install jupyterlab
    ```

    ``` sh
    jupyter lab
    ```

    and inside the notebook, in a code cell, run

    ``` python
    from tf.app import use

    A = use('annotation/mondriaan')
    ```

    which will also download the corpus.

In both cases, the corpus ends up in your home directory,
under `text-fabric-data`.

We have published several notebooks that show how the data is converted
and how the Text-Fabric version of the data can be used.

*   [tutorial](https://nbviewer.org/github/annotation/mondriaan/blob/master/tutorial/start.ipynb)
    on using Text-Fabric to explore this corpus;
*   [convertExpress](https://nbviewer.jupyter.org/github/annotation/mondriaan/blob/master/programs/convertExpress.ipynb)
    on converting TEI to Text-Fabric and using an NLP pipeline to delineate tokens and sentences;
*   [watmFromTf](https://nbviewer.jupyter.org/github/annotation/mondriaan/blob/master/programs/watmFromTf.ipynb)
    on converting TF to text segments plus web annotations, without information loss.

For reference, see some other public datasets on GitHub:

*   Herman Melville, Moby Dick
    *   [repo](https://github.com/annotation/mobydick)
    *   [tutorial](https://nbviewer.jupyter.org/github/annotation/mobydick/blob/main/tutorial/start.ipynb)
    *   [pandas tutorial](https://nbviewer.jupyter.org/github/annotation/mobydick/blob/main/tutorial/pandas.ipynb)

*   Descartes, Letters
    *   [repo](https://github.com/CLARIAH/descartes-tf)
    *   [tutorial](https://nbviewer.jupyter.org/github/CLARIAH/descartes-tf/blob/main/tutorial/start.ipynb)
    *   [search tutorial](https://nbviewer.jupyter.org/github/CLARIAH/descartes-tf/blob/main/tutorial/search.ipynb)

# Authors and contributors

*   Piet Mondriaan (original author)
*   Leo Jansen (editor)
*   Wietse Coppes (editor)
*   Sabine Craft-Giepmans (RKD data architect)
*   Reinier van 't Zelfde (RKD data architect)
*   Mariken Teeuwen (Huygens researcher)
*   Hennie Brugman (HuC software architect)
*   Hayco de Jong (HuC data modeller and software developer)
*   Bram Buitendijk (HuC senior software developer)
*   Sebastiaan van Daalen (HuC interface developer)
*   Dirk Roorda (Huc data modeller and software developer)

See [about](docs/about.md) for the authors/editors of the data.

[Dirk Roorda](https://github.com/dirkroorda) has set up and organized this repo,
and designed the data conversions.
He has also written Text-Fabric.
