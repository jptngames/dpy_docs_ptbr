:orphan:

.. _quickstart:

.. currentmodule:: discord

Guia Rápido
============

Esta página dá uma breve introdução à biblioteca. Ela assume que você já tem a biblioteca instalada,
se não tiver, confira a parte de :ref:`installing`.

Um Bot Simples e Minimalista
-------------------

Vamos criar um bot que responde a uma mensagem específica e te guiar passo a passo.

Ele se parece com isso:

.. code-block:: python3

    # Este exemplo requer a intent 'message_content'.

    import discord

    intents = discord.Intents.default()
    intents.message_content = True

    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'Conectado como {client.user}')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if message.content.startswith('$hello'):
            await message.channel.send('Olá!')

    client.run('seu token aqui')

Vamos nomear este arquivo como ``example_bot.py``. Tenha certeza de não nomeá-lo como ``discord.py``,
pois isso entraria em conflito com a biblioteca.

Há bastante coisa acontecendo aqui, então vamos explicar passo a passo:

1. A primeira linha apenas importa a biblioteca. Se isso levantar um :exc:`ModuleNotFoundError` ou
   :exc:`ImportError`, vá até a seção :ref:`installing` para instalar corretamente.
2. Em seguida, criamos uma instância de :class:`Client`. Este cliente é nossa conexão com o Discord.
3. Depois usamos o decorador :meth:`Client.event` para registrar um evento. Esta biblioteca possui
   muitos eventos. Como ela é assíncrona, fazemos as coisas em um estilo de "callback".

   Um callback é basicamente uma função chamada quando algo acontece. No nosso caso,
   o evento :func:`on_ready` é chamado quando o bot terminou de logar e se configurar,
   e o evento :func:`on_message` é chamado quando o bot recebe uma mensagem.
4. Como o evento :func:`on_message` é disparado para *todas* as mensagens recebidas, precisamos
   garantir que vamos ignorar as mensagens enviadas por nós mesmos. Fazemos isso verificando se
   o :attr:`Message.author` é o mesmo que o :attr:`Client.user`.
5. Depois, verificamos se o :class:`Message.content` começa com ``'$hello'``. Se começar,
   então enviamos uma mensagem no canal em que foi usado com ``'Olá!'``. Essa é uma forma básica de
   lidar com comandos, que pode ser futuramente automatizada com o framework :doc:`./ext/commands/index`.
6. Finalmente, executamos o bot com nosso token de login. Se precisar de ajuda para conseguir seu
   token ou criar um bot, veja a seção :ref:`discord-intro`.

Agora que criamos um bot, precisamos *executar* o bot. Felizmente, isso é simples, já que
este é apenas um script Python que podemos rodar diretamente.

No Windows:

.. code-block:: shell

    $ py -3 example_bot.py

No macOS, Linux:

.. code-block:: shell

    $ python3 example_bot.py

Agora você pode brincar um pouco com seu bot básico.
Tradução feita por `jptngames <https://github.com/jptngames>`_