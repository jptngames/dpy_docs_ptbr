# -- Project information -----------------------------------------------------
import logging
import sys
import os
import re

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('extensions'))

# -- Configurações básicas ------------------------------------------------
project = "discord.py"
author = "Rapptz"
release = "1.0"

# -- Extensões do Sphinx --------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_autodoc_typehints",
    "sphinx_copybutton",
    "sphinx.ext.extlinks",
    "sphinx.ext.intersphinx",
    "sphinxcontrib_trio",
    "sphinx_inline_tabs",
]

# Ordem de membros e typehints
autodoc_member_order = 'bysource'
autodoc_typehints = 'none'

# Extlinks (links rápidos)
extlinks = {
    'issue': ('https://github.com/Rapptz/discord.py/issues/%s', 'GH-%s'),
    'ddocs': ('https://discord.com/developers/docs/%s', None),
}

# Intersphinx
intersphinx_mapping = {
    'py': ('https://docs.python.org/3', None),
    'aio': ('https://docs.aiohttp.org/en/stable/', None),
    'req': ('https://requests.readthedocs.io/en/latest/', None)
}

# RST prolog (substituições para português)
rst_prolog = """
.. |coro| replace:: Esta função é uma |coroutine_link|_.
.. |maybecoro| replace:: Esta função *pode ser uma* |coroutine_link|_.
.. |coroutine_link| replace:: *corrotina*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

# -- Templates e paths ----------------------------------------------------
templates_path = ["_templates"]
exclude_patterns = ['_build']

# -- Idioma ---------------------------------------------------------------
language = "pt_BR"
locale_dirs = ['locale/']
gettext_compact = False

# -- HTML -----------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "discord.py (Documentação em Português)"

# Contexto adicional
html_context = {
    'discord_invite': 'https://discord.gg/r3sSKJJ',
    'discord_extensions': [
        ('discord.ext.commands', 'ext/commands'),
        ('discord.ext.tasks', 'ext/tasks'),
    ],
}

# Filtro para warnings inúteis de tradução
def _i18n_warning_filter(record: logging.LogRecord) -> bool:
    return not record.msg.startswith(
        (
            'inconsistent references in translated message',
            'inconsistent term references in translated message',
        )
    )
_i18n_logger = logging.getLogger('sphinx')
_i18n_logger.addFilter(_i18n_warning_filter)

# Arquivos JavaScript adicionais
html_js_files = [
    'custom.js',
    'settings.js',
    'copy.js',
    'sidebar.js'
]

# Favicon
html_favicon = './images/discord_py_logo.ico'

# -- Opções de saída adicionais (LaTeX, manual, Texinfo) -----------------
latex_elements = {}
latex_documents = [
    ('index', 'discord.py.tex', 'discord.py Documentação',
     'Rapptz', 'manual'),
]

man_pages = [
    ('index', 'discord.py', 'discord.py Documentação', ['Rapptz'], 1)
]

texinfo_documents = [
    ('index', 'discord.py', 'discord.py Documentação',
     'Rapptz', 'discord.py', 'Uma linha de projeto.',
     'Miscellaneous'),
]

def setup(app):
    pass