:orphan:

.. currentmodule:: discord
.. versionadded:: 0.6.0
.. _logging_setup:

Configurando Logging
=====================

*discord.py* registra erros e informações de depuração via o módulo :mod:`logging` do Python. Para simplificar este processo, a biblioteca fornece uma configuração padrão para o logger ``discord`` ao usar :meth:`Client.run`. É fortemente recomendado que o módulo de logging seja configurado, pois nenhum erro ou aviso será exibido se não for configurado.

A configuração de logging padrão fornecida pela biblioteca imprime em :data:`sys.stderr` usando saída colorida. Você pode configurá-la para enviar para um arquivo usando um dos :mod:`logging.handlers` incorporados, como :class:`logging.FileHandler`.

Isso pode ser feito passando o handler através de :meth:`Client.run`:

.. code-block:: python3

    import logging

    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    # Supondo que client seja uma subclasse de discord.Client...
    client.run(token, log_handler=handler)

Também é possível desabilitar completamente a configuração de logging da biblioteca passando ``None``:

.. code-block:: python3

    client.run(token, log_handler=None)

Da mesma forma, configurar o nível de log para ``logging.DEBUG`` também é possível:

.. code-block:: python3

    import logging

    handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')

    # Supondo que client seja uma subclasse de discord.Client...
    client.run(token, log_handler=handler, log_level=logging.DEBUG)

Isto é recomendado, especialmente em níveis verbosos como ``DEBUG``, pois muitos eventos são registrados e isso poderia congestionar o stderr do seu programa.

Se você deseja que a configuração de logging fornecida pela biblioteca afete todos os loggers, e não apenas o logger ``discord``, você pode passar ``root_logger=True`` dentro de :meth:`Client.run`:

.. code-block:: python3

    client.run(token, log_handler=handler, root_logger=True)

Se você deseja configurar logging usando a configuração fornecida pela biblioteca sem usar :meth:`Client.run`, você pode usar :func:`discord.utils.setup_logging`:

.. code-block:: python3

    import discord

    discord.utils.setup_logging()

    # ou, por exemplo
    discord.utils.setup_logging(level=logging.INFO, root=False)

Configurações mais avançadas são possíveis com o módulo :mod:`logging`. O exemplo abaixo configura um handler de arquivo rotativo que registra DEBUG para tudo que a biblioteca registra, exceto requisições HTTP:

.. code-block:: python3

    import discord
    import logging
    import logging.handlers

    logger = logging.getLogger('discord')
    logger.setLevel(logging.DEBUG)
    logging.getLogger('discord.http').setLevel(logging.INFO)

    handler = logging.handlers.RotatingFileHandler(
        filename='discord.log',
        encoding='utf-8',
        maxBytes=32 * 1024 * 1024,  # 32 MiB
        backupCount=5,  # Rotaciona por 5 arquivos
    )
    dt_fmt = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter('[{asctime}] [{levelname:<8}] {name}: {message}', dt_fmt, style='{')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    # Supondo que client seja uma subclasse de discord.Client...
    # Suprime a configuração padrão já que temos a nossa própria
    client.run(token, log_handler=None)

Para mais informações, consulte a documentação e tutorial do módulo :mod:`logging`.

.. versionchanged:: 2.0

    A biblioteca agora fornece uma configuração de logging padrão.