:orphan:

.. _discord-intro:

Criando a Conta do bOT no Portal do Desenvolvedor
========================

Para trabalhar com a biblioteca e a API do Discord em geral, primeiro precisamos criar uma conta de Bot no Discord.

Criar uma conta de Bot é um processo bastante simples.

1. Certifique-se de que está logado no `site do Discord <https://discord.com>`_.
2. Navegue até a `página de aplicações <https://discord.com/developers/applications>`_
3. Clique no botão "Nova Aplicação".

    .. image:: /images/discord_create_app_button.png
        :alt: O botão de nova aplicação.

4. Dê um nome à aplicação e clique em "Criar".

    .. image:: /images/discord_create_app_form.png
        :alt: O formulário da nova aplicação preenchido.

5. Navegue até a aba "Bot" para configurá-la.
6. Certifique-se de que **Bot Público** está marcado se você quiser que outros possam adicionar seu bot.

    - Também é recomendável que **Require OAuth2 Code Grant** não esteja marcado, a menos que você esteja desenvolvendo um serviço que precise disso. Se não tiver certeza, **deixe desmarcado**.

    .. image:: /images/discord_bot_user_options.png
        :alt: Como as opções do Bot User devem parecer para a maioria das pessoas.

7. Copie o token usando o botão "Copiar".

    - **Isso não é o Client Secret que aparece na página de Informações Gerais.**

    .. warning::

        Vale notar que este token é essencialmente a senha do seu bot. Você **nunca** deve compartilhá-lo com outra pessoa. Ao fazer isso, alguém poderia entrar no seu bot e executar ações maliciosas, como sair de servidores, banir todos os membros de um servidor ou marcar todos de forma maliciosa.

        As possibilidades são infinitas, então **não compartilhe este token.**

        Se você vazou o token acidentalmente, clique no botão "Regenerate" o quanto antes. Isso revoga o token antigo e gera um novo.
        Agora você precisará usar o novo token para fazer login.

E é isso. Agora você tem uma conta de bot e pode fazer login com esse token.

.. _discord_invite_bot:

Convidando Seu Bot
-------------------

Então você criou um Bot User, mas ele ainda não está em nenhum servidor.

Se você quiser convidar seu bot, deve criar uma URL de convite para ele.

1. Certifique-se de que está logado no `site do Discord <https://discord.com>`_.
2. Navegue até a `página de aplicações <https://discord.com/developers/applications>`_
3. Clique na página do seu bot.
4. Vá para a aba "OAuth2 > Gerador de URL".

    .. image:: /images/discord_oauth2.png
        :alt: Como a página OAuth2 deve parecer.

5. Marque a caixa "bot" em "scopes".

    .. image:: /images/discord_oauth2_scope.png
        :alt: A caixa de escopos com "bot" marcada.

6. Marque as permissões necessárias para o funcionamento do seu bot em "Permissões do Bot".

    - Esteja ciente das consequências de conceder a permissão "Administrador" ao bot.

    - Proprietários de bots devem ter 2FA habilitado para certas ações e permissões quando adicionados a servidores com 2FA habilitado. Confira a `página de suporte a 2FA <https://support.discord.com/hc/pt-br/articles/219576828-Configurando-a-verifica%C3%A7%C3%A3o-em-duas-etapas>`_ para mais informações.

    .. image:: /images/discord_oauth2_perms.png
        :alt: As caixas de permissões com algumas permissões marcadas.

7. Agora a URL resultante pode ser usada para adicionar seu bot a um servidor. Copie e cole a URL no seu navegador, escolha um servidor para convidar o bot e clique em "Autorizar".


.. note::

    A pessoa que adiciona o bot precisa ter permissão de "Gerenciar Servidor".

Se você quiser gerar essa URL dinamicamente em tempo de execução dentro do seu bot usando a interface
:class:`discord.Permissions`, pode usar :func:`discord.utils.oauth_url`.