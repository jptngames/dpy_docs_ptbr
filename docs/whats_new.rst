.. currentmodule:: discord

.. |commands| replace:: [:ref:`ext.commands <discord_ext_commands>`]
.. |tasks| replace:: [:ref:`ext.tasks <discord_ext_tasks>`]

.. _whats_new:

Changelog
============

Esta página mantém um histórico detalhado e legível por humanos das novidades e mudanças
em versões específicas.

.. _vp2p6p1:

v2.6.1
-------

Bug Fixes
~~~~~~~~~~

- Fix :attr:`ui.Section.children` and :attr:`ui.Section.accessory` having ``None`` as the :attr:`Item.parent` (:issue:`10269`)
- Fix error when using a :class:`ui.DynamicItem` inside an :class:`ui.Section`
- Fix :class:`ui.DynamicItem` not working when set as an :attr:`ui.Section.acessory` (:issue:`10271`)
- Fix :attr:`ui.LayoutView.total_children_count` being inaccurate when adding nested items
- Fix crash when accessing :attr:`AuditLogEntry.category` for unknown audit log actions
- |tasks| Add logging statement when a handled exception occurs (:issue:`10276`)

.. _vp2p6p0:

v2.6.0
--------

Novos Recursos
~~~~~~~~~~~~~~

- Adiciona suporte para os "Components v2" do Discord (:issue:`10166`)
- Um novo :class:`ui.LayoutView` é usado para utilizar esses componentes, o que exige layout manual.
- A compatibilidade retroativa é mantida com tudo, incluindo :class:`ui.DynamicItem`.
- Foram adicionados os seguintes novos componentes e seus equivalentes na UI:
- :class:`SectionComponent` corresponde a :class:`ui.Section`
- :class:`TextDisplay` corresponde a :class:`ui.TextDisplay`
- :class:`ThumbnailComponent` corresponde a :class:`ui.Thumbnail`
- :class:`MediaGalleryComponent` corresponde a :class:`ui.MediaGallery`
- :class:`FileComponent` corresponde a :class:`ui.File`
- :class:`SeparatorComponent` corresponde a :class:`ui.Separator`
- :class:`Container` corresponde a :class:`ui.Container`
- :class:`ActionRow` corresponde a :class:`ui.ActionRow`

- Adiciona suporte à primeira fase de melhorias do :class:`discord.ui.Modal`.
- Agora é possível usar :class:`discord.ui.Select` dentro de modals.
- Também permite :class:`discord.ui.Label` para maior controle dos formulários dentro de modals.
- Isso torna o :attr:`discord.ui.TextInput.label` opcional e o deprecia em favor de :class:`discord.ui.Label`.
- No momento desta escrita, essa atualização do Discord ainda não está disponível para usuários.

- Adiciona suporte para guild tags (também conhecidas como guilds primárias) (:issue:`10211`)
- Isso é feito por meio da classe :class:`PrimaryGuild`.
- Você pode recuperar usando :attr:`Member.primary_guild`.

- Adiciona suporte ao novo endpoint de pins (:issue:`10205`)
- Isso transforma :meth:`abc.Messageable.pins` em um iterador assíncrono.
- O comportamento antigo usando ``await`` ainda é suportado, mas está obsoleto.

- Adiciona suporte para guild onboarding (:issue:`10226`, :issue:`9260`)
- Adiciona suporte para :attr:`MemberFlags.automod_quarantined_guild_tag` (:issue:`10236`)
- Adiciona suporte para novas cores de cargo em gradiente e holográficas (:issue:`10214`, :issue:`10225`)
- Adiciona o atributo :attr:`Locale.language_code` (:issue:`10222`)
- Adiciona suporte para convites de convidados (:issue:`10220`)
- Adiciona :attr:`File.uri` para obter a URI ``attachment://<filename>`` de um arquivo
    - Adiciona suporte para respostas de :meth:`InteractionResponse.launch_activity` (:issue:`10193`)
    - Adiciona capacidade de criar um canal de fórum somente de mídia via parâmetro ``media`` em :meth:`Guild.create_forum` (:issue:`10170`)
    - Adiciona :attr:`Interaction.filesize_limit` (:issue:`10159`)
    - Adiciona novas cores dos temas recentes do Discord (:issue:`10152`)
    - Atualiza os métodos antigos :meth:`Colour.dark_theme`, :meth:`Colour.light_theme`, :meth:`Colour.light_embed` e :meth:`Colour.dark_embed`
    - Adiciona :meth:`Colour.ash_theme`, :meth:`Colour.ash_embed`, :meth:`Colour.onyx_theme` e :meth:`Colour.onyx_embed`
    
    - Adiciona suporte para novos campos em :class:`Activity` (:issue:`10227`)
    - Adiciona o novo enum :class:`StatusDisplayType`
    
    - Adiciona método de classe :meth:`Permissions.apps` (:issue:`10147`)
    - Adiciona mais atributos em :class:`app_commands.AppCommandThread` e :class:`app_commands.AppCommandChannel` (:issue:`10180`, :issue:`10252`)
    
    Correções de Bugs
    ~~~~~~~~~~~~~~~~~~
    
    - Corrige decoradores de instalação de contexto para restringir comandos explicitamente
    - Corrige erro ao enviar views não interativas via webhooks parciais (:issue:`10235`)
    - Corrige problemas de conexão de voz e atualiza a versão de voz para 8 (:issue:`10210`)
    - Corrige cálculo de chaves de limite de taxa com hash (:issue:`10215`)
    - Corrige :attr:`Thread.applied_tags` vazio para canais de mídia (:issue:`10178`)
    - Corrige :meth:`Embed.to_dict` para classes Embed herdadas de usuário (:issue:`10173`)
    - Corrige possíveis buckets de limite de taxa presos em certas circunstâncias (:issue:`10160`)
    - Corrige ``__bool__`` incorreto para :class:`Embed` (:issue:`10154`)
    - Corrige log de auditoria ``automod_rule_trigger_type`` ausente em extras (:issue:`10244`)
    - Transforma corretamente canais de mídia em comandos de app (:issue:`10177`)
    - |commands| Corrige certos conversores que não funcionavam com type hints ``Optional`` em hybrids (:issue:`10239`, :issue:`10245`)
    
    Miscelânea
    ~~~~~~~~~~~~
    
    - Ignora ``GUILD_MEMBER_ADD`` se o membro já estiver em cache (:issue:`10238`)
    - Deprecia vários métodos relacionados à criação de guilds (:issue:`10164`, :issue:`10246`)
    - Deprecia o parâmetro ``with_expiration`` em :meth:`Client.fetch_invite` (:issue:`10259`)
    - Permite criar canais de voz/palco NSFW (:issue:`10200`)
    - :class:`Invite` agora é retornado ao usar :meth:`Invite.delete` ou :meth:`Client.delete_invite` (:issue:`10181`)
    - Copia opções de Select ao criar classes View (:issue:`10143`)
    - Atualiza a versão mínima da dependência PyNaCl (:issue:`10127`)

.. _vp2p5p2:

v2.5.2
-------

Correções de Bugs
~~~~~~~~~~~~~~~~

- Corrige problema de serialização ao enviar embeds (:issue:`10126`)

.. _vp2p5p1:

v2.5.1
-------

Correções de Bugs
~~~~~~~~~~~~~~~~

- Corrige :attr:`InteractionCallbackResponse.resource` com estado incorreto (:issue:`10107`)
- Cria :class:`ScheduledEvent` em cache miss para :func:`on_scheduled_event_delete` (:issue:`10113`)
- Adiciona valores padrão na criação de :class:`Message` prevenindo alguns crashes (:issue:`10115`)
- Corrige :meth:`Attachment.is_spoiler` e :meth:`Attachment.is_voice_message` estando incorretos (:issue:`10122`)


.. _vp2p5p0:

v2.5.0
-------

Novos Recursos
~~~~~~~~~~~~~~

- Suporte para encaminhamento de mensagens (:issue:`9950`)
    - Adiciona :class:`MessageReferenceType`
    - Adiciona :class:`MessageSnapshot`
    - Adiciona parâmetro ``type`` em :class:`MessageReference`, :meth:`MessageReference.from_message` e :meth:`PartialMessage.to_reference`
    - Adiciona :meth:`PartialMessage.forward`

- Suporte para assinaturas SKU (:issue:`9930`)
    - Adiciona novos eventos :func:`on_subscription_create`, :func:`on_subscription_update` e :func:`on_subscription_delete`
    - Adiciona :class:`SubscriptionStatus` enum
    - Adiciona :class:`Subscription` model
    - Adiciona :meth:`SKU.fetch_subscription` e :meth:`SKU.subscriptions`

- Suporte para emojis de aplicativo (:issue:`9891`)
    - Adiciona :meth:`Client.create_application_emoji`
    - Adiciona :meth:`Client.fetch_application_emoji`
    - Adiciona :meth:`Client.fetch_application_emojis`
    - Adiciona :meth:`Emoji.is_application_owned`

- Suporte para Soundboard e efeitos de VC (:issue:`9349`)
    - Adiciona :class:`BaseSoundboardSound`, :class:`SoundboardDefaultSound`, :class:`SoundboardSound`
    - Adiciona :class:`VoiceChannelEffect`
    - Adiciona :class:`VoiceChannelEffectAnimation`
    - Adiciona :class:`VoiceChannelEffectAnimationType`
    - Adiciona :class:`VoiceChannelSoundEffect`
    - Adiciona :meth:`VoiceChannel.send_sound`
    - Adiciona novas ações de audit log: :attr:`AuditLogAction.soundboard_sound_create`, :attr:`AuditLogAction.soundboard_sound_update`, :attr:`AuditLogAction.soundboard_sound_delete`
    - Adiciona :attr:`Intents.expressions` e aliases :attr:`Intents.emojis` e :attr:`Intents.emojis_and_stickers`
    - Novos eventos: :func:`on_soundboard_sound_create`, :func:`on_soundboard_sound_update`, :func:`on_soundboard_sound_delete`, :func:`on_voice_channel_effect`
    - Métodos/propriedades para lidar com soundboards:
        - :attr:`Client.soundboard_sounds`
        - :attr:`Guild.soundboard_sounds`
        - :meth:`Client.get_soundboard_sound`
        - :meth:`Guild.get_soundboard_sound`
        - :meth:`Client.fetch_soundboard_default_sounds`
        - :meth:`Guild.fetch_soundboard_sound`
        - :meth:`Guild.fetch_soundboard_sounds`
        - :meth:`Guild.create_soundboard_sound`

- Suporte para respostas de interação ao enviar respostas (:issue:`9957`)
    - Métodos de :class:`InteractionResponse` agora retornam :class:`InteractionCallbackResponse`
    - Dependendo do tipo de resposta, :attr:`InteractionCallbackResponse.resource` será diferente

- Adiciona :attr:`PartialWebhookChannel.mention` (:issue:`10101`)
- Suporte para envio de views sem estado para :class:`SyncWebhook` ou webhooks sem estado (:issue:`10089`)
- Interface mais completa para :meth:`Role.move` (:issue:`10100`)
- Suporte para :class:`EmbedFlags` via :attr:`Embed.flags` (:issue:`10085`)
- Novas flags para :class:`AttachmentFlags` (:issue:`10085`)
- Evento :func:`on_raw_presence_update` que não depende do cache (:issue:`10048`)
    - Requer ``enable_raw_presences`` em :class:`Client`.
- Adiciona :attr:`ForumChannel.members` (:issue:`10034`)
- Parâmetro ``exclude_deleted`` em :meth:`Client.entitlements` (:issue:`10027`)
- :meth:`Client.fetch_guild_preview` (:issue:`9986`)
- :meth:`AutoShardedClient.fetch_session_start_limits` (:issue:`10007`)
- :attr:`PartialMessageable.mention` (:issue:`9988`)
- Adiciona comando alvo a :class:`MessageInteractionMetadata` (:issue:`10004`)
    - :attr:`MessageInteractionMetadata.target_user`
    - :attr:`MessageInteractionMetadata.target_message_id`
    - :attr:`MessageInteractionMetadata.target_message`
- Adiciona flag :attr:`Message.forward` (:issue:`9978`)
- Suporte para mensagens de notificação de compra (:issue:`9906`)
    - Adiciona tipo :attr:`MessageType.purchase_notification`
    - Adiciona modelos :class:`GuildProductPurchase` e :class:`PurchaseNotification`
    - Adiciona :attr:`Message.purchase_notification`
- Parâmetro ``category`` em :meth:`.abc.GuildChannel.clone` (:issue:`9941`)
- Suporte para mensagem de chamada (:issue:`9911`)
    - Adiciona modelos :class:`CallMessage`
    - Adiciona :attr:`Message.call`
- Parsing completo de mensagem em evento de edição (:issue:`10035`)
    - Adiciona :attr:`RawMessageUpdateEvent.message`
- Suporte para configuração de integração de tipo (:issue:`9818`)
    - Adiciona :class:`IntegrationTypeConfig`
    - Obtido via :attr:`AppInfo.guild_integration_config` e :attr:`AppInfo.user_integration_config`
    - Editável via :meth:`AppInfo.edit`
- Permite passar ``None`` em ``scopes`` no :func:`utils.oauth_url` (:issue:`10078`)
- Suporte para mensagens do tipo :attr:`MessageType.poll_result` (:issue:`9905`)
- Novos :class:`MessageFlags`
- :meth:`Member.fetch_voice` (:issue:`9908`)
- :attr:`Guild.dm_spam_detected_at` e :meth:`Guild.is_dm_spam_detected` (:issue:`9808`)
- :meth:`Client.fetch_premium_sticker_pack` (:issue:`9909`)
- :attr:`Member.guild_banner` e :attr:`Member.display_banner`
- Restaura parâmetro ``connector`` removido na v2.0 (:issue:`9900`)
- |commands| Adiciona :class:`~discord.ext.commands.SoundboardSoundConverter` (:issue:`9973`)


.. _vp2p4p0:

v2.4.0
-------

Novos Recursos
~~~~~~~~~~~~~~

