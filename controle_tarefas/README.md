-- Gerenciador de Chamados Internos

-- Objetivo

O projeto tem como objetivo realizar o controle de chamados internos de uma equipe, permitindo cadastrar, listar, concluir, filtrar e atualizar chamados.

Nesta versão, o projeto foi refatorado utilizando a classe `Tarefa`, funções e módulos separados, conforme a proposta da atividade de refatoração.

-- Execução

Entre na pasta `controle_tarefas` pelo terminal e execute:

```bash
python main.py
```

Caso seja necessário:

```bash
python3 main.py
```

## Organização dos arquivos

 `tarefa.py`: contém a classe `Tarefa` e os métodos relacionados às tarefas.
 `servicos.py`: contém as funções de cadastro, listagem, filtro, atualização e categorias.
 `main.py`: realiza o cadastro dos chamados e demonstra o funcionamento do sistema.
 `README.md`: apresenta as informações e instruções do projeto.

## Funcionalidades

O sistema possui as seguintes funcionalidades:

. Cadastro de chamados;
. Listagem de todos os chamados;
. Conclusão de uma tarefa;
. Filtro por situação;
. Atualização da situação pelo ID;
. Identificação de chamado inexistente;
. Exibição das categorias sem repetição.

-- Chamados cadastrados

O sistema utiliza os chamados do projeto original:

1. Sem acesso ao sistema interno;
2. Impressora sem conexão;
3. Senha do e-mail bloqueada;
4. Computador muito lento;
5. Erro no sistema de chamados;
6. Atualização de programa.

-- Refatoração

O projeto anterior utilizava uma lista de dicionários. Nesta nova versão, cada chamado é representado por um objeto da classe `Tarefa`.

A situação inicial das tarefas é `Pendente`. O método `concluir()` altera a situação para `Concluída`.

-- Autoria

Aluna: Danielle Gil Silva RA:202422994
Aluna: Dayana Gil Silva RA: 202422920

Disciplina: Laboratório de Programação Back-End
