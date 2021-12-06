# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
import shutil
from pathlib import Path
sys.path.insert(0, os.path.abspath('..'))

# copy the example readmes to this directory
this_directory = Path(__file__).parent
example_directory = this_directory.parent / 'examples'
example_readmes = [example_directory / 'ApertureOptimisation' / 'README.md',
                   example_directory / 'PhaseSpaceOptimisation' / 'README.md']

for read_me in example_readmes:
    try:
        shutil.copy(read_me, (this_directory / os.path.split(read_me.parent)[1]).with_suffix('.md'))
    except FileNotFoundError:
        print(f'Could not find ApertureOptimisation readme at {read_me}.]n continuing...')

# -- Project information -----------------------------------------------------

project = 'TopasBayesOpt'
copyright = '2021, Brendan Whelan(s)'
author = 'Brendan Whelan(s)'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.

extensions = [
'sphinx.ext.autodoc',
'sphinx.ext.coverage',
'sphinx.ext.githubpages',
'sphinx.ext.napoleon',
'sphinx.ext.todo',
'recommonmark',
'sphinx_markdown_tables']

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