- Adiciona suporte para contextos permitidos em comandos de aplicativo (:issue:`9760`).
    - Um "contexto permitido" é o local onde um comando de aplicativo pode ser usado.
    - Isso é uma mudança interna para decorators como :func:`app_commands.guild_only` e :func:`app_commands.dm_only`.
    - Adiciona :func:`app_commands.private_channel_only`.
    - Adiciona :func:`app_commands.allowed_contexts`.
    - Adiciona :class:`app_commands.AppCommandContext`.
    - Adiciona :attr:`app_commands.Command.allowed_contexts`.
    - Adiciona :attr:`app_commands.AppCommand.allowed_contexts`.
    - Adiciona :attr:`app_commands.ContextMenu.allowed_contexts`.

- Adiciona suporte para aplicativos instaláveis pelo usuário (:issue:`9760`).
    - Adiciona :attr:`app_commands.Command.allowed_installs`.
    - Adiciona :attr:`app_commands.AppCommand.allowed_installs`.
    - Adiciona :attr:`app_commands.ContextMenu.allowed_installs`.
    - Adiciona :func:`app_commands.allowed_installs`.
    - Adiciona :func:`app_commands.guild_install`.
    - Adiciona :func:`app_commands.user_install`.
    - Adiciona :class:`app_commands.AppInstallationType`.
    - Adiciona :attr:`Interaction.context`.
    - Adiciona :meth:`Interaction.is_guild_integration`.
    - Adiciona :meth:`Interaction.is_user_integration`.

- Adiciona suporte para enquetes (:issue:`9759`).
    - Enquetes podem ser criadas usando :class:`Poll` e o parâmetro apenas-por-palavra-chave ``poll`` em diversos métodos de envio de mensagem.
    - Adiciona :class:`PollAnswer` e :class:`PollMedia`.
    - Adiciona intents :attr:`Intents.polls`, :attr:`Intents.guild_polls` e :attr:`Intents.dm_polls`.
    - Adiciona :meth:`Message.end_poll` para encerrar enquetes.
    - Adiciona novos eventos: :func:`on_poll_vote_add`, :func:`on_poll_vote_remove`, :func:`on_raw_poll_vote_add`, :func:`on_raw_poll_vote_remove`.

- Reescrita completa do sistema de voz para corrigir diversos bugs (:issue:`9525`, :issue:`9528`, :issue:`9536`, :issue:`9572`, :issue:`9576`, :issue:`9596`, :issue:`9683`, :issue:`9699`, :issue:`9772`, etc.)
- Adiciona :attr:`DMChannel.recipients` para obter todos os destinatários de um canal DM (:issue:`9760`).
- Adiciona suporte para :attr:`RawReactionActionEvent.message_author_id`.
- Adiciona suporte para :attr:`AuditLogAction.creator_monetization_request_created` e :attr:`AuditLogAction.creator_monetization_terms_accepted`.
- Adiciona suporte para :class:`AttachmentFlags`, acessível via :attr:`Attachment.flags` (:issue:`9486`).
- Adiciona suporte para :class:`RoleFlags`, acessível via :attr:`Role.flags` (:issue:`9485`).
- Adiciona suporte para :attr:`ChannelType.media`, acessível via :meth:`ForumChannel.is_media`.
- Adiciona várias novas permissões (:issue:`9501`, :issue:`9762`, :issue:`9759`, :issue:`9857`)
    - Adiciona :meth:`Permissions.events`.
    - Adiciona :attr:`Permissions.create_events`.
    - Adiciona :attr:`Permissions.view_creator_monetization_analytics`.
    - Adiciona :attr:`Permissions.send_polls`.
    - Adiciona :attr:`Permissions.create_polls`.
    - Adiciona :attr:`Permissions.use_external_apps`.

- Atalho para :attr:`CategoryChannel.forums`.
- Opções de encoder para :meth:`VoiceClient.play` (:issue:`9527`).
- Suporte para cargos de membros de equipe.
    - Adiciona :class:`TeamMemberRole`.
    - Adiciona :attr:`TeamMember.role`.
    - Atualiza :attr:`Bot.owner_ids <.ext.commands.Bot.owner_ids>` para considerar cargos de equipe. Donos ou desenvolvedores da equipe são considerados donos do bot.

- Adiciona atributo opcional ``integration_type`` em :attr:`AuditLogEntry.extra` para ações ``kick`` ou ``member_role_update``.
- Suporte para :class:`ui.Item` "dinâmico" que permite analisar estado a partir de um ``custom_id`` usando regex.
    - Para usar, é necessário subclasse de :class:`ui.DynamicItem`.
    - Alternativa às views persistentes.
    - Adiciona :meth:`Client.add_dynamic_items`.
    - Adiciona :meth:`Client.remove_dynamic_items`.
    - Adiciona :meth:`ui.Item.interaction_check`.
    - Confira o exemplo :resource:`dynamic_counter example <examples>` para mais informações.

- Suporte para leitura de reações em burst. A API atualmente não suporta envio dessas reações.
    - Adiciona :attr:`Reaction.normal_count`.
    - Adiciona :attr:`Reaction.burst_count`.
    - Adiciona :attr:`Reaction.me_burst`.

- Suporte para valores padrão em menus de seleção (:issue:`9577`).
    - Adiciona :class:`SelectDefaultValue`.
    - Adiciona :class:`SelectDefaultValueType`.
    - Adiciona atributo ``default_values`` para cada menu de seleção especializado.

- Parâmetro ``scheduled_event`` para :meth:`StageChannel.create_instance` (:issue:`9595`).
- Suporte para auto mod em membros (:issue:`9328`).
    - Adiciona argumento ``type`` em :class:`AutoModRuleAction`.
    - Adiciona :attr:`AutoModTrigger.mention_raid_protection`.
    - Adiciona :attr:`AutoModRuleTriggerType.member_profile`.
    - Adiciona :attr:`AutoModRuleEventType.member_update`.
    - Adiciona :attr:`AutoModRuleActionType.block_member_interactions`.

- Suporte para integrações premium de aplicativo (:issue:`9453`).
    - Adiciona múltiplas classes relacionadas a SKU e entitlements, e.g., :class:`SKU`, :class:`Entitlement`, :class:`SKUFlags`.
    - Adiciona múltiplos enums, e.g., :class:`SKUType`, :class:`EntitlementType`, :class:`EntitlementOwnerType`.
    - Adiciona :meth:`Client.fetch_skus` e :meth:`Client.fetch_entitlement`.
    - Adiciona :meth:`Client.create_entitlement`.
    - Adiciona :attr:`Client.entitlements`.
    - Adiciona :attr:`Interaction.entitlement_sku_ids`.
    - Adiciona :attr:`Interaction.entitlements`.
    - Adiciona :attr:`ButtonStyle.premium` e :attr:`ui.Button.sku_id` para enviar botão pedindo compra de SKU (:issue:`9845`).
    - Suporte para compra única (:issue:`9803`).

- Suporte para edição de informações de aplicativo (:issue:`9610`).
    - Adiciona :attr:`AppInfo.interactions_endpoint_url`.
    - Adiciona :attr:`AppInfo.redirect_uris`.
    - Adiciona :meth:`AppInfo.edit`.

- Suporte para obter/fetch threads a partir de :class:`Message` (:issue:`9665`).
    - Adiciona :attr:`PartialMessage.thread`.
    - Adiciona :attr:`Message.thread`.
    - Adiciona :meth:`Message.fetch_thread`.

- Suporte para plataforma e assets em atividades (:issue:`9677`).
    - Adiciona :attr:`Activity.platform`.
    - Adiciona :attr:`Game.platform`.
    - Adiciona :attr:`Game.assets`.

- Suporte para suprimir embeds em respostas de interação (:issue:`9678`).
- Suporte para adicionar tags de threads de fórum via webhook (:issue:`9680`, :issue:`9783`).
- Suporte para tipos de mensagens de incidentes de guilda (:issue:`9686`).
- Adiciona :attr:`Locale.latin_american_spanish` (:issue:`9689`).
- Suporte para status de canal de voz (:issue:`9603`).
- Adiciona parâmetro de timeout de conexão de shard para :class:`AutoShardedClient`.
- Suporte para incidentes de guilda (:issue:`9590`).
    - Atualiza :meth:`Guild.edit` com parâmetros ``invites_disabled_until`` e ``dms_disabled_until``.
    - Adiciona :attr:`Guild.invites_paused_until`.
    - Adiciona :attr:`Guild.dms_paused_until`.
    - Adiciona :meth:`Guild.invites_paused`.
    - Adiciona :meth:`Guild.dms_paused`.

- Suporte para :attr:`abc.User.avatar_decoration` (:issue:`9343`).
- Suporte para stickers GIF (:issue:`9737`).
- Suporte para atualizar banners de :class:`ClientUser` (:issue:`9752`).
- Suporte para banimento em massa via :meth:`Guild.bulk_ban`.
- Argumento ``reason`` para :meth:`Thread.delete` (:issue:`9804`).
- Adiciona :attr:`AppInfo.approximate_guild_count` (:issue:`9811`).
- Suporte para :attr:`Message.interaction_metadata` (:issue:`9817`).
- Suporte para diferentes tipos de :class:`Invite` (:issue:`9682`).
- Suporte para tipos de reação em modelos raw e non-raw (:issue:`9836`).
- |tasks| Adiciona parâmetro ``name`` em :meth:`~ext.tasks.loop` para nomear a :class:`asyncio.Task` interna.
- |commands| Adiciona comportamento de fallback para :class:`~ext.commands.CurrentGuild`.
- |commands| Adiciona logging para erros que ocorrem durante :meth:`~ext.commands.Cog.cog_unload`.
- |commands| Adiciona suporte para :class:`typing.NewType` e aliases de tipo via palavra-chave ``type`` (:issue:`9815`).
    - Também suporta comandos de aplicação.

- |commands| Adiciona suporte para parâmetros de flag apenas-posicionais (:issue:`9805`).
- |commands| Adiciona suporte para URLs de canais em classes relacionadas ao ChannelConverter (:issue:`9799`).


Correções de Bugs
~~~~~~~~~~~~~~~~~

- Corrige cache de emojis e stickers sendo preenchido mesmo com a intent desligada.
- Corrige pedidos de chunk pendentes não sendo limpos ao receber evento READY do gateway (:issue:`9571`).
- Corrige comportamento de escape para listas e headers em :meth:`~utils.escape_markdown`.
- Corrige valor de alias para :attr:`Intents.auto_moderation` (:issue:`9524`).
- Correções e melhorias para :class:`FFmpegAudio` e todas subclasses relacionadas (:issue:`9528`).
- Corrige :meth:`Template.source_guild` tentando resolver via cache (:issue:`9535`).
- Corrige :exc:`IndexError` sendo lançado em vez de :exc:`ValueError` ao chamar :meth:`Colour.from_str` com string vazia (:issue:`9540`).
- Corrige :meth:`View.from_message` não criando corretamente os diferentes tipos de :class:`ui.Select` (:issue:`9559`).
- Corrige logging de exceções de autocomplete, que antes eram suprimidas.
- Corrige possível erro na lógica de limpeza de voz (:issue:`9572`).
- Corrige possível :exc:`AttributeError` em :meth:`app_commands.CommandTree.sync` se um comando for considerado 'muito grande'.
- Corrige possível :exc:`TypeError` se um :class:`app_commands.Group` não tiver nome definido (:issue:`9581`).
- Corrige estado de voz inválido ao mover para canal com permissões ausentes (:issue:`9596`).
- Corrige websocket entrando em estado de erro devido a payload recebido (:issue:`9561`).
- Corrige tratamento de :class:`AuditLogDiff` relacionado a triggers de auto mod (:issue:`9622`).
- Corrige condição de corrida na lógica de voz envolvendo desconectar e conectar (:issue:`9683`).
- Usa guilda de :attr:`Interaction.user` como fallback para :attr:`Interaction.guild` se não estiver disponível.
- Corrige restrição na faixa de IDs do log de auditoria de auto mod.
- Corrige verificação do número máximo de filhos por :class:`ui.View`.
- Corrige comparação entre classes :class:`Object` com ``type`` definido.
- Corrige tratamento de enum em :meth:`AutoModRule.edit` (:issue:`9798`).
- Corrige tratamento de :meth:`Client.close` dentro de :meth:`Client.__aexit__` (:issue:`9769`).
- Corrige exclusão de canal não removendo threads relacionadas do cache (:issue:`9796`).
- Corrige bug em cache que incrementava posições de cargo desnecessariamente (:issue:`9853`).
- Corrige ``exempt_channels`` não sendo passado em :meth:`Guild.create_automod_rule` (:issue:`9861`).
- Corrige :meth:`abc.GuildChannel.purge` falhando em modo de exclusão de mensagem única se a mensagem já foi deletada (:issue:`9830`, :issue:`9863`).
- |commands| Corrige suporte de localização para fallback de :class:`~ext.commands.HybridGroup`.
- |commands| Corrige inserção manual de comandos de aplicação em :class:`~ext.commands.HybridGroup` aninhados.
- |commands| Corrige problema onde instâncias wrapadas de :class:`~ext.commands.HybridGroup` ficavam fora de sincronia.
- |commands| Corrige checks definidos em :class:`~ext.commands.HelpCommand` não sendo copiados (:issue:`9843`).

Diversos
~~~~~~~~

- Documentação adicional adicionada para capacidades de logging.
- Aumento de performance na construção de :class:`Permissions` usando argumentos nomeados.
- Melhoria no ``__repr__`` de :class:`SyncWebhook` e :class:`Webhook` (:issue:`9764`).
- Padronização de nomes internos de threads (:issue:`9538`).

.. _vp2p3p2:

v2.3.2
-------

Correções de Bugs
~~~~~~~~~~~~~~~~~

