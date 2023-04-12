[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

![mondriaan](app/static/logo.png)

# Piet Mondriaan - Letters

Selected Letters of Mondriaan in Text-Fabric.

In this repository we prepare a "Proeftuin* of 14 letters of
[Mondriaan](https://en.wikipedia.org/wiki/Piet_Mondrian)
for the application of data science.

The source files, TEI-XML files, are provided by the Huygens Institute.

They have been converted to
[Text-Fabric](https://github.com/annotation/text-fabric)
representation.

The result can be readily loaded into Python programs for further processing.

See

* [about](docs/about.md) for the provenance of the data;
* [transcription](docs/transcription.md) for how the resulting data is modelled;
* [tutorial]() to get started with computing;
* [getImages]() to see how we got the images;
* [docs]() for an index to all documentation.

## Disclaimer

As the badge above indicates: this is work in progress.
Although we use this repository to develop an official website to publish the letters
by Mondriaan, nothing that you see here is a promise of what that website will
look like.

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

For reference, see the public corpus of the correspondence of Descartes in Text-Fabric on github:

* [repo](https://github.com/CLARIAH/descartes-tf)
* [tutorial](https://nbviewer.jupyter.org/github/CLARIAH/descartes-tf/blob/main/tutorial/start.ipynb)
* [search tutorial](https://nbviewer.jupyter.org/github/CLARIAH/descartes-tf/blob/main/tutorial/search.ipynb)

# Author

See [about](docs/about.md) for the authors/editors of the data.

[Dirk Roorda](https://github.com/dirkroorda) is the author of the representation in Text-Fabric of the data,
and the tutorials and documentation.
