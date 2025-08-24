# -- Project information -----------------------------------------------------
import logging
import sys
import os
import re

sys.path.insert(0, os.path.abspath('..'))
sys.path.append(os.path.abspath('extensions'))

project = 'discord.py'
author = 'Rapptz'
copyright = '2015-present, Rapptz'

version = ''
with open('../discord/__init__.py') as f:
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', f.read(), re.MULTILINE).group(1)
release = version
branch = 'master' if version.endswith('a') else 'v' + version

# -- General configuration ---------------------------------------------------
extensions = [
    'builder',
    'sphinx.ext.autodoc',
    'sphinx.ext.extlinks',
    'sphinx.ext.intersphinx',
    'sphinx.ext.napoleon',
    'sphinxcontrib_trio',
    'sphinx_inline_tabs',
    'details',
    'exception_hierarchy',
    'attributetable',
    'resourcelinks',
    'nitpick_file_ignorer',
    'colour_preview',
]

autodoc_member_order = 'bysource'
autodoc_typehints = 'none'

extlinks = {
    'issue': ('https://github.com/Rapptz/discord.py/issues/%s', 'GH-%s'),
    'ddocs': ('https://discord.com/developers/docs/%s', None),
}

intersphinx_mapping = {
  'py': ('https://docs.python.org/3', None),
  'aio': ('https://docs.aiohttp.org/en/stable/', None),
  'req': ('https://requests.readthedocs.io/en/latest/', None)
}

rst_prolog = """
.. |coro| replace:: Esta função é uma |coroutine_link|_.
.. |maybecoro| replace:: Esta função *pode ser uma* |coroutine_link|_.
.. |coroutine_link| replace:: *corrotina*
.. _coroutine_link: https://docs.python.org/3/library/asyncio-task.html#coroutine
"""

templates_path = ['_templates']
source_suffix = '.rst'
master_doc = 'index'

# Idioma em PT-BR
language = "pt_BR"

locale_dirs = ['locale/']
gettext_compact = False

exclude_patterns = ['_build']
pygments_style = 'friendly'

nitpick_ignore_files = [
  "migrating_to_async",
  "migrating_to_v1",
  "migrating",
  "whats_new",
]

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

# -- Options for HTML output -------------------------------------------------
html_experimental_html5_writer = True
html_theme = 'sphinx_rtd_theme'

html_context = {
  'discord_invite': 'https://discord.gg/r3sSKJJ',
  'discord_extensions': [
    ('discord.ext.commands', 'ext/commands'),
    ('discord.ext.tasks', 'ext/tasks'),
  ],
}

resource_links = {
  'discord': 'https://discord.gg/r3sSKJJ',
  'issues': 'https://github.com/Rapptz/discord.py/issues',
  'discussions': 'https://github.com/Rapptz/discord.py/discussions',
  'examples': f'https://github.com/Rapptz/discord.py/tree/{branch}/examples',
}

html_favicon = './images/discord_py_logo.ico'
html_static_path = ['_static']

html_search_scorer = '_static/scorer.js'
html_js_files = [
  'custom.js',
  'settings.js',
  'copy.js',
  'sidebar.js'
]

htmlhelp_basename = 'discord.pydoc'

# -- Options for LaTeX output ------------------------------------------------
latex_elements = {}
latex_documents = [
  ('index', 'discord.py.tex', 'discord.py Documentação',
   'Rapptz', 'manual'),
]

# -- Options for manual page output ------------------------------------------
man_pages = [
    ('index', 'discord.py', 'discord.py Documentação',
     ['Rapptz'], 1)
]

# -- Options for Texinfo output ----------------------------------------------
texinfo_documents = [
  ('index', 'discord.py', 'discord.py Documentação',
   'Rapptz', 'discord.py', 'Uma linha de projeto.',
   'Miscellaneous'),
]

def setup(app):
    pass