- Corrigido o parâmetro ``name`` que não estava sendo respeitado ao enviar uma :class:`CustomActivity`.
- Corrigido :attr:`Intents.emoji` e :attr:`Intents.emojis_and_stickers` que tinham valores de alias trocados (:issue:`9471`).
- Corrigido o erro ``NameError`` ao usar :meth:`abc.GuildChannel.create_invite` (:issue:`9505`).
- Corrigido o crash ao desconectar no meio de um pacote ``HELLO`` ao usar :class:`AutoShardedClient`.
- Corrigido o websocket de voz que não estava sendo fechado antes de ser substituído por um novo (:issue:`9518`).
- |commands| Corrigido o método errado :meth:`~ext.commands.HelpCommand.on_help_command_error` sendo chamado ao ser removido de um cog.
- |commands| Corrigido ``=None`` sendo exibido em :attr:`~ext.commands.Command.signature`.

.. _vp2p3p1:

v2.3.1
-------

Correções de Bugs
~~~~~~~~~~~~~~~~~

- Corrigido a busca de nomes de usuário em :meth:`Guild.get_member_named` (:issue:`9451`).
- Usar dados do cache primeiro para :attr:`Interaction.channel` em vez de dados da API.
    - Esse bug geralmente se manifestava em objetos de canal incompletos (por exemplo, sem ``overwrites``), porque o Discord não fornece esses dados.

- Corrigido falsos positivos em :meth:`PartialEmoji.from_str` configurando ``animated`` como ``True`` de forma inapropriada (:issue:`9456`, :issue:`9457`).
- Corrigido certos tipos de select que não apareciam em :attr:`Message.components` (:issue:`9462`).
- |commands| Alterada a ordem de busca para :class:`~ext.commands.MemberConverter` e :class:`~ext.commands.UserConverter` para priorizar nomes de usuário em vez de apelidos.

.. _vp2p3p0:

v2.3.0
--------

Novos Recursos
~~~~~~~~~~~~~~

- Adicionado suporte para o novo sistema de nomes de usuário (também conhecido como "pomelo").
    - Adicionado :attr:`User.global_name` para obter o apelido global ou "nome de exibição".
    - Atualizado :attr:`User.display_name` e :attr:`Member.display_name` para entender apelidos globais.
    - Atualizado ``__str__`` para :class:`User` para remover discriminadores se o usuário foi migrado.
    - Atualizado :meth:`Guild.get_member_named` para funcionar com usuários migrados.
    - Atualizado :attr:`User.default_avatar` para funcionar com usuários migrados.
    - |commands| Atualizados conversores de usuário e membro para entender usuários migrados.

- Adicionado :attr:`DefaultAvatar.pink` para novos avatares padrão rosa.
- Adicionado :meth:`Colour.pink` para obter a cor do avatar padrão rosa.
- Adicionado suporte para mensagens de voz (:issue:`9358`)
    - Adicionado :attr:`MessageFlags.voice`
    - Adicionado :attr:`Attachment.duration` e :attr:`Attachment.waveform`
    - Adicionado :meth:`Attachment.is_voice_message`
    - Isso não suporta *enviar* mensagens de voz pois atualmente não é suportado pela API.

- Adicionado suporte para novo atributo :attr:`Interaction.channel` da atualização da API (:issue:`9339`).
- Adicionado suporte para :attr:`TextChannel.default_thread_slowmode_delay` (:issue:`9291`).
- Adicionado suporte para :attr:`ForumChannel.default_sort_order` (:issue:`9290`).
- Adicionado suporte para ``default_reaction_emoji`` e ``default_forum_layout`` em :meth:`Guild.create_forum` (:issue:`9300`).
- Adicionado suporte para ``widget_channel``, ``widget_enabled``, e ``mfa_level`` em :meth:`Guild.edit` (:issue:`9302`, :issue:`9303`).
- Adicionadas várias novas :class:`Permissions` e alterações (:issue:`9312`, :issue:`9325`, :issue:`9358`, :issue:`9378`)
    - Novas permissões: :attr:`~Permissions.manage_expressions`, :attr:`~Permissions.use_external_sounds`, :attr:`~Permissions.use_soundboard`, :attr:`~Permissions.send_voice_messages`, :attr:`~Permissions.create_expressions`.
    - Alterado :attr:`Permissions.manage_emojis` para ser um alias de :attr:`~Permissions.manage_expressions`.

- Adicionadas várias novas propriedades a :class:`PartialAppInfo` e :class:`AppInfo` (:issue:`9298`).
- Adicionado suporte para o parâmetro ``with_counts`` em :meth:`Client.fetch_guilds` (:issue:`9369`).
- Novo helper :meth:`Guild.get_emoji` (:issue:`9296`).
- Adicionado :attr:`ApplicationFlags.auto_mod_badge` (:issue:`9313`).
- Adicionado :attr:`Guild.max_stage_video_users` e :attr:`Guild.safety_alerts_channel` (:issue:`9318`).
- Adicionado suporte para ``raid_alerts_disabled`` e ``safety_alerts_channel`` em :meth:`Guild.edit` (:issue:`9318`).
- |commands| Adicionado :attr:`BadLiteralArgument.argument <ext.commands.BadLiteralArgument.argument>` para obter o valor do argumento que falhou (:issue:`9283`).
- |commands| Adicionado :attr:`Context.filesize_limit <ext.commands.Context.filesize_limit>` (:issue:`9416`).
- |commands| Suporte para :attr:`Parameter.displayed_name <ext.commands.Parameter.displayed_name>` (:issue:`9427`).

Correções de Bugs
~~~~~~~~~~~~~~~~~

- Corrigido ``FileHandler`` gravando caracteres ANSI quando o bot é executado no PyCharm.
    - Isso remove os logs coloridos do terminal do PyCharm devido a um bug de detecção TTY upstream (`PY-43798 <https://youtrack.jetbrains.com/issue/PY-43798>`_).

- Corrigido edições de canal com :meth:`Webhook.edit` enviando duas requisições em vez de uma.
- Corrigido :attr:`StageChannel.last_message_id` sempre sendo ``None`` (:issue:`9422`).
- Corrigido entrada de áudio piped terminando prematuramente (:issue:`9001`, :issue:`9380`).
- Corrigido detecção persistente para :class:`ui.TextInput` quando ``custom_id`` é definido depois (:issue:`9438`).
- Corrigido atributos personalizados não sendo copiados ao herdar de :class:`app_commands.Group` (:issue:`9383`).
- Corrigido erro de entrada de log do AutoMod devido a canal_id vazio (:issue:`9384`).
- Corrigido manuseio do parâmetro ``around`` em :meth:`abc.Messageable.history` (:issue:`9388`).
- Corrigido :exc:`AttributeError` ocasional ao acessar :attr:`ClientUser.mutual_guilds` (:issue:`9387`).
- Corrigido :func:`utils.escape_markdown` para escapar a nova markdown (:issue:`9361`).
- Corrigido webhook targets não sendo convertidos em audit logs (:issue:`9332`).
- Corrigido erro ao não passar ``enabled`` em :meth:`Guild.create_automod_rule` (:issue:`9292`).
- Corrigido manuseio de diversos parâmetros em :meth:`Guild.create_scheduled_event` (:issue:`9275`).
- Corrigido não envio do parâmetro ``ssrc`` ao enviar payload SPEAKING (:issue:`9301`).
- Corrigido :attr:`Message.guild` sendo ``None`` às vezes quando recebido via interação.
- Corrigido :attr:`Message.system_content` para :attr:`MessageType.channel_icon_change` (:issue:`9410`).

Diversos
~~~~~~~~

- Atualizado limite base :attr:`Guild.filesize_limit` para 25MiB (:issue:`9353`).
- Permitido URLs de webhooks de Interação em :meth:`Webhook.from_url`.
- Definido socket family do conector interno para ``AF_INET`` para prevenir conexões IPv6 (:issue:`9442`, :issue:`9443`).

.. _vp2p2p3:

v2.2.3
-------

Correções de Bugs
~~~~~~~~~~~~~~~~~

- Corrigido crash causado pelo envio de ``channel_id`` nulo pelo Discord em logs de auditoria do automod.
- Corrigido edições de ``channel`` usando :meth:`Webhook.edit` enviando duas requisições.
- Corrigido :attr:`AuditLogEntry.target` sendo ``None`` para convites (:issue:`9336`).
- Corrigido :exc:`KeyError` ao acessar dados de :class:`GuildSticker` (:issue:`9324`).


.. _vp2p2p2:

v2.2.2
-------

Correções de Bugs
~~~~~~~~~~~~~~~~~

- Corrigido UDP discovery em voice não utilizando o novo layout de 74 bytes, o que causava falha no voice (:issue:`9277`, :issue:`9278`)


.. _vp2p2p0:

v2.2.0
-------

Novos Recursos
~~~~~~~~~~~~~~

- Adicionado suporte para o novo evento :func:`on_audit_log_entry_create`.
- Adicionado suporte para mensagens silenciosas via parâmetro ``silent`` em :meth:`abc.Messageable.send`.
- Isso pode ser consultado via :attr:`MessageFlags.suppress_notifications`.

- Implementado :class:`abc.Messageable` para :class:`StageChannel` (:issue:`9248`).
- Adicionado setter para :attr:`discord.ui.ChannelSelect.channel_types` (:issue:`9068`).
- Adicionado suporte para mensagens customizadas no automod via :attr:`AutoModRuleAction.custom_message` (:issue:`9267`).
- Adicionado :meth:`ForumChannel.get_thread` (:issue:`9106`).
- Adicionado :attr:`StageChannel.slowmode_delay` e :attr:`VoiceChannel.slowmode_delay` (:issue:`9111`).
- Adicionado suporte para editar o slowmode em :class:`StageChannel` e :class:`VoiceChannel` (:issue:`9111`).
- Adicionado :attr:`Locale.indonesian`.
- Adicionado argumento ``delete_after`` para :meth:`Interaction.edit_message` (:issue:`9415`).
- Adicionado argumento ``delete_after`` para :meth:`InteractionMessage.edit` (:issue:`9206`).
- Adicionado suporte para flags de membros (:issue:`9204`).
- Acessível via :attr:`Member.flags` com tipo :class:`MemberFlags`.
- Suporte para ``bypass_verification`` em :meth:`Member.edit`.

- Adicionado suporte para passar um client em :meth:`Webhook.from_url` e :meth:`Webhook.partial`.
- Permite usar views se forem webhooks "bot owned".

- Adicionado :meth:`Colour.dark_embed` e :meth:`Colour.light_embed` (:issue:`9219`).
- Adicionado suporte para mais parâmetros em :meth:`Guild.create_stage_channel` (:issue:`9245`).
- Adicionado :attr:`AppInfo.role_connections_verification_url`.
- Adicionado suporte para :attr:`ForumChannel.default_layout`.
- Adicionados vários novos valores para :class:`MessageType` relacionados a stage channel e role subscriptions.
- Adicionado suporte para atributos relacionados a role subscription.
- :class:`RoleSubscriptionInfo` em :attr:`Message.role_subscription`.
- :attr:`MessageType.role_subscription_purchase`.
- :attr:`SystemChannelFlags.role_subscription_purchase_notifications`.
- :attr:`SystemChannelFlags.role_subscription_purchase_notification_replies`.
- :attr:`RoleTags.subscription_listing_id`.
- :meth:`RoleTags.is_available_for_purchase`.

- Adicionado suporte para verificar se um role é linked em :meth:`RoleTags.is_guild_connection`.
- Adicionado suporte para GIF sticker type.
- Adicionado suporte para :attr:`Message.application_id` e :attr:`Message.position`.
- Adicionado helper :func:`utils.maybe_coroutine`.
- Adicionado :attr:`ScheduledEvent.creator_id`.
- |commands| Adicionado suporte para :meth:`~ext.commands.Cog.interaction_check` para :class:`~ext.commands.GroupCog` (:issue:`9189`).

Correções de Bugs
~~~~~~~~~~~~~~~~~

- Corrigido views não sendo removidas do message store, evitando memory leak em contextos de app commands.
- Corrigido iteradores assíncronos solicitando além dos limites com ``oldest_first`` e ``after`` ou ``before`` (:issue:`9093`).
- Corrigido lógica de paginação de :meth:`Guild.audit_logs` com ``after`` (:issue:`9269`).
- Corrigido :attr:`Message.channel` retornando às vezes :class:`Object` ao invés de :class:`PartialMessageable`.
- Corrigido :class:`ui.View` não chamando corretamente ``super().__init_subclass__`` (:issue:`9231`).
- Corrigido ``available_tags`` e ``default_thread_slowmode_delay`` não sendo respeitados em :meth:`Guild.create_forum`.
- Corrigido :class:`AutoModTrigger` ignorando ``allow_list`` com keyword type (:issue:`9107`).
- Corrigido resolução implícita de permissões para :class:`Thread` (:issue:`9153`).
- Corrigido :meth:`AutoModRule.edit` para funcionar com snowflakes reais como :class:`Object` (:issue:`9159`).
- Corrigido :meth:`Webhook.send` retornando :class:`ForumChannel` para :attr:`WebhookMessage.channel`.
- Quando a busca por :attr:`AuditLogEntry.target` falha, retorna um :class:`Object` com :attr:`Object.type` apropriado (:issue:`9171`).
- Corrigido :attr:`AuditLogDiff.type` para integrações retornando :class:`ChannelType` ao invés de :class:`str` (:issue:`9200`).
- Corrigido :attr:`AuditLogDiff.type` para webhooks retornando :class:`ChannelType` ao invés de :class:`WebhookType` (:issue:`9251`).
- Corrigido fechamento de arquivos em webhooks e interações após requisição concluída.
- Corrigido :exc:`NameError` no target de audit log para app commands.
- Corrigido :meth:`ScheduledEvent.edit` exigindo argumentos desnecessários (:issue:`9261`, :issue:`9268`).
- |commands| Definido explicitamente traceback para invocações de comandos híbridos (:issue:`9205`).

Diversos
~~~~~~~~

- Adicionado preview de cores para cores pré-definidas em :class:`Colour`.
- Views finalizadas não são mais armazenadas pela library ao serem enviadas (:issue:`9235`).
- Forçado habilitar logging colorido no handler padrão quando rodando no Docker.
- Adicionados overloads para :meth:`Client.wait_for` para ajudar na análise estática (:issue:`9184`).
- :class:`Interaction` pode opcionalmente receber parâmetro genérico ``ClientT`` para tipo de :attr:`Interaction.client`.
- |commands| Respeitar :attr:`~ext.commands.Command.ignore_extra` para parâmetros keyword-only de :class:`~discord.ext.commands.FlagConverter`.
- |commands| Alterado :attr:`Paginator.pages <ext.commands.Paginator.pages>` para não fechar prematuramente (:issue:`9257`).

