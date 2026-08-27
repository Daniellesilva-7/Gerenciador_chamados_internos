#Gerenciar Chamados

chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "SENHA DO E-MAIL BLOQUEADA!!",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 4,
        "titulo": "Computador entrou em lentidão",
        "prioridade": "baixa",
        "situacao": "resolvido",
        "categoria": "hardware"
    },
    {
        "id": 5,
        "titulo": "ERRO no sistema atual",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "software"
    }
]

# Listar todos os chamados

print("========== LISTAR TODOS OS CHAMADOS ==========")

for chamado in chamados:
    print("ID:", chamado["id"])
    print("Título:", chamado["titulo"])
    print("Prioridade:", chamado["prioridade"])
    print("Situação:", chamado["situacao"])
    print("Categoria:", chamado["categoria"])
    print("===========================")


# Filtrar por situação

situacao_desejada = "aberto"

print("\n========== CHAMADOS ABERTOS ==========")

encontrou_chamado = False

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print("ID:", chamado["id"])
        print("Título:", chamado["titulo"])
        print("Prioridade:", chamado["prioridade"])
        print("Situação:", chamado["situacao"])
        print("Categoria:", chamado["categoria"])
        print("===========================")

        encontrou_chamado = True

if encontrou_chamado == False:
    print("Nenhum chamado encontrado para essa situação.")


# Teste de situação inexistente

situacao_desejada = "cancelado"

print("\n========== CHAMADOS CANCELADOS ==========")

encontrou_chamado = False

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print("ID:", chamado["id"])
        print("Título:", chamado["titulo"])
        print("Prioridade:", chamado["prioridade"])
        print("Situação:", chamado["situacao"])
        print("Categoria:", chamado["categoria"])
        print("===========================")

        encontrou_chamado = True

if encontrou_chamado == False:
    print("Nenhum chamado encontrado para essa situação.")


# Atualização da situação por ID existente

id_chamado = 2
nova_situacao = "resolvido"

print("\n========== ATUALIZAÇÃO DO CHAMADO ==========")

encontrou_chamado = False

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao

        print("Chamado atualizado com sucesso!")
        print("ID:", chamado["id"])
        print("Nova situação:", chamado["situacao"])

        encontrou_chamado = True

        break

if encontrou_chamado == False:
    print("Chamado não encontrado.")


# Teste com ID que não existe no sistema

id_chamado = 10
nova_situacao = "aberto"

print("\n========== TESTE DE ID INEXISTENTE NO SISTEMA ==========")

encontrou_chamado = False

for chamado in chamados:
    if chamado["id"] == id_chamado:
        chamado["situacao"] = nova_situacao

        print("Chamado atualizado com sucesso!")

        encontrou_chamado = True

        break

if encontrou_chamado == False:
    print("Chamado não encontrado.")


# Mostrar categorias sem duplicação

categorias = set()

for chamado in chamados:
    categorias.add(chamado["categoria"])

print("\n========== CATEGORIAS SEM DUPLICAÇÃO ==========")

for categoria in categorias:
    print(categoria)
