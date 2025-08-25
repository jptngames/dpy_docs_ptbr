
.. _version_guarantees:

Garantia de Versão
==================

A biblioteca segue o `princípio de versionamento semântico <https://semver.org/>`_, o que significa que a versão principal é atualizada sempre que há uma mudança incompatível na API. No entanto, devido à falta de garantias por parte do Discord em relação a mudanças que quebrem funcionalidades, juntamente com a natureza dinâmica do Python, pode ser difícil discernir o que pode ser considerado uma mudança incompatível e o que não é.

A primeira coisa a se ter em mente é que mudanças incompatíveis aplicam-se apenas a **funções e classes documentadas publicamente**. Se não estiver listada na documentação aqui, então não faz parte da API pública e, portanto, está sujeita a mudanças. Isso inclui atributos que começam com um underscore ou funções sem underscore que não estão documentadas.

.. note::

    Os exemplos abaixo não são exaustivos.

Exemplos de Mudanças Incompatíveis
-----------------------------------

- Alterar o valor padrão de um parâmetro para outro valor.
- Renomear uma função sem manter um alias para a função antiga.
- Adicionar ou remover parâmetros de um evento.

Exemplos de Mudanças Compatíveis
---------------------------------

- Adicionar ou remover atributos privados iniciados com underscore.
- Adicionar um elemento ao ``__slots__`` de uma data class.
- Alterar o comportamento de uma função para corrigir um bug.
- Mudanças no comportamento de tipagem da biblioteca.
- Mudanças na convenção de chamada de funções que são principalmente callbacks.
- Alterações na documentação.
- Modificação do tratamento interno de HTTP.
- Atualização das dependências para uma nova versão, principal ou não.