.. _vp2p1p1:

v2.1.1
-------

Bug Fixes
~~~~~~~~~~

- Corrigido crash envolvendo GIF stickers ao buscar a extensão do filename.


.. _vp2p1p0:

v2.1.0
-------

Novos Recursos
~~~~~~~~~~~~~~

- Adicionado suporte para ``delete_message_seconds`` em :meth:`Guild.ban` (:issue:`8391`).
- Adicionado suporte para ações de audit log relacionadas ao automod (:issue:`8389`).
- Adicionado suporte para anotações de :class:`ForumChannel` em app commands.
- Adicionado suporte para :attr:`ForumChannel.default_thread_slowmode_delay`.
- Adicionado suporte para :attr:`ForumChannel.default_reaction_emoji`.
- Adicionado suporte para tags de forum via :class:`ForumTag`.
- Tags podem ser obtidas via :attr:`ForumChannel.available_tags` ou :meth:`ForumChannel.get_tag`.
- Veja :meth:`Thread.edit` e :meth:`ForumChannel.edit` para modificar tags e seu uso.

- Adicionado suporte para novos tipos de select (:issue:`9013`, :issue:`9003`).
- Divididos em classes separadas: :class:`~discord.ui.ChannelSelect`, :class:`~discord.ui.RoleSelect`, :class:`~discord.ui.UserSelect`, :class:`~discord.ui.MentionableSelect`.
- O decorator ainda usa uma única função, :meth:`~discord.ui.select`. O tipo de select é alterado pelo parâmetro keyword ``cls``.

- Adicionado suporte para alternar discoverable e invites_disabled em :meth:`Guild.edit` (:issue:`8390`).
- Adicionado helper :meth:`Interaction.translate` (:issue:`8425`).
- Adicionado :meth:`Forum.archived_threads` (:issue:`8476`).
- Adicionados :attr:`ApplicationFlags.active`, :attr:`UserFlags.active_developer`, :attr:`PublicUserFlags.active_developer`.
- Adicionado ``delete_after`` em :meth:`InteractionResponse.send_message` (:issue:`9022`).
- Adicionado suporte para :attr:`AutoModTrigger.regex_patterns`.
- |commands| Adicionado :attr:`GroupCog.group_extras <discord.ext.commands.GroupCog.group_extras>` para configurar :attr:`app_commands.Group.extras` (:issue:`8405`).
    - |commands| Adicionado suporte a docstrings estilo NumPy para comandos regulares para definir descrições de parâmetros.
    - |commands| Permitir que :class:`~discord.ext.commands.Greedy` mantenha estado entre chamadas.
    - |commands| Adicionado :meth:`Cog.has_app_command_error_handler <discord.ext.commands.Cog.has_app_command_error_handler>` (:issue:`8991`).
        - |commands| Permitir ``delete_after`` em :meth:`Context.send <discord.ext.commands.Context.send>` para mensagens efêmeras (:issue:`9021`).
            
Correções de Bugs
~~~~~~~~~~~~~~~~~
            
- Corrigido :exc:`KeyError` ao construir :class:`app_commands.Group` sem módulo (:issue:`8411`).
- Corrigido regex de URL de webhook não escapando ponto (:issue:`8443`).
- Corrigido :exc:`app_commands.CommandSyncFailure` disparando para outros códigos de status 400.
- Corrigido problemas de formatação mostrando `_errors` em :exc:`app_commands.CommandSyncFailure`.
- Corrigido :attr:`Guild.stage_instances` e :attr:`Guild.schedule_events` sendo limpos em ``GUILD_UPDATE``.
- Corrigida detecção de :meth:`app_commands.Group.on_error` sobrescrita.
- Corrigido :meth:`app_commands.CommandTree.on_error` sendo chamado mesmo com um handler de erro ligado.
- Corrigido permissões de thread sendo definidas como ``True`` em :meth:`DMChannel.permissions_for` (:issue:`8965`).
- Corrigido ``on_scheduled_event_delete`` despachando com parâmetros excessivos (:issue:`9019`).
- |commands| Corrigido :meth:`Context.from_interaction <discord.ext.commands.Context.from_interaction>` ignorando :attr:`~discord.ext.commands.Context.command_failed`.
    - |commands| Corrigido :class:`~discord.ext.commands.Range` para aceitar sintaxe Union do Python 3.10 (:issue:`8446`).
    - |commands| Corrigido ``before_invoke`` não disparando para fallback commands em hybrid group commands (:issue:`8461`, :issue:`8462`).
                
Diversos
~~~~~~~~
                
- Alterada mensagem de erro para callbacks não ligados em :class:`app_commands.ContextMenu` para deixar claro que métodos ligados não são permitidos.
- Normalizado formatação de tipo em exceções TypeError (:issue:`8453`).
- Alterados parâmetros de :meth:`VoiceProtocol.on_voice_state_update` e :meth:`VoiceProtocol.on_voice_server_update` para serem somente posicionais (:issue:`8463`).
- Adicionado suporte ao PyCharm para logger colorido padrão (:issue:`9015`).


.. _vp2p0p1:

v2.0.1
-------

Correcao de bugs
~~~~~~~~~~

- Corrigido ``cchardet`` sendo instalado no Python >=3.10 usando o extra ``speed``.
- Corrigido timeout de :class:`ui.View` ao falhar :meth:`ui.View.interaction_check`.
- Corrigido :meth:`app_commands.CommandTree.on_error` não disparando se :meth:`~app_commands.CommandTree.interaction_check` levanta erro.
- Corrigido script ``__main__`` para usar ``importlib.metadata`` em vez do depreciado ``pkg_resources``.
- Corrigidos callbacks da library disparando erro de type checking se os nomes dos parâmetros eram diferentes.
- Isso exigiu alteração no :ref:`version_guarantees`.
                
- |commands| Corrigido tipos Union do Python 3.10 não funcionando com :class:`commands.Greedy <discord.ext.commands.Greedy>`.

.. _vp2p0p0:

v2.0.0
--------

O changelog desta versão é grande demais😏 para ser listado aqui. Para mais informações, veja :ref:`the migrating page <migrating_2_0>`.


.. _vp1p7p3:

v1.7.3
--------

Correcao de bugs (to fazendo de propósito a falta de acentuação pq mobile não merece esse sofrimento 😔)
~~~~~~~~~~

- Corrigido crash envolvendo guild uploaded stickers.
- Corrigido :meth:`DMChannel.permissions_for` não tendo :attr:`Permissions.read_messages` definido.

.. _vp1p7p2:

v1.7.2
-------

Correções de Bugs
~~~~~~~~~~~~~~~~~

- Corrige ``fail_if_not_exists`` fazendo com que certas referências de mensagem não pudessem ser usadas em :meth:`abc.Messageable.send` e :meth:`Message.reply` (:issue:`6726`)
- Corrige :meth:`Guild.chunk` travando quando o usuário saiu do servidor (:issue:`6730`)
- Corrige a pausa do loop ocorrendo após a iteração final em vez de antes (:issue:`6744`)


.. _vp1p7p1:

v1.7.1
-------

Correções de Bugs
~~~~~~~~~~~~~~~~~

- |commands| Corrige :meth:`Cog.has_error_handler <ext.commands.Cog.has_error_handler>` não funcionando como esperado


.. _vp1p7p0:

v1.7.0
--------

Esta versão é principalmente para melhorias e correções de bugs. É muito provavelmente a última versão principal da série 1.x.
O trabalho a partir daqui será focado no v2.0. Como resultado, **esta é a última versão a suportar Python 3.5**.
Da mesma forma, **esta é a última versão a suportar user bots**.

O desenvolvimento do v2.0 terá mudanças incompatíveis e suporte para novos recursos da API.

Novos Recursos
~~~~~~~~~~~~~~

- Suporte a canais de palco via :class:`StageChannel` (:issue:`6602`, :issue:`6608`)
- Suporte a :attr:`MessageReference.fail_if_not_exists` (:issue:`6484`)
- Suporte ao novo esquema de serialização de permissões do Discord.
- Forma mais fácil de mover canais usando :meth:`abc.GuildChannel.move`
- Adiciona :attr:`Permissions.use_slash_commands`
- Adiciona :attr:`Permissions.request_to_speak`
- Suporte a regiões de voz em canais de voz via :attr:`VoiceChannel.rtc_region` (:issue:`6606`)
- Suporte a :meth:`PartialEmoji.url_as` (:issue:`6341`)
- Adiciona :attr:`MessageReference.jump_url` (:issue:`6318`)
- Adiciona :attr:`File.spoiler` (:issue:`6317`)
- Suporte para passar ``roles`` em :meth:`Guild.estimate_pruned_members` (:issue:`6538`)
- Permitir factories de classe chamáveis em :meth:`abc.Connectable.connect` (:issue:`6478`)
- Adicionar uma forma de obter servidores em comum do cache do cliente via :attr:`User.mutual_guilds` (:issue:`2539`, :issue:`6444`)
- :meth:`PartialMessage.edit` agora retorna uma :class:`Message` completa ao ter sucesso (:issue:`6309`)
- Adiciona :attr:`RawMessageUpdateEvent.guild_id` (:issue:`6489`)
- :class:`AuditLogEntry` agora é hashable (:issue:`6495`)
- :class:`Attachment` agora é hashable
- Adiciona :attr:`Attachment.content_type` (:issue:`6618`)
- Suporte para converter :class:`Attachment` em :class:`str` para obter a URL.
- Adiciona parâmetro ``seed`` para :class:`Colour.random` (:issue:`6562`)
- Adiciona função auxiliar :func:`utils.remove_markdown` (:issue:`6573`)
- Suporte para passar scopes em :func:`utils.oauth_url` (:issue:`6568`)
- |commands| Suporte à função CSS ``rgb`` como parâmetro de :class:`ColourConverter <ext.commands.ColourConverter>` (:issue:`6374`)
- |commands| Suporte para converter :class:`StoreChannel` via :class:`StoreChannelConverter <ext.commands.StoreChannelConverter>` (:issue:`6603`)
- |commands| Suporte para remover espaços em branco após o prefixo usando o parâmetro ``strip_after_prefix`` do :class:`~ext.commands.Bot`
- |commands| Adiciona :attr:`Context.invoked_parents <ext.commands.Context.invoked_parents>` para obter os aliases do comando pai (:issue:`1874`, :issue:`6462`)
- |commands| Adiciona conversor para :class:`PartialMessage` via :class:`ext.commands.PartialMessageConverter` (:issue:`6308`)
- |commands| Adiciona conversor para :class:`Guild` via :class:`ext.commands.GuildConverter` (:issue:`6016`, :issue:`6365`)
- |commands| Adiciona :meth:`Command.has_error_handler <ext.commands.Command.has_error_handler>`
- |commands| Permite que tipos chamáveis atuem como chave de bucket para cooldowns (:issue:`6563`)
- |commands| Adiciona argumento ``linesep`` ao :class:`Paginator <ext.commands.Paginator>` (:issue:`5975`)
- |commands| Permite passar ``None`` para :attr:`HelpCommand.verify_checks <ext.commands.HelpCommand.verify_checks>` para verificar apenas no contexto do servidor (:issue:`2008`, :issue:`6446`)
- |commands| Permite caminhos relativos ao carregar extensões usando o argumento ``package`` (:issue:`2465`, :issue:`6445`)

Correções de Bugs
~~~~~~~~~~~~~~~~~~

- Corrige menções não funcionando se ``mention_author`` for passado em :meth:`abc.Messageable.send` sem :attr:`Client.allowed_mentions` definido (:issue:`6192`, :issue:`6458`)
- Corrige instâncias criadas pelo usuário de :class:`CustomActivity` gerando erro (:issue:`4049`)
- Corrige :exc:`ZeroDivisionError` levantado por :attr:`VoiceClient.average_latency` (:issue:`6430`, :issue:`6436`)
- Corrige :attr:`User.public_flags` não atualizando após edição (:issue:`6315`)
- Corrige :attr:`Message.call` causando erros de atributo (:issue:`6390`)
- Corrige reenvio de arquivo durante retries em versões mais novas do ``aiohttp`` (:issue:`6531`)
- Levanta erro quando ``user_ids`` está vazio em :meth:`Guild.query_members`
- Corrige ``__str__`` lançando erro quando :class:`Guild` está indisponível.
- Corrige possível :exc:`AttributeError` ao acessar :attr:`VoiceChannel.members` (:issue:`6602`)
- Parâmetros do construtor de :class:`Embed` agora convertem implicitamente para :class:`str` (:issue:`6574`)
- Garante que o pacote ``discord`` só rode se executado como script (:issue:`6483`)
- |commands| Corrige comandos irrelevantes sendo descarregados durante unload de cog devido a falha
- |commands| Corrige erros de atributo ao definir um cog como :class:`~.ext.commands.HelpCommand` (:issue:`5154`)
- |commands| Corrige :attr:`Context.invoked_with <ext.commands.Context.invoked_with>` sendo redefinido de forma incorreta durante :meth:`~ext.commands.Context.reinvoke` (:issue:`6451`, :issue:`6462`)
- |commands| Remove duplicatas de :meth:`HelpCommand.get_bot_mapping <ext.commands.HelpCommand.get_bot_mapping>` (:issue:`6316`)
- |commands| Trata corretamente parâmetros apenas-posicionais em assinaturas de comando (:issue:`6431`)
- |commands| Assinaturas de grupo agora aparecem corretamente em :attr:`Command.signature <ext.commands.Command.signature>` (:issue:`6529`, :issue:`6530`)

Diversos
~~~~~~~~~~

- Endpoints de usuário e todas funcionalidades de userbot foram depreciadas e serão removidas na próxima versão principal
- Métodos da classe :class:`Permission` foram atualizados para corresponder à UI do cliente do Discord (:issue:`6476`)
- Caracteres ``_`` e ``-`` agora são removidos ao criar um novo cog usando o pacote ``discord`` (:issue:`6313`)

