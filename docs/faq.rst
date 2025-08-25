Example code can be found in the `examples folder <https://github.com/Rapptz/discord.py/tree/master/examples>`_
in the repository.:orphan:

.. currentmodule:: discord
.. _faq:

Perguntas Frequentes
===========================

Esta é uma lista de Perguntas Frequentes sobre o uso do ``discord.py`` e seus módulos de extensão. Sinta-se à vontade para sugerir uma
nova pergunta ou enviar uma via pull request.

.. contents:: Perguntas
    :local:

Corrotinas
------------

Perguntas relacionadas a corrotinas e asyncio pertencem a esta seção.

O que é uma corrotina?
~~~~~~~~~~~~~~~~~~~~~~

Uma |coroutine_link|_ é uma função que deve ser chamada com ``await`` ou ``yield from``. Quando o Python encontra um ``await``, ele
interrompe a execução da função naquele ponto e trabalha em outras tarefas até voltar e finalizar o trabalho. 
Isso permite que seu programa execute múltiplas tarefas ao mesmo tempo sem usar threads ou multiprocessing complicado.

**Se você esquecer de usar await em uma corrotina, ela não será executada. Nunca se esqueça de await em uma corrotina.**

Onde posso usar ``await``\?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Você só pode usar ``await`` dentro de funções ``async def`` e em nenhum outro lugar.

O que significa "bloqueio"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Em programação assíncrona, uma chamada bloqueante é basicamente todas as partes da função que não são ``await``. 
Não se preocupe, pois nem todas as formas de bloqueio são ruins! Usar chamadas bloqueantes é inevitável, mas você deve garantir 
que não bloqueie funções excessivamente. Lembre-se, se você bloquear por muito tempo, seu bot irá travar, pois a execução 
da função não parou naquele ponto para fazer outras tarefas.

Se o logging estiver habilitado, esta biblioteca tentará avisar quando houver bloqueio com a mensagem:
``Heartbeat blocked for more than N seconds.``
Veja :ref:`logging_setup` para detalhes sobre como habilitar logging.

Uma fonte comum de bloqueio excessivo é algo como :func:`time.sleep`. Não faça isso. Use :func:`asyncio.sleep` 
em vez disso. Similar ao exemplo: ::

    # ruim
    time.sleep(10)

    # bom
    await asyncio.sleep(10)

Outra fonte comum de bloqueio excessivo é usar requisições HTTP com o famoso módulo :doc:`req:index`.
Enquanto :doc:`req:index` é um módulo incrível para programação não assíncrona, ele não é uma boa escolha para 
:mod:`asyncio` porque certas requisições podem bloquear o event loop por muito tempo. Em vez disso, use a biblioteca :doc:`aiohttp <aio:index>`, 
que já vem instalada junto com esta biblioteca.

Considere o seguinte exemplo: ::

    # ruim
    r = requests.get('http://aws.random.cat/meow')
    if r.status_code == 200:
        js = r.json()
        await channel.send(js['file'])

    # bom
    async with aiohttp.ClientSession() as session:
        async with session.get('http://aws.random.cat/meow') as r:
            if r.status == 200:
                js = await r.json()
                await channel.send(js['file'])

Geral
---------

Perguntas gerais sobre o uso da biblioteca pertencem a esta seção.

Onde posso encontrar exemplos de uso?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O código de exemplo pode ser encontrado na `pasta de exemplos <https://github.com/Rapptz/discord.py/tree/master/examples>`_ 
no repositório.

            data = io.BytesIO(await resp.read())
            await channel.send(file=discord.File(data, 'cool_image.png'))Como faço para definir o status "Jogando"?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O argumento de palavra-chave ``activity`` pode ser passado no construtor da :class:`Client` ou em :meth:`Client.change_presence`, 
dado um objeto :class:`Activity`.

O construtor pode ser usado para atividades estáticas, enquanto :meth:`Client.change_presence` pode ser usado para atualizar 
a atividade em tempo de execução.

.. warning::

    É altamente desaconselhado usar :meth:`Client.change_presence` ou chamadas de API em :func:`on_ready`, 
    pois este evento pode ser chamado várias vezes durante a execução, não apenas uma vez.

    Há uma grande chance de desconexão se as presenças forem alteradas logo após conectar.

O tipo de status (jogando, ouvindo, transmitindo, assistindo) pode ser definido usando o enum :class:`ActivityType`.
Para otimização de memória, algumas atividades são oferecidas em versões simplificadas:

- :class:`Game`
- :class:`Streaming`

Juntando essas informações, você teria o seguinte: ::

    client = discord.Client(activity=discord.Game(name='meu jogo'))

    # ou, para assistir:
    activity = discord.Activity(name='minha atividade', type=discord.ActivityType.watching)
    client = discord.Client(activity=activity)

Como envio uma mensagem para um canal específico?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Você deve buscar o canal diretamente e então chamar o método apropriado. Exemplo: ::

    channel = client.get_channel(12324234183172)
    await channel.send('olá')

Como envio uma DM?
~~~~~~~~~~~~~~~~~~

Obtenha o objeto :class:`User` ou :class:`Member` e chame :meth:`abc.Messageable.send`. Por exemplo: ::

    user = client.get_user(381870129706958858)
    await user.send('👀')

Se você está respondendo a um evento, como :func:`on_message`, você já tem o objeto :class:`User` via :attr:`Message.author`: ::

    await message.author.send('👋')

Como obtenho o ID de uma mensagem enviada?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

:meth:`abc.Messageable.send` retorna a :class:`Message` que foi enviada.
O ID de uma mensagem pode ser acessado via :attr:`Message.id`: ::

    message = await channel.send('hmm…')
    message_id = message.id

Como faço upload de uma imagem?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para enviar algo para o Discord, você deve usar o objeto :class:`File`.

Um :class:`File` aceita dois parâmetros, o objeto tipo arquivo (ou caminho do arquivo) e o nome do arquivo
para enviar ao Discord durante o upload.

Se você quiser enviar uma imagem é tão simples quanto: ::

    await channel.send(file=discord.File('meu_arquivo.png'))

Se você tiver um objeto tipo arquivo, pode fazer o seguinte: ::

    with open('meu_arquivo.png', 'rb') as fp:
        await channel.send(file=discord.File(fp, 'novo_nome.png'))

Para enviar múltiplos arquivos, você pode usar o argumento de palavra-chave ``files`` ao invés de ``file``\: ::

    meus_arquivos = [
        discord.File('resultado.zip'),
        discord.File('grafico_teaser.png'),
    ]
    await channel.send(files=meus_arquivos)

Se você quiser enviar algo a partir de uma URL, será necessário fazer uma requisição HTTP usando :doc:`aiohttp <aio:index>`
e então passar uma instância :class:`io.BytesIO` para :class:`File`, assim:

.. code-block:: python3

    import io
    import aiohttp

    async with aiohttp.ClientSession() as session:
        async with session.get(minha_url) as resp:
            if resp.status != 200:
                return await channel.send('Não foi possível baixar o arquivo...')
            data = io.BytesIO(await resp.read())
            await channel.send(file=discord.File(data, 'imagem_legenda.png'))


        # find a channel by name
        channel = discord.utils.get(guild.text_channels, name='cool-channel')Como faço para adicionar uma reação a uma mensagem?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Você usa o método :meth:`Message.add_reaction`.

Se você quiser usar emojis unicode, deve passar um ponto de código unicode válido em uma string. No seu código, você pode escrever isso de algumas maneiras diferentes:

- ``'👍'``
- ``'\U0001F44D'``
- ``'\N{THUMBS UP SIGN}'``

Exemplo rápido:

.. code-block:: python3

    emoji = '\N{THUMBS UP SIGN}'
    # ou '\U0001f44d' ou '👍'
    await message.add_reaction(emoji)

Caso queira usar emojis que vêm de uma mensagem, você já obtém seus pontos de código no conteúdo sem precisar
fazer nada de especial. Você **não pode** enviar abreviações do estilo ``':thumbsup:'``.

Para emojis personalizados, você deve passar uma instância de :class:`Emoji`. Você também pode passar uma string ``'<:nome:id>'``, mas se você
pode usar esse emoji, deve conseguir usar :meth:`Client.get_emoji` para obter um emoji via ID ou usar :func:`utils.find`/
:func:`utils.get` nas coleções :attr:`Client.emojis` ou :attr:`Guild.emojis`.

O nome e o ID de um emoji personalizado podem ser encontrados com o cliente prefixando ``:custom_emoji:`` com uma barra invertida.
Por exemplo, enviar a mensagem ``\:python3:`` com o cliente resultará em ``<:python3:232720527448342530>``.

