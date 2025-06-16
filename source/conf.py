# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = "MapBoards Pro"
copyright = "2020-%Y, Icarus Soft Landings, LLC"
author = "Icarus"
release = version = "2.815"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ["sphinx_togglebutton"]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = "alabaster"
# html_theme = "haiku"
html_theme = "classic"
# html_theme = "sphinxdoc"
# html_theme_options = {
#     "navigation_with_keys": "true",
# }
html_theme_options = {
    "rightsidebar": "false",
    "relbarbgcolor": "black",
    "bgcolor": "black",
    "textcolor": "white",
    "sidebarwidth": 300,
    "navigation_with_keys": "true",
    "stickysidebar": "true",
    "body_max_width": "none",
    "page_width": "auto",
}
html_sidebars = {
    "**": ["globaltoc.html", "sourcelink.html", "searchbox.html"],
    "using/windows": ["windows-sidebar.html", "searchbox.html"],
}
html_copy_source = False
html_use_index = False

html_static_path = ["_static"]
html_css_files = ["custom.css", "hacks.css"]