.. _vp1p6p0:

v1.6.0
--------

Esta versão traz suporte para respostas e stickers.

Novos Recursos
~~~~~~~~~~~~~~

- Documentação totalmente redesenhada, resultado de vários meses de trabalho.
- Agora há tema escuro, que pode ser alterado na interface, embora normalmente seja automático.
- Suporte para :meth:`AppInfo.icon_url_as` e :meth:`AppInfo.cover_image_url_as` (:issue:`5888`)
- Adiciona :meth:`Colour.random` para obter uma cor aleatória (:issue:`6067`)
- Suporte para stickers via :class:`Sticker` (:issue:`5946`)
- Suporte para respostas via :meth:`Message.reply` (:issue:`6061`)
- Inclui a configuração :attr:`AllowedMentions.replied_user`
- :meth:`abc.Messageable.send` agora aceita :class:`MessageReference`
- :class:`MessageReference` pode ser construído pelo usuário
- :meth:`Message.to_reference` converte uma mensagem em :class:`MessageReference`
- Suporte para acessar a mensagem respondida resolvida via :attr:`MessageReference.resolved`
- Suporte para tags de funções:
- :attr:`Guild.premium_subscriber_role` para obter o cargo "Nitro Booster" (se disponível)
- :attr:`Guild.self_role` para obter o cargo do bot (se disponível)
- :attr:`Role.tags` para obter as tags do cargo
- :meth:`Role.is_premium_subscriber` para verificar se é o cargo "Nitro Booster"
- :meth:`Role.is_bot_managed` para verificar se é um cargo de bot
- :meth:`Role.is_integration` para verificar se é um cargo criado por integração
- Adiciona :meth:`Client.is_ws_ratelimited` para checar se o websocket está rate-limited
- :meth:`ShardInfo.is_ws_ratelimited` faz o mesmo para shards específicos
- Suporte para chunking de :class:`AsyncIterator` via :meth:`AsyncIterator.chunk` (:issue:`6100`, :issue:`6082`)
- Adiciona :attr:`PartialEmoji.created_at` (:issue:`6128`)
- Suporte para editar e deletar mensagens enviadas por webhook (:issue:`6058`)
- Inclui :class:`WebhookMessage`
- Adiciona :class:`PartialMessage` para trabalhar com mensagens usando apenas channel objects e message_id (:issue:`5905`)
- Adiciona :meth:`Emoji.url_as` (:issue:`6162`)
- Suporte para :attr:`Member.pending` (controle de membership gating)
- Permite que o parâmetro ``colour`` aceite ``int`` em :meth:`Guild.create_role` (:issue:`6195`)
- Suporte para ``presences`` em :meth:`Guild.query_members` (:issue:`2354`)
- |commands| Adiciona suporte ao argumento ``description`` em :class:`commands.Cog <ext.commands.Cog>` (:issue:`6028`)
    - |tasks| Suporte para chamar a coroutine via ``__call__``
    
    
Correções de Bugs
~~~~~~~~~~~~~~~~~
    
    - Lança :exc:`DiscordServerError` ao atingir 503s repetidos (:issue:`6044`)
    - Corrige :exc:`AttributeError` em :meth:`Client.fetch_template` (:issue:`5986`)
    - Corrige erros ao tocar áudio e trocar de canal (:issue:`5953`)
    - Corrige :exc:`AttributeError` quando canais de voz desconectam muito rápido (:issue:`6039`)
    - Corrige referências antigas de :class:`User` quando intent de membros está desativada
    - Corrige :func:`on_user_update` não disparando quando membro não está em cache mas usuário está
    - Corrige :attr:`Message.author` sendo sobrescrito durante update de mensagem
    - Corrige :exc:`UnboundLocalError` ao editar ``public_updates_channel`` em :meth:`Guild.edit` (:issue:`6093`)
    - Corrige :attr:`CustomActivity.created_at` não inicializado (:issue:`6095`)
    - |commands| Erros durante unload de cog não interrompem limpeza do módulo (:issue:`6113`)
    - |commands| Limpeza correta de comandos conflitantes ao adicionar (:issue:`6217`)
    
    
Diversos
~~~~~~~~~~
    
- Processos ``ffmpeg`` não abrem mais janelas no Windows (:issue:`6038`)
- Atualiza dependências para compatibilidade com Python 3.9+ sem ferramentas de build (:issue:`5984`, :issue:`5970`)
- Corrige docstring causando SyntaxError no Python 3.9 (:issue:`6153`)
- Atualiza binários Opus do Windows de 1.2.1 para 1.3.1 (:issue:`6161`)
- |commands| :class:`MessageConverter <ext.commands.MessageConverter>` regex atualizado para suportar prefixos ``www.`` (:issue:`6002`)
    - |commands| :class:`UserConverter <ext.commands.UserConverter>` agora busca na API se ID não está em cache
        - |commands| :func:`max_concurrency <ext.commands.max_concurrency>` agora é chamado antes dos cooldowns (:issue:`6172`)

.. _vp1p5p1:

v1.5.1
-------

Bug Fixes
~~~~~~~~~~~

- Fix :func:`utils.escape_markdown` not escaping quotes properly (:issue:`5897`)
- Fix :class:`Message` not being hashable (:issue:`5901`, :issue:`5866`)
- Fix moving channels to the end of the channel list (:issue:`5923`)
- Fix seemingly strange behaviour in ``__eq__`` for :class:`PermissionOverwrite` (:issue:`5929`)
- Fix aliases showing up in ``__iter__`` for :class:`Intents` (:issue:`5945`)
- Fix the bot disconnecting from voice when moving them to another channel (:issue:`5904`)
- Fix attribute errors when chunking times out sometimes during delayed on_ready dispatching.
- Ensure that the bot's own member is not evicted from the cache (:issue:`5949`)

Miscellaneous
~~~~~~~~~~~~~~

- Members are now loaded during ``GUILD_MEMBER_UPDATE`` events if :attr:`MemberCacheFlags.joined` is set. (:issue:`5930`)
- |commands| :class:`MemberConverter <ext.commands.MemberConverter>` now properly lazily fetches members if not available from cache.
    - This is the same as having ``discord.Member`` as the type-hint.
- :meth:`Guild.chunk` now allows concurrent calls without spamming the gateway with requests.

.. _vp1p5p0:

v1.5.0
--------

This version came with forced breaking changes that Discord is requiring all bots to go through on October 7th. It is highly recommended to read the documentation on intents, :ref:`intents_primer`.

API Changes
~~~~~~~~~~~~~

- Members and presences will no longer be retrieved due to an API change. See :ref:`privileged_intents` for more info.
- As a consequence, fetching offline members is disabled if the members intent is not enabled.

New Features
~~~~~~~~~~~~~~

- Support for gateway intents, passed via ``intents`` in :class:`Client` using :class:`Intents`.
- Add :attr:`VoiceRegion.south_korea` (:issue:`5233`)
- Add support for ``__eq__`` for :class:`Message` (:issue:`5789`)
- Add :meth:`Colour.dark_theme` factory method (:issue:`1584`)
- Add :meth:`AllowedMentions.none` and :meth:`AllowedMentions.all` (:issue:`5785`)
- Add more concrete exceptions for 500 class errors under :class:`DiscordServerError` (:issue:`5797`)
- Implement :class:`VoiceProtocol` to better intersect the voice flow.
- Add :meth:`Guild.chunk` to fully chunk a guild.
- Add :class:`MemberCacheFlags` to better control member cache. See :ref:`intents_member_cache` for more info.
- Add support for :attr:`ActivityType.competing` (:issue:`5823`)
    - This seems currently unused API wise.

- Add support for message references, :attr:`Message.reference` (:issue:`5754`, :issue:`5832`)
- Add alias for :class:`ColourConverter` under ``ColorConverter`` (:issue:`5773`)
- Add alias for :attr:`PublicUserFlags.verified_bot_developer` under :attr:`PublicUserFlags.early_verified_bot_developer` (:issue:`5849`)
- |commands| Add support for ``require_var_positional`` for :class:`Command` (:issue:`5793`)

Bug Fixes
~~~~~~~~~~

- Fix issue with :meth:`Guild.by_category` not showing certain channels.
- Fix :attr:`abc.GuildChannel.permissions_synced` always being ``False`` (:issue:`5772`)
- Fix handling of cloudflare bans on webhook related requests (:issue:`5221`)
- Fix cases where a keep-alive thread would ack despite already dying (:issue:`5800`)
- Fix cases where a :class:`Member` reference would be stale when cache is disabled in message events (:issue:`5819`)
- Fix ``allowed_mentions`` not being sent when sending a single file (:issue:`5835`)
- Fix ``overwrites`` being ignored in :meth:`abc.GuildChannel.edit` if ``{}`` is passed (:issue:`5756`, :issue:`5757`)
- |commands| Fix exceptions being raised improperly in command invoke hooks (:issue:`5799`)
- |commands| Fix commands not being properly ejected during errors in a cog injection (:issue:`5804`)
- |commands| Fix cooldown timing ignoring edited timestamps.
- |tasks| Fix tasks extending the next iteration on handled exceptions (:issue:`5762`, :issue:`5763`)

Miscellaneous
~~~~~~~~~~~~~~~

- Webhook requests are now logged (:issue:`5798`)
- Remove caching layer from :attr:`AutoShardedClient.shards`. This was causing issues if queried before launching shards.
- Gateway rate limits are now handled.
- Warnings logged due to missed caches are now changed to DEBUG log level.
- Some strings are now explicitly interned to reduce memory usage.
- Usage of namedtuples has been reduced to avoid potential breaking changes in the future (:issue:`5834`)
- |commands| All :class:`BadArgument` exceptions from the built-in converters now raise concrete exceptions to better tell them apart (:issue:`5748`)
- |tasks| Lazily fetch the event loop to prevent surprises when changing event loop policy (:issue:`5808`)

.. _vp1p4p2:

v1.4.2
--------

This is a maintenance release with backports from :ref:`vp1p5p0`.

Bug Fixes
~~~~~~~~~~~

- Fix issue with :meth:`Guild.by_category` not showing certain channels.
- Fix :attr:`abc.GuildChannel.permissions_synced` always being ``False`` (:issue:`5772`)
- Fix handling of cloudflare bans on webhook related requests (:issue:`5221`)
- Fix cases where a keep-alive thread would ack despite already dying (:issue:`5800`)
- Fix cases where a :class:`Member` reference would be stale when cache is disabled in message events (:issue:`5819`)
- Fix ``allowed_mentions`` not being sent when sending a single file (:issue:`5835`)
- Fix ``overwrites`` being ignored in :meth:`abc.GuildChannel.edit` if ``{}`` is passed (:issue:`5756`, :issue:`5757`)
- |commands| Fix exceptions being raised improperly in command invoke hooks (:issue:`5799`)
- |commands| Fix commands not being properly ejected during errors in a cog injection (:issue:`5804`)
- |commands| Fix cooldown timing ignoring edited timestamps.
- |tasks| Fix tasks extending the next iteration on handled exceptions (:issue:`5762`, :issue:`5763`)

Miscellaneous
~~~~~~~~~~~~~~~

- Remove caching layer from :attr:`AutoShardedClient.shards`. This was causing issues if queried before launching shards.
- |tasks| Lazily fetch the event loop to prevent surprises when changing event loop policy (:issue:`5808`)

.. _vp1p4p1:

v1.4.1
--------

Bug Fixes
~~~~~~~~~~~

- Properly terminate the connection when :meth:`Client.close` is called (:issue:`5207`)
- Fix error being raised when clearing embed author or image when it was already cleared (:issue:`5210`, :issue:`5212`)
- Fix ``__path__`` to allow editable extensions (:issue:`5213`)

.. _vp1p4p0:

v1.4.0
--------

Another version with a long development time. Features like Intents are slated to be released in a v1.5 release. Thank you for your patience!

New Features
~~~~~~~~~~~~~~

- Add support for :class:`AllowedMentions` to have more control over what gets mentioned.
    - This can be set globally through :attr:`Client.allowed_mentions`
    - This can also be set on a per message basis via :meth:`abc.Messageable.send`

- :class:`AutoShardedClient` has been completely redesigned from the ground up to better suit multi-process clusters (:issue:`2654`)
    - Add :class:`ShardInfo` which allows fetching specific information about a shard.
    - The :class:`ShardInfo` allows for reconnecting and disconnecting of a specific shard as well.
    - Add :meth:`AutoShardedClient.get_shard` and :attr:`AutoShardedClient.shards` to get information about shards.
    - Rework the entire connection flow to better facilitate the ``IDENTIFY`` rate limits.
    - Add a hook :meth:`Client.before_identify_hook` to have better control over what happens before an ``IDENTIFY`` is done.
    - Add more shard related events such as :func:`on_shard_connect`, :func:`on_shard_disconnect` and :func:`on_shard_resumed`.

- Add support for guild templates (:issue:`2652`)
    - This adds :class:`Template` to read a template's information.
    - :meth:`Client.fetch_template` can be used to fetch a template's information from the API.
    - :meth:`Client.create_guild` can now take an optional template to base the creation from.
    - Note that fetching a guild's template is currently restricted for bot accounts.

- Add support for guild integrations (:issue:`2051`, :issue:`1083`)
    - :class:`Integration` is used to read integration information.
    - :class:`IntegrationAccount` is used to read integration account information.
    - :meth:`Guild.integrations` will fetch all integrations in a guild.
    - :meth:`Guild.create_integration` will create an integration.
    - :meth:`Integration.edit` will edit an existing integration.
    - :meth:`Integration.delete` will delete an integration.
    - :meth:`Integration.sync` will sync an integration.
    - There is currently no support in the audit log for this.

