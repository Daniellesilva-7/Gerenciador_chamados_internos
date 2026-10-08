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

## Semana 7 — Modelagem e Persistência de Dados com Django

### Objetivo

Nesta etapa, o projeto foi desenvolvido utilizando o framework Django, com o objetivo de implementar a persistência de dados, permitindo que categorias e tarefas continuem armazenadas mesmo após o encerramento e reinicialização do servidor.

### Implementações realizadas

- Criação do model `Categoria`, contendo o campo nome.
- Criação do model `Tarefa`, contendo título, descrição, prioridade, data prevista, situação e categoria.
- Implementação do relacionamento `ForeignKey` entre Categoria e Tarefa.
- Implementação do método `__str__` nos dois models.
- Criação e aplicação das migrações no banco de dados SQLite.
- Registro dos models no Django Admin.
- Cadastro das categorias Estudos e Pessoal.
- Cadastro das tarefas Revisar Django e Organizar estudos.
- Realização de consultas utilizando o ORM do Django.
- Atualização da situação de uma tarefa de Pendente para Concluída.

### Comandos utilizados

Para gerar e aplicar as migrações:

```bash
python manage.py makemigrations
python manage.py migrate
```

Para iniciar o servidor:

```bash
python manage.py runserver
```

Para acessar o shell do Django:

```bash
python manage.py shell
```

### Consultas realizadas pelo ORM

```python
from tarefas.models import Categoria, Tarefa

# Listar todas as tarefas
Tarefa.objects.all()

# Consultar tarefas pendentes
Tarefa.objects.filter(situacao="PENDENTE")

# Ordenar pela data prevista
Tarefa.objects.order_by("data_prevista")

# Atualizar uma tarefa
tarefa = Tarefa.objects.get(titulo="Revisar Django")
tarefa.situacao = "CONCLUIDA"
tarefa.save()
```

### Dificuldade encontrada e solução

Durante a implementação, foi identificado um problema na exibição dos nomes das categorias e tarefas no Django Admin. Os registros apareciam como `Categoria object` e `Tarefa object`, em vez de apresentar seus respectivos nomes.

O problema ocorreu devido à indentação incorreta dos métodos `__str__` nos models.

A solução foi corrigir a indentação e os retornos dos métodos, utilizando `self.nome` para Categoria e `self.titulo` para Tarefa.

Após a correção, os registros passaram a ser exibidos corretamente no painel administrativo.

### Validação da persistência

Foram cadastradas duas categorias e duas tarefas no banco de dados SQLite.

A tarefa Revisar Django foi atualizada para Concluída, enquanto a tarefa Organizar estudos permaneceu Pendente.

Após interromper e reiniciar o servidor Django, os registros continuaram disponíveis no painel administrativo, confirmando a persistência dos dados.

-- Autoria

Aluna: Danielle Gil Silva RA:202422994
Aluna: Dayana Gil Silva RA: 202422920

Disciplina: Laboratório de Programação Back-End
