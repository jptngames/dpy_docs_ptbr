.. _discord_ext_tasks:

``discord.ext.tasks`` -- helpers para asyncio.Task
====================================================

.. versionadded:: 1.1.0

Uma das operações mais comuns ao criar um bot é ter um loop rodando em segundo plano em um intervalo específico. Esse padrão é muito comum, mas existem várias coisas para se atentar:

- Como lidar com :exc:`asyncio.CancelledError`?
- O que faço se a internet cair?
- Qual é o número máximo de segundos que posso usar no sleep?

O objetivo desta extensão do discord.py é abstrair todas essas preocupações de você.

Formas de Fazer (Receitas? 🤨)
---------

Uma tarefa simples em segundo plano dentro de um :class:`~discord.ext.commands.Cog`:

.. code-block:: python3

    from discord.ext import tasks, commands

    class MyCog(commands.Cog):
        def __init__(self):
            self.index = 0
            self.printer.start()

        def cog_unload(self):
            self.printer.cancel()

        @tasks.loop(seconds=5.0)
        async def printer(self):
            print(self.index)
            self.index += 1

Adicionando uma exceção para tratar durante a reconexão:

.. code-block:: python3

    import asyncpg
    from discord.ext import tasks, commands

    class MyCog(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.data = []
            self.batch_update.add_exception_type(asyncpg.PostgresConnectionError)
            self.batch_update.start()

        def cog_unload(self):
            self.batch_update.cancel()

        @tasks.loop(minutes=5.0)
        async def batch_update(self):
            async with self.bot.pool.acquire() as con:
                # atualização em lote aqui...
                pass

Executando um loop um número específico de vezes antes de sair:

.. code-block:: python3

    from discord.ext import tasks
    import discord

    @tasks.loop(seconds=5.0, count=5)
    async def slow_count():
        print(slow_count.current_loop)

    @slow_count.after_loop
    async def after_slow_count():
        print('feito!')

    class MyClient(discord.Client):
        async def setup_hook(self):
            slow_count.start()

Aguardando até que o bot esteja pronto antes do loop começar:

.. code-block:: python3

    from discord.ext import tasks, commands

    class MyCog(commands.Cog):
        def __init__(self, bot):
            self.index = 0
            self.bot = bot
            self.printer.start()

        def cog_unload(self):
            self.printer.cancel()

        @tasks.loop(seconds=5.0)
        async def printer(self):
            print(self.index)
            self.index += 1

        @printer.before_loop
        async def before_printer(self):
            print('aguardando...')
            await self.bot.wait_until_ready()

Fazendo algo durante o cancelamento:

.. code-block:: python3

    from discord.ext import tasks, commands
    import asyncio

    class MyCog(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self._batch = []
            self.lock = asyncio.Lock()
            self.bulker.start()

        async def cog_unload(self):
            self.bulker.cancel()

        async def do_bulk(self):
            # inserção em lote aqui
            ...

        @tasks.loop(seconds=10.0)
        async def bulker(self):
            async with self.lock:
                await self.do_bulk()

        @bulker.after_loop
        async def on_bulker_cancel(self):
            if self.bulker.is_being_cancelled() and len(self._batch) != 0:
                # se fomos cancelados e ainda temos dados restantes...
                # vamos inserir no banco de dados
                await self.do_bulk()

Fazendo algo em um horário específico a cada dia:

.. code-block:: python3

    import datetime
    from discord.ext import commands, tasks

    utc = datetime.timezone.utc

    # Se nenhum tzinfo for dado, assume-se UTC.
    time = datetime.time(hour=8, minute=30, tzinfo=utc)

    class MyCog(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.my_task.start()

        def cog_unload(self):
            self.my_task.cancel()

        @tasks.loop(time=time)
        async def my_task(self):
            print("Minha tarefa está rodando!")

Fazendo algo em múltiplos horários específicos por dia:

.. code-block:: python3

    import datetime
    from discord.ext import commands, tasks

    utc = datetime.timezone.utc

    # Se nenhum tzinfo for dado, assume-se UTC.
    times = [
        datetime.time(hour=8, tzinfo=utc),
        datetime.time(hour=12, minute=30, tzinfo=utc),
        datetime.time(hour=16, minute=40, second=30, tzinfo=utc)
    ]

    class MyCog(commands.Cog):
        def __init__(self, bot):
            self.bot = bot
            self.my_task.start()

        def cog_unload(self):
            self.my_task.cancel()

        @tasks.loop(time=times)
        async def my_task(self):
            print("Minha tarefa está rodando!")

.. _ext_tasks_api:

Referência da API
-----------------

.. attributetable:: discord.ext.tasks.Loop

.. autoclass:: discord.ext.tasks.Loop()
:members:
:special-members: __call__
:exclude-members: after_loop, before_loop, error

.. automethod:: Loop.after_loop()
:decorator:

.. automethod:: Loop.before_loop()
:decorator:

.. automethod:: Loop.error()
:decorator:

.. autofunction:: discord.ext.tasks.loop
:decorator: