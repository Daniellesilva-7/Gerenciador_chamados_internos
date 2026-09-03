--- Gerenciador de Chamados

--- Objetivo

O programa tem como objetivo gerenciar chamados internos de uma empresa de suporte técnico.

Os chamados são armazenados em uma lista de dicionários contendo as seguintes informações:
- ID
- Título
- Prioridade
- Situação
- Categoria

O programa permite listar todos os chamados, filtrar chamados por situação, atualizar a situação de um chamado pelo ID e mostrar as categorias sem duplicação.

---Como executar

Para executar o programa, abra o terminal na pasta onde está o arquivo `gerenciador_chamados.py` e digite:


python gerenciador_chamados.py


Caso seja necessário utilizar o comando `python3`, digite:


python3 gerenciador_chamados.py


-- Exemplo de uso

O programa apresenta inicialmente todos os chamados cadastrados.

Depois, realiza um filtro pelos chamados que estão com a situação **"aberto"**.

Também é realizado um teste com a situação **"cancelado"**, que não possui chamados, mostrando a mensagem:


Nenhum chamado encontrado para essa situação.


Em seguida, o programa atualiza o chamado de ID **2** para a situação **"resolvido"**.

Também é realizado um teste com o ID **10**, que não existe no sistema, mostrando:

Chamado não encontrado.


Por fim, o programa apresenta as categorias cadastradas sem duplicação.

--Autoria

Aluno(a): Danielle Gil Silva RA: 202422994 e Dayana Gil Silva RA: 202422920

Disciplina: Laboratório de Programação Back-End

Atividade: Hands On — Semana 04
