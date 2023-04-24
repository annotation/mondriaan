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

## Purpose

We make a test bed for the data transformations from the original TEI through
Text-Fabric to Web Annotations, the format that will drive the resulting
website.

In this repository you can see and follow and reproduce the whole chain.

The results in this repo can be used to visualise the effects of data design
on the interface, so that we can get feedback on them, in order to arrive
at a display that meets the demands of the Mondriaan project.

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

    This will fetch the corpus and open a browser window where you can leaf
    through the texts and make queries. 
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

## Documentation

We have published several
[tutorial](https://nbviewer.org/github/annotation/mondriaan/blob/master/tutorial/start.ipynb)
notebooks that show how the Text-Fabric version of the data can be used.


Use
[transcription](docs/transcription.md)
as a reference to the ins and outs of the TF encoding of the data.
This file is one click away when you are using Text-Fabric. 

## Who and what

Several memory institutions and their associated developers are working to
make rich datasets available to the public and researchers.

The Mondriaan Letters collection is such a dataset for which active
development is taking place as part of the
[Mondrian edit project](https://www.huygens.knaw.nl/en/projecten/mondrian-edit-project/).

Participating institutes are:

*   [RKD](https://rkd.nl/en/)
*   [Huygens Institute](https://www.huygens.knaw.nl/en/)
*   [Humanities Cluster](https://huc.knaw.nl)

## Provenance

See
[about](docs/about.md)
for the provenance of the data and a more detailed list of all people
involved.

## Disclaimer

As the badge above indicates: this is work in progress.
Although we use this repository to develop an official website to publish the
letters by Mondriaan, nothing that you see here is a promise of what that
website will look like.

## Status

*   2023-04-21
    Source data, Text-Fabric data and Web annotation data all present,
    the pipeline works.
    The conversion aims at conserving all information that is present in the
    source throughout all stages in the pipeline.
    Later we should discuss which elements should be rendered and in what
    ways, and with what controls on the interface.

*   2023-04-12
    Initial content, the source data is not yet present, hence the programs
    do not yet work in this context. They do work in another repo, but that
    repo is not accessible.

## References

See some other TF datasets on GitHub:

*   Herman Melville, Moby Dick
    *   [repo](https://github.com/annotation/mobydick)
    *   [tutorial](https://nbviewer.jupyter.org/github/annotation/mobydick/blob/main/tutorial/start.ipynb)
    *   [pandas tutorial](https://nbviewer.jupyter.org/github/annotation/mobydick/blob/main/tutorial/pandas.ipynb)

*   Descartes, Letters
    *   [repo](https://github.com/CLARIAH/descartes-tf)
    *   [tutorial](https://nbviewer.jupyter.org/github/CLARIAH/descartes-tf/blob/main/tutorial/start.ipynb)
    *   [search tutorial](https://nbviewer.jupyter.org/github/CLARIAH/descartes-tf/blob/main/tutorial/search.ipynb)

*   or one of these
    [corpora](https://annotation.github.io/text-fabric/tf/about/corpora.html).

# Author

For those who have worked on the source material, and the ones that
work on the Mondriaan project, see
[about](docs/about.md).

[Dirk Roorda](https://github.com/dirkroorda)
has set up and organized this repo, and designed the data conversions.
He has also written Text-Fabric.