- Add an alias for :attr:`VerificationLevel.extreme` under :attr:`VerificationLevel.very_high` (:issue:`2650`)
- Add various grey to gray aliases for :class:`Colour` (:issue:`5130`)
- Added :attr:`VoiceClient.latency` and :attr:`VoiceClient.average_latency` (:issue:`2535`)
- Add ``use_cached`` and ``spoiler`` parameters to :meth:`Attachment.to_file` (:issue:`2577`, :issue:`4095`)
- Add ``position`` parameter support to :meth:`Guild.create_category` (:issue:`2623`)
- Allow passing ``int`` for the colour in :meth:`Role.edit` (:issue:`4057`)
- Add :meth:`Embed.remove_author` to clear author information from an embed (:issue:`4068`)
- Add the ability to clear images and thumbnails in embeds using :attr:`Embed.Empty` (:issue:`4053`)
- Add :attr:`Guild.max_video_channel_users` (:issue:`4120`)
- Add :attr:`Guild.public_updates_channel` (:issue:`4120`)
- Add ``guild_ready_timeout`` parameter to :class:`Client` and subclasses to control timeouts when the ``GUILD_CREATE`` stream takes too long (:issue:`4112`)
- Add support for public user flags via :attr:`User.public_flags` and :class:`PublicUserFlags` (:issue:`3999`)
- Allow changing of channel types via :meth:`TextChannel.edit` to and from a news channel (:issue:`4121`)
- Add :meth:`Guild.edit_role_positions` to bulk edit role positions in a single API call (:issue:`2501`, :issue:`2143`)
- Add :meth:`Guild.change_voice_state` to change your voice state in a guild (:issue:`5088`)
- Add :meth:`PartialInviteGuild.is_icon_animated` for checking if the invite guild has animated icon (:issue:`4180`, :issue:`4181`)
- Add :meth:`PartialInviteGuild.icon_url_as` now supports ``static_format`` for consistency (:issue:`4180`, :issue:`4181`)
- Add support for ``user_ids`` in :meth:`Guild.query_members`
- Add support for pruning members by roles in :meth:`Guild.prune_members` (:issue:`4043`)
- |commands| Implement :func:`~ext.commands.before_invoke` and :func:`~ext.commands.after_invoke` decorators (:issue:`1986`, :issue:`2502`)
- |commands| Add a way to retrieve ``retry_after`` from a cooldown in a command via :meth:`Command.get_cooldown_retry_after <.ext.commands.Command.get_cooldown_retry_after>` (:issue:`5195`)
- |commands| Add a way to dynamically add and remove checks from a :class:`HelpCommand <.ext.commands.HelpCommand>` (:issue:`5197`)
- |tasks| Add :meth:`Loop.is_running <.ext.tasks.Loop.is_running>` method to the task objects (:issue:`2540`)
- |tasks| Allow usage of custom error handlers similar to the command extensions to tasks using :meth:`Loop.error <.ext.tasks.Loop.error>` decorator (:issue:`2621`)


Bug Fixes
~~~~~~~~~~~~

- Fix issue with :attr:`PartialEmoji.url` reads leading to a failure (:issue:`4015`, :issue:`4016`)
- Allow :meth:`abc.Messageable.history` to take a limit of ``1`` even if ``around`` is passed (:issue:`4019`)
- Fix :attr:`Guild.member_count` not updating in certain cases when a member has left the guild (:issue:`4021`)
- Fix the type of :attr:`Object.id` not being validated. For backwards compatibility ``str`` is still allowed but is converted to ``int`` (:issue:`4002`)
- Fix :meth:`Guild.edit` not allowing editing of notification settings (:issue:`4074`, :issue:`4047`)
- Fix crash when the guild widget contains channels that aren't in the payload (:issue:`4114`, :issue:`4115`)
- Close ffmpeg stdin handling from spawned processes with :class:`FFmpegOpusAudio` and :class:`FFmpegPCMAudio` (:issue:`4036`)
- Fix :func:`utils.escape_markdown` not escaping masked links (:issue:`4206`, :issue:`4207`)
- Fix reconnect loop due to failed handshake on region change (:issue:`4210`, :issue:`3996`)
- Fix :meth:`Guild.by_category` not returning empty categories (:issue:`4186`)
- Fix certain JPEG images not being identified as JPEG (:issue:`5143`)
- Fix a crash when an incomplete guild object is used when fetching reaction information (:issue:`5181`)
- Fix a timeout issue when fetching members using :meth:`Guild.query_members`
- Fix an issue with domain resolution in voice (:issue:`5188`, :issue:`5191`)
- Fix an issue where :attr:`PartialEmoji.id` could be a string (:issue:`4153`, :issue:`4152`)
- Fix regression where :attr:`Member.activities` would not clear.
- |commands| A :exc:`TypeError` is now raised when :obj:`typing.Optional` is used within :data:`commands.Greedy <.ext.commands.Greedy>` (:issue:`2253`, :issue:`5068`)
- |commands| :meth:`Bot.walk_commands <.ext.commands.Bot.walk_commands>` no longer yields duplicate commands due to aliases (:issue:`2591`)
- |commands| Fix regex characters not being escaped in :attr:`HelpCommand.clean_prefix <.ext.commands.HelpCommand.clean_prefix>` (:issue:`4058`, :issue:`4071`)
- |commands| Fix :meth:`Bot.get_command <.ext.commands.Bot.get_command>` from raising errors when a name only has whitespace (:issue:`5124`)
- |commands| Fix issue with :attr:`Context.subcommand_passed <.ext.commands.Context.subcommand_passed>` not functioning as expected (:issue:`5198`)
- |tasks| Task objects are no longer stored globally so two class instances can now start two separate tasks (:issue:`2294`)
- |tasks| Allow cancelling the loop within :meth:`before_loop <.ext.tasks.Loop.before_loop>` (:issue:`4082`)


Miscellaneous
~~~~~~~~~~~~~~~

- The :attr:`Member.roles` cache introduced in v1.3 was reverted due to issues caused (:issue:`4087`, :issue:`4157`)
- :class:`Webhook` objects are now comparable and hashable (:issue:`4182`)
- Some more API requests got a ``reason`` parameter for audit logs (:issue:`5086`)
    - :meth:`TextChannel.follow`
    - :meth:`Message.pin` and :meth:`Message.unpin`
    - :meth:`Webhook.delete` and :meth:`Webhook.edit`

- For performance reasons ``websockets`` has been dropped in favour of ``aiohttp.ws``.
- The blocking logging message now shows the stack trace of where the main thread was blocking
- The domain name was changed from ``discordapp.com`` to ``discord.com`` to prepare for the required domain migration
- Reduce memory usage when reconnecting due to stale references being held by the message cache (:issue:`5133`)
- Optimize :meth:`abc.GuildChannel.permissions_for` by not creating as many temporary objects (20-32% savings).
- |commands| Raise :exc:`~ext.commands.CommandRegistrationError` instead of :exc:`ClientException` when a duplicate error is registered (:issue:`4217`)
- |tasks| No longer handle :exc:`HTTPException` by default in the task reconnect loop (:issue:`5193`)

.. _vp1p3p4:

v1.3.4
--------

Bug Fixes
~~~~~~~~~~~

- Fix an issue with channel overwrites causing multiple issues including crashes (:issue:`5109`)

.. _vp1p3p3:

v1.3.3
--------

Bug Fixes
~~~~~~~~~~~~

- Change default WS close to 4000 instead of 1000.
    - The previous close code caused sessions to be invalidated at a higher frequency than desired.

- Fix ``None`` appearing in ``Member.activities``. (:issue:`2619`)

.. _vp1p3p2:

v1.3.2
---------

Another minor bug fix release.

Bug Fixes
~~~~~~~~~~~

- Higher the wait time during the ``GUILD_CREATE`` stream before ``on_ready`` is fired for :class:`AutoShardedClient`.
- :func:`on_voice_state_update` now uses the inner ``member`` payload which should make it more reliable.
- Fix various Cloudflare handling errors (:issue:`2572`, :issue:`2544`)
- Fix crashes if :attr:`Message.guild` is :class:`Object` instead of :class:`Guild`.
- Fix :meth:`Webhook.send` returning an empty string instead of ``None`` when ``wait=False``.
- Fix invalid format specifier in webhook state (:issue:`2570`)
- |commands| Passing invalid permissions to permission related checks now raises ``TypeError``.

.. _vp1p3p1:

v1.3.1
--------

Minor bug fix release.

Bug Fixes
~~~~~~~~~~~

- Fix fetching invites in guilds that the user is not in.
- Fix the channel returned from :meth:`Client.fetch_channel` raising when sending messages. (:issue:`2531`)

Miscellaneous
~~~~~~~~~~~~~~

- Fix compatibility warnings when using the Python 3.9 alpha.
- Change the unknown event logging from WARNING to DEBUG to reduce noise.

.. _vp1p3p0:

v1.3.0
--------

This version comes with a lot of bug fixes and new features. It's been in development for a lot longer than was anticipated!

New Features
~~~~~~~~~~~~~~

- Add :meth:`Guild.fetch_members` to fetch members from the HTTP API. (:issue:`2204`)
- Add :meth:`Guild.fetch_roles` to fetch roles from the HTTP API. (:issue:`2208`)
- Add support for teams via :class:`Team` when fetching with :meth:`Client.application_info`. (:issue:`2239`)
- Add support for suppressing embeds via :meth:`Message.edit`
- Add support for guild subscriptions. See the :class:`Client` documentation for more details.
- Add :attr:`VoiceChannel.voice_states` to get voice states without relying on member cache.
- Add :meth:`Guild.query_members` to request members from the gateway.
- Add :class:`FFmpegOpusAudio` and other voice improvements. (:issue:`2258`)
- Add :attr:`RawMessageUpdateEvent.channel_id` for retrieving channel IDs during raw message updates. (:issue:`2301`)
- Add :attr:`RawReactionActionEvent.event_type` to disambiguate between reaction addition and removal in reaction events.
- Add :attr:`abc.GuildChannel.permissions_synced` to query whether permissions are synced with the category. (:issue:`2300`, :issue:`2324`)
- Add :attr:`MessageType.channel_follow_add` message type for announcement channels being followed. (:issue:`2314`)
- Add :meth:`Message.is_system` to allow for quickly filtering through system messages.
- Add :attr:`VoiceState.self_stream` to indicate whether someone is streaming via Go Live. (:issue:`2343`)
- Add :meth:`Emoji.is_usable` to check if the client user can use an emoji. (:issue:`2349`)
- Add :attr:`VoiceRegion.europe` and :attr:`VoiceRegion.dubai`. (:issue:`2358`, :issue:`2490`)
- Add :meth:`TextChannel.follow` to follow a news channel. (:issue:`2367`)
- Add :attr:`Permissions.view_guild_insights` permission. (:issue:`2415`)
- Add support for new audit log types. See :ref:`discord-api-audit-logs` for more information. (:issue:`2427`)
    - Note that integration support is not finalized.

- Add :attr:`Webhook.type` to query the type of webhook (:class:`WebhookType`). (:issue:`2441`)
- Allow bulk editing of channel overwrites through :meth:`abc.GuildChannel.edit`. (:issue:`2198`)
- Add :class:`Activity.created_at` to see when an activity was started. (:issue:`2446`)
- Add support for ``xsalsa20_poly1305_lite`` encryption mode for voice. (:issue:`2463`)
- Add :attr:`RawReactionActionEvent.member` to get the member who did the reaction. (:issue:`2443`)
- Add support for new YouTube streaming via :attr:`Streaming.platform` and :attr:`Streaming.game`. (:issue:`2445`)
- Add :attr:`Guild.discovery_splash_url` to get the discovery splash image asset. (:issue:`2482`)
- Add :attr:`Guild.rules_channel` to get the rules channel of public guilds. (:issue:`2482`)
    - It should be noted that this feature is restricted to those who are either in Server Discovery or planning to be there.

- Add support for message flags via :attr:`Message.flags` and :class:`MessageFlags`. (:issue:`2433`)
- Add :attr:`User.system` and :attr:`Profile.system` to know whether a user is an official Discord Trust and Safety account.
- Add :attr:`Profile.team_user` to check whether a user is a member of a team.
- Add :meth:`Attachment.to_file` to easily convert attachments to :class:`File` for sending.
- Add certain aliases to :class:`Permissions` to match the UI better. (:issue:`2496`)
    - :attr:`Permissions.manage_permissions`
    - :attr:`Permissions.view_channel`
    - :attr:`Permissions.use_external_emojis`

- Add support for passing keyword arguments when creating :class:`Permissions`.
- Add support for custom activities via :class:`CustomActivity`. (:issue:`2400`)
    - Note that as of now, bots cannot send custom activities yet.

- Add support for :func:`on_invite_create` and :func:`on_invite_delete` events.
- Add support for clearing a specific reaction emoji from a message.
    - :meth:`Message.clear_reaction` and :meth:`Reaction.clear` methods.
    - :func:`on_raw_reaction_clear_emoji` and :func:`on_reaction_clear_emoji` events.

- Add :func:`utils.sleep_until` helper to sleep until a specific datetime. (:issue:`2517`, :issue:`2519`)
- |commands| Add support for teams and :attr:`Bot.owner_ids <.ext.commands.Bot.owner_ids>` to have multiple bot owners. (:issue:`2239`)
- |commands| Add new :attr:`BucketType.role <.ext.commands.BucketType.role>` bucket type. (:issue:`2201`)
- |commands| Expose :attr:`Command.cog <.ext.commands.Command.cog>` property publicly. (:issue:`2360`)
- |commands| Add non-decorator interface for adding checks to commands via :meth:`Command.add_check <.ext.commands.Command.add_check>` and :meth:`Command.remove_check <.ext.commands.Command.remove_check>`. (:issue:`2411`)
- |commands| Add :func:`has_guild_permissions <.ext.commands.has_guild_permissions>` check. (:issue:`2460`)
- |commands| Add :func:`bot_has_guild_permissions <.ext.commands.bot_has_guild_permissions>` check. (:issue:`2460`)
- |commands| Add ``predicate`` attribute to checks decorated with :func:`~.ext.commands.check`.
- |commands| Add :func:`~.ext.commands.check_any` check to logical OR multiple checks.
- |commands| Add :func:`~.ext.commands.max_concurrency` to allow only a certain amount of users to use a command concurrently before waiting or erroring.
- |commands| Add support for calling a :class:`~.ext.commands.Command` as a regular function.
- |tasks| :meth:`Loop.add_exception_type <.ext.tasks.Loop.add_exception_type>` now allows multiple exceptions to be set. (:issue:`2333`)
- |tasks| Add :attr:`Loop.next_iteration <.ext.tasks.Loop.next_iteration>` property. (:issue:`2305`)

