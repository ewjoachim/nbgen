[![PyPI version](https://badge.fury.io/py/nbgen.svg)](https://badge.fury.io/py/nbgen)

# `nbgen` generates a Jupyter Notebook and slides from your data

This script is a wrapper around simple Jupyter functions to simplify the task
of automating the creation of Jupyter Notebooks for datasets.


## Installation

	pip install nbgen


## Usage information

	nbgen -h

	nbgen nb ./sample.py test "1 + 3"


## More details ?

`nbgen` doesn't know how to load your data, or how to present them, or anything that's your job.
You're invited to create an executable (like a python script) that will receive input and output
Notebook cells in [json format](http://nbformat.readthedocs.io/en/latest/format_description.html#cell-types). See [sample.py](sample.py) for an example of this.

`nbgen` then takes care of creating a Notebook file and saving it, and executing all the cells.

`nbgen` takes 3 arguments :

- the executable path (can be relative to your current position)
- the name of the Notebook file to create (minus `.ipynb`)
- arbitrary string to pass to the executable


## You mentionned slides ?

Yes ! Jupyter supports [exporting into slides](http://echorand.me/presentation-slides-with-jupyter-notebook.html#.V4S2epOLSHo).
As a convenience, the ``slide`` subcommand will do the export for you.

	nbgen slides ./sample.py test "1 + 3"

> Note :
>
> If you don't specify a local path for `reveal.js` using `--reveal`, a CDN will be used. In this case, the slide
> will only work if you have internet access.

## Feedback ? Contributions ?

All contacts are welcome through issues and pull requests, [Twitter](https://twitter.com/Ewjoachim) or anything. Don't forget to follow the [Code of Conduct](COC.md), it's important !

