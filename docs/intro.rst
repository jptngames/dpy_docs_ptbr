
:orphan:

.. currentmodule:: discord

.. _intro:

Introdução
===========

Esta é a documentação do discord.py, uma biblioteca para Python que auxilia
na criação de aplicações que utilizam a API do Discord.

Pré-requisitos
---------------

discord.py funciona com Python 3.8 ou superior. Não há suporte para versões anteriores do Python.
Python 2.7 ou inferior não é suportado. Python 3.7 ou inferior também não é suportado.

.. _installing:

Instalação
-----------

Você pode obter a biblioteca diretamente do PyPI: ::

    python3 -m pip install -U discord.py

Se estiver usando Windows, utilize o seguinte comando: ::

    py -3 -m pip install -U discord.py

Para suporte a voz, use ``discord.py[voice]`` em vez de ``discord.py``, por exemplo: ::

    python3 -m pip install -U discord.py[voice]

Em ambientes Linux, instalar suporte a voz requer as seguintes dependências:

- `libffi <https://github.com/libffi/libffi>`_
- `libnacl <https://github.com/saltstack/libnacl>`_
- `python3-dev <https://packages.debian.org/python3-dev>`_

Para sistemas baseados em Debian, o seguinte comando instala essas dependências:

.. code-block:: shell

    $ apt install libffi-dev libnacl-dev python3-dev

Lembre-se de verificar suas permissões!

Ambientes Virtuais
~~~~~~~~~~~~~~~~~~

Às vezes você quer evitar que bibliotecas poluam instalações do sistema ou usar uma versão diferente
das bibliotecas instaladas no sistema. Você também pode não ter permissões para instalar bibliotecas globalmente.
Para isso, a biblioteca padrão a partir do Python 3.3 inclui o conceito de **Ambientes Virtuais** para
manter essas versões separadas.

Um tutorial mais completo está disponível em :doc:`py:tutorial/venv`.

Para um guia rápido:

1. Vá para o diretório do seu projeto:

    .. code-block:: shell

        $ cd seu-projeto
        $ python3 -m venv bot-env

2. Ative o ambiente virtual:

    .. code-block:: shell

        $ source bot-env/bin/activate

    No Windows, ative com:

    .. code-block:: shell

        $ bot-env\Scripts\activate.bat

3. Use o pip normalmente:

    .. code-block:: shell

        $ pip install -U discord.py

Parabéns. Agora você tem um ambiente virtual configurado.

.. note::

    Scripts executados com ``py -3`` irão ignorar qualquer ambiente virtual ativo,
    já que o ``-3`` especifica o escopo global.

Conceitos Básicos
-----------------

discord.py gira em torno do conceito de :ref:`eventos <discord-api-events>`.
Um evento é algo que você "ouve" e então responde. Por exemplo, quando uma mensagem
é enviada, você receberá um evento sobre ela que pode ser respondido.

Um exemplo rápido para mostrar como eventos funcionam:

.. code-block:: python3

    # Este exemplo requer o intent 'message_content'.

    import discord

    class MyClient(discord.Client):
        async def on_ready(self):
            print(f'Logado como {self.user}!')

        async def on_message(self, message):
            print(f'Mensagem de {message.author}: {message.content}')

    intents = discord.Intents.default()
    intents.message_content = True

    client = MyClien(intents=intents)
    client.run('seu token aqui')