Bug Fixes
~~~~~~~~~~

- Fix issue with permission resolution sometimes failing for guilds with no owner.
- Tokens are now stripped upon use. (:issue:`2135`)
- Passing in a ``name`` is no longer required for :meth:`Emoji.edit`. (:issue:`2368`)
- Fix issue with webhooks not re-raising after retries have run out. (:issue:`2272`, :issue:`2380`)
- Fix mismatch in URL handling in :func:`utils.escape_markdown`. (:issue:`2420`)
- Fix issue with ports being read in little endian when they should be big endian in voice connections. (:issue:`2470`)
- Fix :meth:`Member.mentioned_in` not taking into consideration the message's guild.
- Fix bug with moving channels when there are gaps in positions due to channel deletion and creation.
- Fix :func:`on_shard_ready` not triggering when ``fetch_offline_members`` is disabled. (:issue:`2504`)
- Fix issue with large sharded bots taking too long to actually dispatch :func:`on_ready`.
- Fix issue with fetching group DM based invites in :meth:`Client.fetch_invite`.
- Fix out of order files being sent in webhooks when there are 10 files.
- |commands| Extensions that fail internally due to ImportError will no longer raise :exc:`~.ext.commands.ExtensionNotFound`. (:issue:`2244`, :issue:`2275`, :issue:`2291`)
- |commands| Updating the :attr:`Paginator.suffix <.ext.commands.Paginator.suffix>` will not cause out of date calculations. (:issue:`2251`)
- |commands| Allow converters from custom extension packages. (:issue:`2369`, :issue:`2374`)
- |commands| Fix issue with paginator prefix being ``None`` causing empty pages. (:issue:`2471`)
- |commands| :class:`~.commands.Greedy` now ignores parsing errors rather than propagating them.
- |commands| :meth:`Command.can_run <.ext.commands.Command.can_run>` now checks whether a command is disabled.
- |commands| :attr:`HelpCommand.clean_prefix <.ext.commands.HelpCommand.clean_prefix>` now takes into consideration nickname mentions. (:issue:`2489`)
- |commands| :meth:`Context.send_help <.ext.commands.Context.send_help>` now properly propagates to the :meth:`HelpCommand.on_help_command_error <.ext.commands.HelpCommand.on_help_command_error>` handler.

Miscellaneous
~~~~~~~~~~~~~~~

- The library now fully supports Python 3.8 without warnings.
- Bump the dependency of ``websockets`` to 8.0 for those who can use it. (:issue:`2453`)
- Due to Discord providing :class:`Member` data in mentions, users will now be upgraded to :class:`Member` more often if mentioned.
- :func:`utils.escape_markdown` now properly escapes new quote markdown.
- The message cache can now be disabled by passing ``None`` to ``max_messages`` in :class:`Client`.
- The default message cache size has changed from 5000 to 1000 to accommodate small bots.
- Lower memory usage by only creating certain objects as needed in :class:`Role`.
- There is now a sleep of 5 seconds before re-IDENTIFYing during a reconnect to prevent long loops of session invalidation.
- The rate limiting code now uses millisecond precision to have more granular rate limit handling.
    - Along with that, the rate limiting code now uses Discord's response to wait. If you need to use the system clock again for whatever reason, consider passing ``assume_synced_clock`` in :class:`Client`.

- The performance of :attr:`Guild.default_role` has been improved from O(N) to O(1). (:issue:`2375`)
- The performance of :attr:`Member.roles` has improved due to usage of caching to avoid surprising performance traps.
- The GC is manually triggered during things that cause large deallocations (such as guild removal) to prevent memory fragmentation.
- There have been many changes to the documentation for fixes both for usability, correctness, and to fix some linter errors. Thanks to everyone who contributed to those.
- The loading of the opus module has been delayed which would make the result of :func:`opus.is_loaded` somewhat surprising.
- |commands| Usernames prefixed with @ inside DMs will properly convert using the :class:`User` converter. (:issue:`2498`)
- |tasks| The task sleeping time will now take into consideration the amount of time the task body has taken before sleeping. (:issue:`2516`)

.. _vp1p2p5:

v1.2.5
--------

Bug Fixes
~~~~~~~~~~~

- Fix a bug that caused crashes due to missing ``animated`` field in Emoji structures in reactions.

.. _vp1p2p4:

v1.2.4
--------

Bug Fixes
~~~~~~~~~~~

- Fix a regression when :attr:`Message.channel` would be ``None``.
- Fix a regression where :attr:`Message.edited_at` would not update during edits.
- Fix a crash that would trigger during message updates (:issue:`2265`, :issue:`2287`).
- Fix a bug when :meth:`VoiceChannel.connect` would not return (:issue:`2274`, :issue:`2372`, :issue:`2373`, :issue:`2377`).
- Fix a crash relating to token-less webhooks (:issue:`2364`).
- Fix issue where :attr:`Guild.premium_subscription_count` would be ``None`` due to a Discord bug. (:issue:`2331`, :issue:`2376`).

.. _vp1p2p3:

v1.2.3
--------

Bug Fixes
~~~~~~~~~~~

- Fix an AttributeError when accessing :attr:`Member.premium_since` in :func:`on_member_update`. (:issue:`2213`)
- Handle :exc:`asyncio.CancelledError` in :meth:`abc.Messageable.typing` context manager. (:issue:`2218`)
- Raise the max encoder bitrate to 512kbps to account for nitro boosting. (:issue:`2232`)
- Properly propagate exceptions in :meth:`Client.run`. (:issue:`2237`)
- |commands| Ensure cooldowns are properly copied when used in cog level ``command_attrs``.

.. _vp1p2p2:

v1.2.2
--------

Bug Fixes
~~~~~~~~~~~

- Audit log related attribute access have been fixed to not error out when they shouldn't have.

.. _vp1p2p1:

v1.2.1
--------

Bug Fixes
~~~~~~~~~~~

- :attr:`User.avatar_url` and related attributes no longer raise an error.
- More compatibility shims with the ``enum.Enum`` code.

.. _vp1p2p0:

v1.2.0
--------

This update mainly brings performance improvements and various nitro boosting attributes (referred to in the API as "premium guilds").

New Features
~~~~~~~~~~~~~~

- Add :attr:`Guild.premium_tier` to query the guild's current nitro boost level.
- Add :attr:`Guild.emoji_limit`, :attr:`Guild.bitrate_limit`, :attr:`Guild.filesize_limit` to query the new limits of a guild when taking into consideration boosting.
- Add :attr:`Guild.premium_subscription_count` to query how many members are boosting a guild.
- Add :attr:`Member.premium_since` to query since when a member has boosted a guild.
- Add :attr:`Guild.premium_subscribers` to query all the members currently boosting the guild.
- Add :attr:`Guild.system_channel_flags` to query the settings for a guild's :attr:`Guild.system_channel`.
    - This includes a new type named :class:`SystemChannelFlags`
- Add :attr:`Emoji.available` to query if an emoji can be used (within the guild or otherwise).
- Add support for animated icons in :meth:`Guild.icon_url_as` and :attr:`Guild.icon_url`.
- Add :meth:`Guild.is_icon_animated`.
- Add support for the various new :class:`MessageType` involving nitro boosting.
- Add :attr:`VoiceRegion.india`. (:issue:`2145`)
- Add :meth:`Embed.insert_field_at`. (:issue:`2178`)
- Add a ``type`` attribute for all channels to their appropriate :class:`ChannelType`. (:issue:`2185`)
- Add :meth:`Client.fetch_channel` to fetch a channel by ID via HTTP. (:issue:`2169`)
- Add :meth:`Guild.fetch_channels` to fetch all channels via HTTP. (:issue:`2169`)
- |tasks| Add :meth:`Loop.stop <.ext.tasks.Loop.stop>` to gracefully stop a task rather than cancelling.
- |tasks| Add :meth:`Loop.failed <.ext.tasks.Loop.failed>` to query if a task had failed somehow.
- |tasks| Add :meth:`Loop.change_interval <.ext.tasks.Loop.change_interval>` to change the sleep interval at runtime (:issue:`2158`, :issue:`2162`)

Bug Fixes
~~~~~~~~~~~

- Fix internal error when using :meth:`Guild.prune_members`.
- |commands| Fix :attr:`.Command.invoked_subcommand` being invalid in many cases.
- |tasks| Reset iteration count when the loop terminates and is restarted.
- |tasks| The decorator interface now works as expected when stacking (:issue:`2154`)

Miscellaneous
~~~~~~~~~~~~~~~

- Improve performance of all Enum related code significantly.
    - This was done by replacing the ``enum.Enum`` code with an API compatible one.
    - This should not be a breaking change for most users due to duck-typing.
- Improve performance of message creation by about 1.5x.
- Improve performance of message editing by about 1.5-4x depending on payload size.
- Improve performance of attribute access on :class:`Member` about by 2x.
- Improve performance of :func:`utils.get` by around 4-6x depending on usage.
- Improve performance of event parsing lookup by around 2.5x.
- Keyword arguments in :meth:`Client.start` and :meth:`Client.run` are now validated (:issue:`953`, :issue:`2170`)
- The Discord error code is now shown in the exception message for :exc:`HTTPException`.
- Internal tasks launched by the library will now have their own custom ``__repr__``.
- All public facing types should now have a proper and more detailed ``__repr__``.
- |tasks| Errors are now logged via the standard :mod:`py:logging` module.

.. _vp1p1p1:

v1.1.1
--------

Bug Fixes
~~~~~~~~~~~~

- Webhooks do not overwrite data on retrying their HTTP requests (:issue:`2140`)

Miscellaneous
~~~~~~~~~~~~~~

- Add back signal handling to :meth:`Client.run` due to issues some users had with proper cleanup.

.. _vp1p1p0:

v1.1.0
---------

New Features
~~~~~~~~~~~~~~

- **There is a new extension dedicated to making background tasks easier.**
    - You can check the documentation here: :ref:`ext_tasks_api`.
- Add :attr:`Permissions.stream` permission. (:issue:`2077`)
- Add equality comparison and hash support to :class:`Asset`
- Add ``compute_prune_members`` parameter to :meth:`Guild.prune_members` (:issue:`2085`)
- Add :attr:`Client.cached_messages` attribute to fetch the message cache (:issue:`2086`)
- Add :meth:`abc.GuildChannel.clone` to clone a guild channel. (:issue:`2093`)
- Add ``delay`` keyword-only argument to :meth:`Message.delete` (:issue:`2094`)
- Add support for ``<:name:id>`` when adding reactions (:issue:`2095`)
- Add :meth:`Asset.read` to fetch the bytes content of an asset (:issue:`2107`)
- Add :meth:`Attachment.read` to fetch the bytes content of an attachment (:issue:`2118`)
- Add support for voice kicking by passing ``None`` to :meth:`Member.move_to`.

``discord.ext.commands``
++++++++++++++++++++++++++

- Add new :func:`~.commands.dm_only` check.
- Support callable converters in :data:`~.commands.Greedy`
- Add new :class:`~.commands.MessageConverter`.
    - This allows you to use :class:`Message` as a type hint in functions.
- Allow passing ``cls`` in the :func:`~.commands.group` decorator (:issue:`2061`)
- Add :attr:`.Command.parents` to fetch the parents of a command (:issue:`2104`)


Bug Fixes
~~~~~~~~~~~~

- Fix :exc:`AttributeError` when using ``__repr__`` on :class:`Widget`.
- Fix issue with :attr:`abc.GuildChannel.overwrites` returning ``None`` for keys.
- Remove incorrect legacy NSFW checks in e.g. :meth:`TextChannel.is_nsfw`.
- Fix :exc:`UnboundLocalError` when :class:`RequestsWebhookAdapter` raises an error.
- Fix bug where updating your own user did not update your member instances.
- Tighten constraints of ``__eq__`` in :class:`Spotify` objects (:issue:`2113`, :issue:`2117`)

``discord.ext.commands``
++++++++++++++++++++++++++

- Fix lambda converters in a non-module context (e.g. ``eval``).
- Use message creation time for reference time when computing cooldowns.
    - This prevents cooldowns from triggering during e.g. a RESUME session.
- Fix the default :func:`on_command_error` to work with new-style cogs (:issue:`2094`)
- DM channels are now recognised as NSFW in :func:`~.commands.is_nsfw` check.
- Fix race condition with help commands (:issue:`2123`)
- Fix cog descriptions not showing in :class:`~.commands.MinimalHelpCommand` (:issue:`2139`)

Miscellaneous
~~~~~~~~~~~~~~~

- Improve the performance of internal enum creation in the library by about 5x.
- Make the output of ``python -m discord --version`` a bit more useful.
- The loop cleanup facility has been rewritten again.
- The signal handling in :meth:`Client.run` has been removed.

``discord.ext.commands``
++++++++++++++++++++++++++

- Custom exception classes are now used for all default checks in the library (:issue:`2101`)


.. _vp1p0p1:

v1.0.1
--------

Bug Fixes
~~~~~~~~~~~

- Fix issue with speaking state being cast to ``int`` when it was invalid.
- Fix some issues with loop cleanup that some users experienced on Linux machines.
- Fix voice handshake race condition (:issue:`2056`, :issue:`2063`)

.. _vp1p0p0:

v1.0.0
--------

The changeset for this version are too big to be listed here, for more information please
see :ref:`the migrating page <migrating_1_0>`.


.. _vp0p16p6:

v0.16.6
--------

Bug Fixes
~~~~~~~~~~

- Fix issue with :meth:`Client.create_server` that made it stop working.
- Fix main thread being blocked upon calling ``StreamPlayer.stop``.
- Handle HEARTBEAT_ACK and resume gracefully when it occurs.
- Fix race condition when pre-emptively rate limiting that caused releasing an already released lock.
- Fix invalid state errors when immediately cancelling a coroutine.

