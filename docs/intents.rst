:orphan:

.. currentmodule:: discord
.. versionadded:: 1.5
.. _intents_primer:

Um Guia de Intents do Gateway
=============================

Na versão 1.5 foi introduzida a classe :class:`Intents`. Isso representa uma mudança radical na forma como bots são escritos. Um intent basicamente permite que um bot se inscreva em grupos específicos de eventos. Os eventos que correspondem a cada intent estão documentados nos atributos individuais da documentação de :class:`Intents`.

Esses intents são passados para o construtor de :class:`Client` ou suas subclasses (:class:`AutoShardedClient`, :class:`~.AutoShardedBot`, :class:`~.Bot`) através do argumento ``intents``.

Quais intents são necessários?
------------------------------

Os intents necessários para o seu bot só podem ser determinados por você. Cada atributo da classe :class:`Intents` documenta a quais :ref:`eventos <discord-api-events>` ele corresponde e que tipo de cache ele habilita.

Por exemplo, se você quiser um bot que funcione sem eventos excessivos como presenças ou digitação, podemos fazer o seguinte:

.. code-block:: python3
   :emphasize-lines: 7,9,10

    import discord
    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False

    # Em outro lugar:
    # client = discord.Client(intents=intents)
    # ou
    # from discord.ext import commands
    # bot = commands.Bot(command_prefix='!', intents=intents)

Observe que isso não habilita :attr:`Intents.members`, pois é um intent privilegiado.

Outro exemplo mostrando um bot que só lida com mensagens e informações do servidor:

.. code-block:: python3
   :emphasize-lines: 7,9,10

    import discord
    intents = discord.Intents(messages=True, guilds=True)
    # Se você também quiser eventos de reação, habilite o seguinte:
    # intents.reactions = True

    # Em outro lugar:
    # client = discord.Client(intents=intents)
    # ou
    # from discord.ext import commands
    # bot = commands.Bot(command_prefix='!', intents=intents)

.. _privileged_intents:

Intents Privilegiados
---------------------

Com a mudança na API exigindo que autores de bots especifiquem intents, alguns intents foram restringidos e requerem etapas manuais adicionais. Esses intents são chamados de **intents privilegiados**.

Um intent privilegiado é aquele que exige que você acesse o portal de desenvolvedores e o habilite manualmente. Para habilitar intents privilegiados, faça o seguinte:

1. Certifique-se de que está logado no `site do Discord <https://discord.com>`_.
2. Navegue até a `página de aplicações <https://discord.com/developers/applications>`_.
3. Clique no bot para o qual deseja habilitar intents privilegiados.
4. Vá para a aba do bot no lado esquerdo da tela.

    .. image:: /images/discord_bot_tab.png
        :alt: A aba do bot na página de aplicações.

5. Role até a seção "Privileged Gateway Intents" e habilite os intents que você deseja.

    .. image:: /images/discord_privileged_intents.png
        :alt: O seletor de intents privilegiados do gateway.

.. warning::

    Habilitar intents privilegiados quando seu bot está em mais de 100 servidores exige passar pelo processo de `verificação de bot (Inglês)<https://support-dev.discord.com/hc/pt-br/articles/23926564536471-How-Do-I-Get-My-App-Verified>`_. Se o seu bot já estiver verificado e você quiser habilitar um intent privilegiado, você deve entrar em contato com o `suporte do Discord <https://dis.gd/contact>`_.

.. note::

    Mesmo que você habilite intents pelo portal de desenvolvedores, ainda será necessário habilitá-los via código também.

Preciso de intents privilegiados?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este é um checklist rápido para verificar se você precisa de intents privilegiados específicos.

.. _need_presence_intent:

Intent de Presença
+++++++++++++++++

- Se você usa :attr:`Member.status` para acompanhar o status dos membros.
- Se você usa :attr:`Member.activity` ou :attr:`Member.activities` para verificar atividades dos membros.

.. _need_members_intent:

Intent de Membros
+++++++++++++++++

- Se você acompanha entradas ou saídas de membros, correspondendo aos eventos :func:`on_member_join` e :func:`on_member_remove`.
- Se você deseja acompanhar atualizações de membros, como alterações de apelido ou funções.
- Se você deseja acompanhar atualizações de usuário, como nomes, avatares, discriminadores, etc.
- Se você deseja solicitar a lista de membros do servidor via :meth:`Guild.chunk` ou :meth:`Guild.fetch_members`.
- Se você deseja um cache de membros preciso via :attr:`Guild.members`.

.. _need_message_content_intent:

Conteúdo de Mensagem
++++++++++++++++++++

- Se você usa :attr:`Message.content` para verificar o conteúdo de mensagens.
- Se você usa :attr:`Message.attachments` para verificar anexos.
- Se você usa :attr:`Message.embeds` para verificar embeds.
- Se você usa :attr:`Message.components` para verificar componentes de mensagens.
- Se você usa a extensão de comandos com prefixo que não mencione.

.. _intents_member_cache:

Cache de Membros
----------------

