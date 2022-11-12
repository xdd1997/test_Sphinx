# -- Project information -----------------------------------------------------
project = 'test_Sphinx'
copyright = '2022, xdd2026@qq.com'
author = 'xdd2026@qq.com'
release = '1.0'
language = 'zh_CN'

# -- General configuration ---------------------------------------------------
import os
import sys
sys.path.insert(0, os.path.abspath(r'..\..\src'))

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.autosummary',
    "sphinx.ext.mathjax",
    'recommonmark',
    'sphinx_copybutton',
    'sphinx_toggleprompt'
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# html_theme = "sphinx_book_theme"
html_theme = 'sphinx_rtd_theme'
toggleprompt_offset_right = 35

html_static_path = ['_static']