Exemplo rápido:

.. code-block:: python3

    # se você já tem o ID
    emoji = client.get_emoji(310177266011340803)
    await message.add_reaction(emoji)

    # sem ID, faça uma busca
    emoji = discord.utils.get(guild.emojis, name='LUL')
    if emoji:
        await message.add_reaction(emoji)

    # se você tem o nome e ID de um emoji personalizado:
    emoji = '<:python3:232720527448342530>'
    await message.add_reaction(emoji)

Como passar uma coroutine para a função "after" do player?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O player de música da biblioteca roda em uma thread separada, portanto não executa dentro de uma coroutine.
Isso não significa que não seja possível chamar uma coroutine no parâmetro ``after``. Para isso, você deve passar uma função chamável
que encapsule alguns aspectos.

O primeiro cuidado que você deve ter é que chamar uma coroutine não é uma operação segura para threads. Como estamos
tecnicamente em outra thread, devemos ter cautela ao chamar operações seguras para threads para evitar bugs. Felizmente,
:mod:`asyncio` possui a função :func:`asyncio.run_coroutine_threadsafe`, que permite chamar
uma coroutine de outra thread.

No entanto, essa função retorna um :class:`~concurrent.futures.Future` e, para realmente chamá-la, precisamos obter seu resultado. 
Juntando tudo isso, podemos fazer o seguinte:

.. code-block:: python3

    def minha_after(error):
        coro = some_channel.send('A música terminou!')
        fut = asyncio.run_coroutine_threadsafe(coro, client.loop)
        try:
            fut.result()
        except:
            # ocorreu um erro ao enviar a mensagem
            pass

    voice.play(discord.FFmpegPCMAudio(url), after=minha_after)

Como executar algo em segundo plano?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`Veja o exemplo background_task.py. <https://github.com/Rapptz/discord.py/blob/master/examples/background_task.py>`_

Como obter um modelo específico?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Existem várias maneiras de fazer isso. Se você tiver o ID de um modelo específico, pode usar
uma das seguintes funções:

- :meth:`Client.get_channel`
- :meth:`Client.get_guild`
- :meth:`Client.get_user`
- :meth:`Client.get_emoji`
- :meth:`Guild.get_member`
- :meth:`Guild.get_channel`
- :meth:`Guild.get_role`

As seguintes usam uma requisição HTTP:

- :meth:`abc.Messageable.fetch_message`
- :meth:`Client.fetch_user`
- :meth:`Client.fetch_guilds`
- :meth:`Client.fetch_guild`
- :meth:`Guild.fetch_emoji`
- :meth:`Guild.fetch_emojis`
- :meth:`Guild.fetch_member`

Se as funções acima não ajudarem, então o uso de :func:`utils.find` ou :func:`utils.get` pode ser útil para encontrar
modelos específicos.

Exemplo rápido:

.. code-block:: python3

    # encontrar uma guilda pelo nome
    guild = discord.utils.get(client.guilds, name='Meu Servidor')

    # certifique-se de verificar se foi encontrada
    if guild is not None:
        # encontrar um canal pelo nome
        channel = discord.utils.get(guild.text_channels, name='canal-bacana')

    async def length(ctx):
        await ctx.send(f'Your message is {len(ctx.message.content)} characters long.')Como faço uma requisição web?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para fazer uma requisição, você deve usar uma biblioteca não bloqueante.
Esta biblioteca já usa e requer uma biblioteca de terceiros para requisições, :doc:`aiohttp <aio:index>`.

Exemplo rápido:

.. code-block:: python3

    async with aiohttp.ClientSession() as session:
        async with session.get('http://aws.random.cat/meow') as r:
            if r.status == 200:
                js = await r.json()

Veja a `documentação completa do aiohttp <http://aiohttp.readthedocs.io/en/stable/>`_ para mais informações.

.. _local_image:

Como usar um arquivo de imagem local em um embed?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O Discord trata de forma especial o upload de uma imagem como anexo e seu uso dentro de um embed, de modo que não
seja exibida separadamente, mas sim na miniatura, imagem, rodapé ou ícone de autor do embed.

Para isso, faça o upload da imagem normalmente com :meth:`abc.Messageable.send`,
e defina o URL da imagem do embed como ``attachment://image.png``,
onde ``image.png`` é o nome do arquivo que você enviará.

Exemplo rápido:

.. code-block:: python3

    file = discord.File("path/to/my/image.png", filename="image.png")
    embed = discord.Embed()
    embed.set_image(url="attachment://image.png")
    await channel.send(file=file, embed=embed)

Existe um evento para entradas do registro de auditoria sendo criadas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este evento agora está disponível na biblioteca e no Discord a partir da versão 2.2. Ele pode ser encontrado em :func:`on_audit_log_entry_create`.

Extensão de Comandos
-------------------

Perguntas sobre ``discord.ext.commands`` pertencem a esta seção.

Por que ``on_message`` faz meus comandos pararem de funcionar?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sobrescrever o ``on_message`` padrão impede que quaisquer comandos adicionais sejam executados. Para corrigir isso, adicione uma
linha ``bot.process_commands(message)`` ao final do seu ``on_message``. Por exemplo: ::

    @bot.event
    async def on_message(message):
        # faça algo extra aqui

        await bot.process_commands(message)

Alternativamente, você pode colocar sua lógica do ``on_message`` em um **listener**. Nesse caso, não
chame manualmente ``bot.process_commands()``. Isso também permite executar várias tarefas de forma assíncrona em resposta
a uma mensagem. Exemplo::

    @bot.listen('on_message')
    async def qualquer_nome_que_quiser(message):
        # faça algo aqui
        # não processe comandos aqui

Por que meus argumentos precisam de aspas?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Em um comando simples definido como:

.. code-block:: python3

    @bot.command()
    async def echo(ctx, message: str):
        await ctx.send(message)

Chamá-lo via ``?echo a b c`` só pegará o primeiro argumento e ignorará os demais. Para corrigir isso, você deve ou chamar
via ``?echo "a b c"`` ou alterar a assinatura para ter o comportamento "consume rest". Exemplo:

.. code-block:: python3

    @bot.command()
    async def echo(ctx, *, message: str):
        await ctx.send(message)

Isso permitirá usar ``?echo a b c`` sem precisar das aspas.

Como obtenho a ``message`` original?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O :class:`~ext.commands.Context` contém um atributo, :attr:`~.Context.message`, para obter a mensagem original.

Exemplo:

.. code-block:: python3

    @bot.command()
    async def length(ctx):
        await ctx.send(f'Sua mensagem tem {len(ctx.message.content)} caracteres.')

        tree.copy_global_to(guild=discord.Object(123456789012345678))
Como faço um subcomando?
~~~~~~~~~~~~~~~~~~~~~~~~

Use o decorador :func:`~ext.commands.group`. Isso transformará a função de callback em um :class:`~ext.commands.Group`, permitindo adicionar comandos ao grupo que funcionarão como "subcomandos". Esses grupos podem ser aninhados arbitrariamente também.

Exemplo:

.. code-block:: python3

    @bot.group()
    async def git(ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send('Comando git inválido...')

    @git.command()
    async def push(ctx, remote: str, branch: str):
        await ctx.send(f'Fazendo push para {remote} {branch}')

Isso poderia ser usado como ``?git push origin master``.

Views e Modals
-----------------

Perguntas sobre :class:`discord.ui.View`, :class:`discord.ui.Modal` e seus componentes, como botões, menus de seleção, etc.

Como posso desativar todos os itens após o tempo esgotar?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Isso requer três passos:

1. Anexar uma mensagem ao :class:`~discord.ui.View` usando o tipo de retorno de :meth:`~abc.Messageable.send` ou recuperando-a via :attr:`InteractionCallbackResponse.resource`.
2. Dentro de :meth:`~ui.View.on_timeout`, percorra todos os itens da view e marque-os como desativados.
3. Edite a mensagem recuperada no passo 1 com a view modificada.

Juntando tudo, podemos fazer isso em um comando de texto:

.. code-block:: python3

    class MyView(discord.ui.View):
        async def on_timeout(self) -> None:
            # Passo 2
            for item in self.children:
                item.disabled = True

            # Passo 3
            await self.message.edit(view=self)

        @discord.ui.button(label='Exemplo')
        async def example_button(self, interaction: discord.Interaction, button: discord.ui.Button):
            await interaction.response.send_message('Olá!', ephemeral=True)

    @bot.command()
    async def timeout_example(ctx):
        """Exemplo de desativação de botões quando o tempo esgota"""
        view = MyView()
        # Passo 1
        view.message = await ctx.send('Clique em mim!', view=view)

Comandos de aplicação, quando você responde com :meth:`InteractionResponse.send_message`, retornam uma instância de :class:`InteractionCallbackResponse`, que contém a mensagem enviada. Esta é a mensagem que você deve anexar à view.

Juntando tudo, usando a definição de view anterior:

.. code-block:: python3

    @tree.command()
    async def more_timeout_example(interaction):
        """Outro exemplo de desativação de botões quando o tempo esgota"""
        view = MyView()
        callback = await interaction.response.send_message('Clique em mim!', view=view)

        # Passo 1
        resource = callback.resource
        # garantindo que é uma mensagem de resposta à interação
        if isinstance(resource, discord.InteractionMessage):
            view.message = resource


Comandos de Aplicação
--------------------

Perguntas sobre os novos comandos de aplicação do Discord, conhecidos como "slash commands" ou "context menu commands".

Os comandos do meu bot não estão aparecendo!
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Você fez :meth:`~.CommandTree.sync` no seu comando? Comandos precisam ser sincronizados antes de aparecer.
2. Você convidou o bot com as permissões corretas? Bots precisam ser convidados com o escopo ``applications.commands`` além do escopo ``bot``. Por exemplo, use a URL:
   ``https://discord.com/oauth2/authorize?client_id=<client id>&scope=applications.commands+bot``.
   Alternativamente, se usar :func:`utils.oauth_url`, você pode chamar a função assim:
   ``oauth_url(<outras opções>, scopes=("bot", "applications.commands"))``.

Como restringir um comando a uma guilda específica?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para restringir um comando de aplicação a uma ou mais guildas, você deve registrá-lo como um **comando de guilda** em vez de global. Comandos de guilda só estarão disponíveis nas guildas especificadas.

A forma mais direta é usar o decorador :meth:`~app_commands.guilds` no seu comando ou GroupCog.

``123456789012345678`` deve ser substituído pelo ID real da guilda que deseja restringir.

.. code-block:: python3

    @app_commands.command()  # ou @tree.command()
    @app_commands.guilds(123456789012345678)  # ou @app_commands.guilds(discord.Object(123456789012345678))
    async def ping(interaction: Interaction):
        await interaction.response.send_message("Pong!")

    # ou GroupCog (aplica-se a todos os subcomandos):

    @app_commands.guilds(123456789012345678)
    class MyGroup(commands.GroupCog):
        @app_commands.command()
        async def pong(self, interaction: Interaction):
            await interaction.response.send_message("Ping!")

Depois disso, você deve :meth:`~app_commands.CommandTree.sync` a árvore de comandos para cada guilda:

.. code-block:: python3

    await tree.sync(guild=discord.Object(123456789012345678))

Outros métodos para restringir comandos a guildas específicas incluem:

- Usar o argumento ``guild`` ou ``guilds`` no decorador :meth:`~app_commands.CommandTree.command`:

    .. code-block:: python3

        @tree.command(guild=discord.Object(123456789012345678))
        async def ping(interaction: Interaction):
            await interaction.response.send_message("Pong!")

- Adicionar comandos com :meth:`~app_commands.CommandTree.add_command` especificando ``guild`` ou ``guilds``:

    .. code-block:: python3

        @app_commands.command()
        async def ping(interaction: Interaction):
            await interaction.response.send_message("Pong!")

        tree.add_command(ping, guild=discord.Object(123456789012345678))

    .. warning::

        Não combine este método com o decorador :meth:`~app_commands.CommandTree.command`,
        pois causará comandos duplicados.

- Usar ``guild`` ou ``guilds`` em :meth:`~ext.commands.Bot.add_cog`:

    Isso é principalmente para :class:`~ext.commands.GroupCog`, mas também funciona para cogs com comandos de aplicação.
    Nota: Isso não funciona com comandos híbridos de aplicação (:issue:`9366`).

    .. code-block:: python3

        class MyCog(commands.Cog):
            @app_commands.command()
            async def ping(self, interaction: Interaction):
                await interaction.response.send_message("Pong!")

        async def setup(bot: commands.Bot) -> None:
            await bot.add_cog(MyCog(...), guild=discord.Object(123456789012345678))

- Usar :meth:`~app_commands.CommandTree.copy_global_to`:

    Isso copia todos os comandos globais para uma guilda específica. Principalmente usado para desenvolvimento.

    .. code-block:: python3

        tree.copy_global_to(guild=discord.Object(123456789012345678))