.. _vp0p16p1:

v0.16.1
--------

This release is just a bug fix release with some better rate limit implementation.

Bug Fixes
~~~~~~~~~~~

- Servers are now properly chunked for user bots.
- The CDN URL is now used instead of the API URL for assets.
- Rate limit implementation now tries to use header information if possible.
- Event loop is now properly propagated (:issue:`420`)
- Allow falsey values in :meth:`Client.send_message` and :meth:`Client.send_file`.

.. _vp0p16p0:

v0.16.0
---------

New Features
~~~~~~~~~~~~~~

- Add :attr:`Channel.overwrites` to get all the permission overwrites of a channel.
- Add :attr:`Server.features` to get information about partnered servers.

Bug Fixes
~~~~~~~~~~

- Timeout when waiting for offline members while triggering :func:`on_ready`.

    - The fact that we did not timeout caused a gigantic memory leak in the library that caused
      thousands of duplicate :class:`Member` instances causing big memory spikes.

- Discard null sequences in the gateway.

    - The fact these were not discarded meant that :func:`on_ready` kept being called instead of
      :func:`on_resumed`. Since this has been corrected, in most cases :func:`on_ready` will be
      called once or twice with :func:`on_resumed` being called much more often.

.. _vp0p15p1:

v0.15.1
---------

- Fix crash on duplicate or out of order reactions.

.. _vp0p15p0:

v0.15.0
--------

New Features
~~~~~~~~~~~~~~

- Rich Embeds for messages are now supported.

    - To do so, create your own :class:`Embed` and pass the instance to the ``embed`` keyword argument to :meth:`Client.send_message` or :meth:`Client.edit_message`.
- Add :meth:`Client.clear_reactions` to remove all reactions from a message.
- Add support for MESSAGE_REACTION_REMOVE_ALL event, under :func:`on_reaction_clear`.
- Add :meth:`Permissions.update` and :meth:`PermissionOverwrite.update` for bulk permission updates.

    - This allows you to use e.g. ``p.update(read_messages=True, send_messages=False)`` in a single line.
- Add :meth:`PermissionOverwrite.is_empty` to check if the overwrite is empty (i.e. has no overwrites set explicitly as true or false).

For the command extension, the following changed:

- ``Context`` is no longer slotted to facilitate setting dynamic attributes.

.. _vp0p14p3:

v0.14.3
---------

Bug Fixes
~~~~~~~~~~~

- Fix crash when dealing with MESSAGE_REACTION_REMOVE
- Fix incorrect buckets for reactions.

.. _v0p14p2:

v0.14.2
---------

New Features
~~~~~~~~~~~~~~

- :meth:`Client.wait_for_reaction` now returns a namedtuple with ``reaction`` and ``user`` attributes.
    - This is for better support in the case that ``None`` is returned since tuple unpacking can lead to issues.

Bug Fixes
~~~~~~~~~~

- Fix bug that disallowed ``None`` to be passed for ``emoji`` parameter in :meth:`Client.wait_for_reaction`.

.. _v0p14p1:

v0.14.1
---------

Bug fixes
~~~~~~~~~~

- Fix bug with ``Reaction`` not being visible at import.
    - This was also breaking the documentation.

.. _v0p14p0:

v0.14.0
--------

This update adds new API features and a couple of bug fixes.

New Features
~~~~~~~~~~~~~

- Add support for Manage Webhooks permission under :attr:`Permissions.manage_webhooks`
- Add support for ``around`` argument in 3.5+ :meth:`Client.logs_from`.
- Add support for reactions.
    - :meth:`Client.add_reaction` to add a reactions
    - :meth:`Client.remove_reaction` to remove a reaction.
    - :meth:`Client.get_reaction_users` to get the users that reacted to a message.
    - :attr:`Permissions.add_reactions` permission bit support.
    - Two new events, :func:`on_reaction_add` and :func:`on_reaction_remove`.
    - :attr:`Message.reactions` to get reactions from a message.
    - :meth:`Client.wait_for_reaction` to wait for a reaction from a user.

Bug Fixes
~~~~~~~~~~

- Fix bug with Paginator still allowing lines that are too long.
- Fix the :attr:`Permissions.manage_emojis` bit being incorrect.

.. _v0p13p0:

v0.13.0
---------

This is a backwards compatible update with new features.

New Features
~~~~~~~~~~~~~

- Add the ability to manage emojis.

    - :meth:`Client.create_custom_emoji` to create new emoji.
    - :meth:`Client.edit_custom_emoji` to edit an old emoji.
    - :meth:`Client.delete_custom_emoji` to delete a custom emoji.
- Add new :attr:`Permissions.manage_emojis` toggle.

    - This applies for :class:`PermissionOverwrite` as well.
- Add new statuses for :class:`Status`.

    - :attr:`Status.dnd` (aliased with :attr:`Status.do_not_disturb`\) for Do Not Disturb.
    - :attr:`Status.invisible` for setting your status to invisible (please see the docs for a caveat).
- Deprecate :meth:`Client.change_status`

    - Use :meth:`Client.change_presence` instead for better more up to date functionality.
    - This method is subject for removal in a future API version.
- Add :meth:`Client.change_presence` for changing your status with the new Discord API change.

    - This is the only method that allows changing your status to invisible or do not disturb.

Bug Fixes
~~~~~~~~~~

- Paginator pages do not exceed their max_size anymore (:issue:`340`)
- Do Not Disturb users no longer show up offline due to the new :class:`Status` changes.

.. _v0p12p0:

v0.12.0
---------

This is a bug fix update that also comes with new features.

New Features
~~~~~~~~~~~~~

- Add custom emoji support.

    - Adds a new class to represent a custom Emoji named :class:`Emoji`
    - Adds a utility generator function, :meth:`Client.get_all_emojis`.
    - Adds a list of emojis on a server, :attr:`Server.emojis`.
    - Adds a new event, :func:`on_server_emojis_update`.
- Add new server regions to :class:`ServerRegion`

    - :attr:`ServerRegion.eu_central` and :attr:`ServerRegion.eu_west`.
- Add support for new pinned system message under :attr:`MessageType.pins_add`.
- Add order comparisons for :class:`Role` to allow it to be compared with regards to hierarchy.

    - This means that you can now do ``role_a > role_b`` etc to check if ``role_b`` is lower in the hierarchy.

- Add :attr:`Server.role_hierarchy` to get the server's role hierarchy.
- Add :attr:`Member.server_permissions` to get a member's server permissions without their channel specific overwrites.
- Add :meth:`Client.get_user_info` to retrieve a user's info from their ID.
- Add a new ``Player`` property, ``Player.error`` to fetch the error that stopped the player.

    - To help with this change, a player's ``after`` function can now take a single parameter denoting the current player.
- Add support for server verification levels.

    - Adds a new enum called :class:`VerificationLevel`.
    - This enum can be used in :meth:`Client.edit_server` under the ``verification_level`` keyword argument.
    - Adds a new attribute in the server, :attr:`Server.verification_level`.
- Add :attr:`Server.voice_client` shortcut property for :meth:`Client.voice_client_in`.

    - This is technically old (was added in v0.10.0) but was undocumented until v0.12.0.

For the command extension, the following are new:

- Add custom emoji converter.
- All default converters that can take IDs can now convert via ID.
- Add coroutine support for ``Bot.command_prefix``.
- Add a method to reset command cooldown.

Bug Fixes
~~~~~~~~~~

- Fix bug that caused the library to not work with the latest ``websockets`` library.
- Fix bug that leaked keep alive threads (:issue:`309`)
- Fix bug that disallowed :class:`ServerRegion` from being used in :meth:`Client.edit_server`.
- Fix bug in :meth:`Channel.permissions_for` that caused permission resolution to happen out of order.
- Fix bug in :attr:`Member.top_role` that did not account for same-position roles.

.. _v0p11p0:

v0.11.0
--------

This is a minor bug fix update that comes with a gateway update (v5 -> v6).

Breaking Changes
~~~~~~~~~~~~~~~~~

- ``Permissions.change_nicknames`` has been renamed to :attr:`Permissions.change_nickname` to match the UI.

New Features
~~~~~~~~~~~~~

- Add the ability to prune members via :meth:`Client.prune_members`.
- Switch the websocket gateway version to v6 from v5. This allows the library to work with group DMs and 1-on-1 calls.
- Add :attr:`AppInfo.owner` attribute.
- Add :class:`CallMessage` for group voice call messages.
- Add :class:`GroupCall` for group voice call information.
- Add :attr:`Message.system_content` to get the system message.
- Add the remaining VIP servers and the Brazil servers into :class:`ServerRegion` enum.
- Add ``stderr`` argument to :meth:`VoiceClient.create_ffmpeg_player` to redirect stderr.
- The library now handles implicit permission resolution in :meth:`Channel.permissions_for`.
- Add :attr:`Server.mfa_level` to query a server's 2FA requirement.
- Add :attr:`Permissions.external_emojis` permission.
- Add :attr:`Member.voice` attribute that refers to a :class:`VoiceState`.

    - For backwards compatibility, the member object will have properties mirroring the old behaviour.

For the command extension, the following are new:

- Command cooldown system with the ``cooldown`` decorator.
- ``UserInputError`` exception for the hierarchy for user input related errors.

Bug Fixes
~~~~~~~~~~

- :attr:`Client.email` is now saved when using a token for user accounts.
- Fix issue when removing roles out of order.
- Fix bug where discriminators would not update.
- Handle cases where ``HEARTBEAT`` opcode is received. This caused bots to disconnect seemingly randomly.

For the command extension, the following bug fixes apply:

- ``Bot.check`` decorator is actually a decorator not requiring parentheses.
- ``Bot.remove_command`` and ``Group.remove_command`` no longer throw if the command doesn't exist.
- Command names are no longer forced to be ``lower()``.
- Fix a bug where Member and User converters failed to work in private message contexts.
- ``HelpFormatter`` now ignores hidden commands when deciding the maximum width.

.. _v0p10p0:

v0.10.0
-------

For breaking changes, see :ref:`migrating-to-async`. The breaking changes listed there will not be enumerated below. Since this version is rather a big departure from v0.9.2, this change log will be non-exhaustive.

New Features
~~~~~~~~~~~~~

- The library is now fully ``asyncio`` compatible, allowing you to write non-blocking code a lot more easily.
- The library now fully handles 429s and unconditionally retries on 502s.
- A new command extension module was added but is currently undocumented. Figuring it out is left as an exercise to the reader.
- Two new exception types, :exc:`Forbidden` and :exc:`NotFound` to denote permission errors or 404 errors.
- Added :meth:`Client.delete_invite` to revoke invites.
- Added support for sending voice. Check :class:`VoiceClient` for more details.
- Added :meth:`Client.wait_for_message` coroutine to aid with follow up commands.
- Added :data:`version_info` named tuple to check version info of the library.
- Login credentials are now cached to have a faster login experience. You can disable this by passing in ``cache_auth=False``
  when constructing a :class:`Client`.
- New utility function, :func:`discord.utils.get` to simplify retrieval of items based on attributes.
- All data classes now support ``!=``, ``==``, ``hash(obj)`` and ``str(obj)``.
- Added :meth:`Client.get_bans` to get banned members from a server.
- Added :meth:`Client.invites_from` to get currently active invites in a server.
- Added :attr:`Server.me` attribute to get the :class:`Member` version of :attr:`Client.user`.
- Most data classes now support a ``hash(obj)`` function to allow you to use them in ``set`` or ``dict`` classes or subclasses.
- Add :meth:`Message.clean_content` to get a text version of the content with the user and channel mentioned changed into their names.
- Added a way to remove the messages of the user that just got banned in :meth:`Client.ban`.
- Added :meth:`Client.wait_until_ready` to facilitate easy creation of tasks that require the client cache to be ready.
- Added :meth:`Client.wait_until_login` to facilitate easy creation of tasks that require the client to be logged in.
- Add :class:`discord.Game` to represent any game with custom text to send to :meth:`Client.change_status`.
- Add :attr:`Message.nonce` attribute.
- Add :meth:`Member.permissions_in` as another way of doing :meth:`Channel.permissions_for`.
- Add :meth:`Client.move_member` to move a member to another voice channel.
- You can now create a server via :meth:`Client.create_server`.
- Added :meth:`Client.edit_server` to edit existing servers.
- Added :meth:`Client.server_voice_state` to server mute or server deafen a member.
- If you are being rate limited, the library will now handle it for you.
- Add :func:`on_member_ban` and :func:`on_member_unban` events that trigger when a member is banned/unbanned.

Performance Improvements
~~~~~~~~~~~~~~~~~~~~~~~~~

- All data classes now use ``__slots__`` which greatly reduce the memory usage of things kept in cache.
- Due to the usage of ``asyncio``, the CPU usage of the library has gone down significantly.
- A lot of the internal cache lists were changed into dictionaries to change the ``O(n)`` lookup into ``O(1)``.
- Compressed READY is now on by default. This means if you're on a lot of servers (or maybe even a few) you would
  receive performance improvements by having to download and process less data.
- While minor, change regex from ``\d+`` to ``[0-9]+`` to avoid unnecessary unicode character lookups.

Bug Fixes
~~~~~~~~~~

- Fix bug where guilds being updated did not edit the items in cache.
- Fix bug where ``member.roles`` were empty upon joining instead of having the ``@everyone`` role.
- Fix bug where :meth:`Role.is_everyone` was not being set properly when the role was being edited.
- :meth:`Client.logs_from` now handles cases where limit > 100 to sidestep the discord API limitation.
- Fix bug where a role being deleted would trigger a ``ValueError``.
- Fix bug where :meth:`Permissions.kick_members` and :meth:`Permissions.ban_members` were flipped.
- Mentions are now triggered normally. This was changed due to the way discord handles it internally.
- Fix issue when a :class:`Message` would attempt to upgrade a :attr:`Message.server` when the channel is
  a :class:`Object`.
- Unavailable servers were not being added into cache, this has been corrected.



.. tip::
   Eu vendo que ainda falta 900 linhas ora traduzir 😫