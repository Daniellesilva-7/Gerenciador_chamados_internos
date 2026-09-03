from tarefa import Tarefa
from servicos import (
    cadastrar_tarefa,
    listar_tarefas,
    filtrar_por_situacao,
    atualizar_situacao,
    mostrar_categorias
)


# Lista que armazenará as tarefas
tarefas = []


# Cadastro dos chamados do projeto original
cadastrar_tarefa(
    tarefas,
    "Sem acesso ao sistema interno",
    "Usuário sem acesso ao sistema interno da empresa.",
    "alta",
    "acesso",
    1,
    Tarefa
)


cadastrar_tarefa(
    tarefas,
    "Impressora sem conexão",
    "Impressora do setor não está conseguindo se conectar.",
    "média",
    "hardware",
    2,
    Tarefa
)


cadastrar_tarefa(
    tarefas,
    "Senha do e-mail bloqueada",
    "Usuário não consegue acessar o e-mail porque a senha está bloqueada.",
    "alta",
    "acesso",
    3,
    Tarefa
)


cadastrar_tarefa(
    tarefas,
    "Computador muito lento",
    "Computador apresenta lentidão durante o uso.",
    "baixa",
    "hardware",
    4,
    Tarefa
)


cadastrar_tarefa(
    tarefas,
    "Erro no sistema de chamados",
    "Sistema de chamados apresenta erro durante a utilização.",
    "média",
    "software",
    5,
    Tarefa
)


cadastrar_tarefa(
    tarefas,
    "Atualização de programa",
    "Programa precisa ser atualizado para uma nova versão.",
    "baixa",
    "software",
    6,
    Tarefa
)


# Demonstração da mudança de estado
# O chamado de ID 1 passa de Pendente para Concluída
tarefas[0].concluir()


print("==========================================")
print("       GERENCIADOR DE CHAMADOS INTERNOS")
print("==========================================")


# Listagem de todos os chamados
listar_tarefas(tarefas)


# Filtro por situação
print("\n========== TAREFAS CONCLUÍDAS ==========")

tarefas_concluidas = filtrar_por_situacao(
    tarefas,
    "Concluída"
)

listar_tarefas(tarefas_concluidas)


print("\n========== TAREFAS PENDENTES ==========")

tarefas_pendentes = filtrar_por_situacao(
    tarefas,
    "Pendente"
)

listar_tarefas(tarefas_pendentes)


# Teste de atualização por ID
print("\n========== ATUALIZAÇÃO DE CHAMADO ==========")

if atualizar_situacao(tarefas, 2, "Em atendimento"):
    print("Chamado 2 atualizado com sucesso!")
    print("Nova situação: Em atendimento")
else:
    print("Chamado não encontrado.")


# Teste de ID inexistente
print("\n========== TESTE DE ID INEXISTENTE ==========")

if atualizar_situacao(tarefas, 10, "Concluída"):
    print("Chamado 10 atualizado com sucesso!")
else:
    print("Chamado não encontrado.")


# Mostrar categorias sem repetição
mostrar_categorias(tarefas)

