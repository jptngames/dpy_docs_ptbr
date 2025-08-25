- `Discord API <https://discord.gg/discord-api>`_
discord.py
==========

.. image:: https://discord.com/api/guilds/336642139381301249/embed.png
   :target: https://discord.gg/r3sSKJJ
   :alt: Convite para o servidor Discord
.. image:: https://img.shields.io/pypi/v/discord.py.svg
   :target: https://pypi.python.org/pypi/discord.py
   :alt: Informações da versão no PyPI
.. image:: https://img.shields.io/pypi/pyversions/discord.py.svg
   :target: https://pypi.python.org/pypi/discord.py
   :alt: Versões de Python suportadas pelo PyPI

Um wrapper de API moderno, fácil de usar, rico em recursos e pronto para `async` para Discord, escrito em Python.

Principais Recursos
-------------------

- API moderna e Pythonica usando ``async`` e ``await``.
- Manipulação adequada de limites de taxa (rate limits).
- Otimizado em velocidade e memória.

Instalação
----------

**Python 3.8 ou superior é necessário**

Para instalar a biblioteca sem suporte completo a voz, basta executar o seguinte comando:

.. note::

    É recomendado utilizar um `Ambiente Virtual <https://docs.python.org/3/library/venv.html>`__ para instalar a biblioteca, especialmente em Linux, onde o Python do sistema é gerenciado externamente e restringe quais pacotes você pode instalar.

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U discord.py

    # Windows
    py -3 -m pip install -U discord.py

Caso queira suporte a voz, execute o seguinte comando:

.. code:: sh

    # Linux/macOS
    python3 -m pip install -U "discord.py[voice]"

    # Windows
    py -3 -m pip install -U discord.py[voice]

Para instalar a versão de desenvolvimento, faça o seguinte:

.. code:: sh

    $ git clone https://github.com/Rapptz/discord.py
    $ cd discord.py
    $ python3 -m pip install -U .[voice]

Pacotes Opcionais
~~~~~~~~~~~~~~~~~~

* `PyNaCl <https://pypi.org/project/PyNaCl/>`__ (para suporte a voz)

Observe que, ao instalar suporte a voz no Linux, você deve instalar os seguintes pacotes via seu gerenciador de pacotes favorito (ex: ``apt``, ``dnf``, etc) antes de executar os comandos acima:

* libffi-dev (ou ``libffi-devel`` em alguns sistemas)
* python-dev (ex: ``python3.8-dev`` para Python 3.8)

Exemplo Rápido
--------------

.. code:: py

    import discord

    class MyClient(discord.Client):
        async def on_ready(self):
            print('Logado como', self.user)

        async def on_message(self, message):
            # não responder a nós mesmos
            if message.author == self.user:
                return

            if message.content == 'ping':
                await message.channel.send('pong')

    intents = discord.Intents.default()
    intents.message_content = True
    client = MyClient(intents=intents)
    client.run('token')

Exemplo de Bot
~~~~~~~~~~~~~~

.. code:: py

    import discord
    from discord.ext import commands

    intents = discord.Intents.default()
    intents.message_content = True
    bot = commands.Bot(command_prefix='>', intents=intents)

    @bot.command()
    async def ping(ctx):
        await ctx.send('pong')

    bot.run('token')

Mais exemplos podem ser encontrados no diretório examples.

Links
------

- `Documentação <https://discordpy.readthedocs.io/en/latest/index.html>`_
- `Servidor Oficial no Discord <https://discord.gg/r3sSKJJ>`_
- `API do Discord <https://discord.gg/discord-api>`_

Tradução
---------

Essa documentação foi traduzida voluntariamente e você também pode contribuir!

- Colabore reportando erros ortográficos ou quaisquer outros problemas nos `issues do GitHub <https://github.com/jptngames/dpy_docs_ptbr/issues/new/choose>`_.
- Esta tradução tem como objetivo ajudar desenvolvedores brasileiros/portugueses a compreender melhor a documentação do discord.py. Todos os direitos sobre o projeto oficial (lib discord.py) pertencem a Rapptz e seus colaboradores.