Junto com intents, o Discord agora restringe ainda mais a capacidade de cache de membros e espera que autores de bots armazenem apenas o necessário. Para manter um cache corretamente, o intent :attr:`Intents.members` é necessário para rastrear os membros que saíram e removê-los apropriadamente.

Para ajudar com cache de membros quando não precisamos armazená-los, a biblioteca possui a flag :class:`MemberCacheFlags`. A documentação da classe detalha as políticas possíveis.

Algumas situações não exigem cache de membros, já que o Discord fornece informações completas se possível. Por exemplo:

- :func:`on_message` terá :attr:`Message.author` como membro mesmo se o cache estiver desativado.
- :func:`on_voice_state_update` terá o parâmetro ``member`` como membro mesmo se o cache estiver desativado.
- :func:`on_reaction_add` terá o parâmetro ``user`` como membro quando em um servidor, mesmo com cache desativado.
- :func:`on_raw_reaction_add` terá :attr:`RawReactionActionEvent.member` como membro quando em um servidor, mesmo com cache desativado.
- Eventos de adição de reação não contêm informações adicionais em mensagens diretas. Isso é uma limitação do Discord.
- Eventos de remoção de reação não têm informações de membros. Isso é uma limitação do Discord.

Outros eventos que recebem um :class:`Member` exigirão o uso do cache. Para precisão absoluta, recomenda-se habilitar :attr:`Intents.members`.

.. _retrieving_members:

Recuperando Membros
--------------------

Se o cache estiver desativado ou você desativar chunking de servidores na inicialização, ainda podemos precisar carregar membros. A biblioteca oferece algumas formas:

- :meth:`Guild.query_members`
    - Usado para consultar membros por prefixo de apelido ou nome.
    - Também pode ser usado para consultar membros por ID de usuário.
    - Usa o gateway e não HTTP.
- :meth:`Guild.chunk`
    - Pode ser usado para buscar a lista completa de membros via gateway.
- :meth:`Guild.fetch_member`
    - Usado para buscar um membro por ID via API HTTP.
- :meth:`Guild.fetch_members`
    - Usado para buscar um grande número de membros via API HTTP.

O gateway possui um limite de 120 requisições a cada 60 segundos.

Solução de Problemas
--------------------

Alguns problemas comuns relacionados à mudança obrigatória de intents.

Cadê meus membros?
~~~~~~~~~~~~~~~~~~

Devido a uma :ref:`mudança na API <intents_member_cache>`, o Discord agora força os desenvolvedores que desejam cache de membros a habilitarem explicitamente. Para recuperar os membros, você deve habilitar explicitamente o :ref:`intent privilegiado de membros <privileged_intents>` e definir :attr:`Intents.members` como True.

Por exemplo:

.. code-block:: python3
   :emphasize-lines: 3,6,8,9

    import discord
    intents = discord.Intents.default()
    intents.members = True

    # Em outro lugar:
    # client = discord.Client(intents=intents)
    # ou
    # from discord.ext import commands
    # bot = commands.Bot(command_prefix='!', intents=intents)

Por que ``on_ready`` demora tanto para ser acionado?
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Como parte da mudança da API sobre intents, o Discord também alterou como membros são carregados no início. Originalmente, a biblioteca podia solicitar 75 servidores de uma vez e buscar membros apenas nos servidores com :attr:`Guild.large` definido como ``True``. Com a mudança de intents, o Discord exige que apenas 1 servidor seja solicitado por vez. Isso causa uma desaceleração de 75x, ainda maior pois *todos* os servidores, não apenas os grandes, estão sendo solicitados.

Algumas soluções para corrigir isso:

A primeira solução é solicitar o intent privilegiado de presenças junto com o intent privilegiado de membros e habilitar ambos. Isso permite que a lista inicial contenha membros online, como no gateway antigo. Note que ainda estamos limitados a 1 servidor por solicitação, mas o número de servidores solicitados é significativamente reduzido.

A segunda solução é desabilitar chunking de membros definindo ``chunk_guilds_at_startup`` como ``False`` ao construir o cliente. Quando for necessário, você pode usar as várias técnicas para :ref:`recuperar membros <retrieving_members>`.

Para ilustrar a desaceleração causada pela mudança da API, considere um bot em 840 servidores, dos quais 95 são "grandes" (mais de 250 membros).

No sistema original, isso resultaria em 2 requisições para buscar a lista de membros (75 servidores, 20 servidores), levando cerca de 60 segundos. Com :attr:`Intents.members` mas não :attr:`Intents.presences`, isso exige 840 requisições, com limite de 120 requisições por 60 segundos, totalizando cerca de 7 minutos para buscar todos os membros. Com ambos :attr:`Intents.members` e :attr:`Intents.presences`, o comportamento antigo é praticamente mantido, já que só precisamos solicitar os 95 servidores grandes, próximo ao limite original.

Infelizmente, devido a esta exigência do Discord, não há nada que a biblioteca possa fazer para mitigar isso.

Se você realmente não gosta da direção que o Discord está tomando com a API, você pode contatá-los via `suporte <https://dis.gd/contact>`_.