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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'DongTai-IAST'
copyright = '2021, DongTai'
author = 'DongTai'

# The full version, including alpha/beta/rc tags
release = '1.1.0'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['recommonmark','sphinx.ext.autosectionlabel','sphinx.ext.intersphinx','sphinx_tabs.tabs','sphinx_copybutton']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_logo = "_static/洞态@2x.png"
html_static_path = ['_static']
html_css_files=['css/s5defs-roles.css','table.css']
html_theme = 'pydata_sphinx_theme'
html_theme_options = {
    "icon_links": [
        {
            "name": "GitHub",
            "url": "https://github.com/HXSecurity/DongTai",
            "icon": "fab fa-github-square",
        },
        {
            "name": "中文",
            "url": "https://doc2.dongtai.io/zh",
            "icon": "fas fa-globe-asia",
        },
        {
            "name": "英文",
            "url": "https://doc2.dongtai.io/en",
            "icon": "fas fa-globe-europe",
        },
    ],"use_edit_page_button": True,
    "show_prev_next": False,
}

html_context = {
    "github_url": "https://github.com", # or your GitHub Enterprise interprise
    "github_user": "HXSecurity",
    "github_repo": "DongTai-docs",
    "github_version": "v1.1.0",
    "doc_path": "content/zh/source/",
}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".

rst_prolog = """.. include:: <s5defs.txt>"""

locale_dirs = ['../build/locale/']   # path is example but recommended.
gettext_compact = False
