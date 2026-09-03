def cadastrar_tarefa(
    tarefas,
    titulo,
    descricao,
    prioridade,
    categoria,
    id_chamado,
    classe_tarefa
):
    nova_tarefa = classe_tarefa(
        titulo,
        descricao,
        prioridade,
        categoria,
        id_chamado
    )

    tarefas.append(nova_tarefa)

    return nova_tarefa


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return

    print("\n========== TODAS AS TAREFAS ==========")

    for tarefa in tarefas:
        print(f"ID: {tarefa.id}")
        print(f"Título: {tarefa.titulo}")
        print(f"Descrição: {tarefa.descricao}")
        print(f"Prioridade: {tarefa.prioridade}")
        print(f"Situação: {tarefa.situacao}")
        print(f"Categoria: {tarefa.categoria}")
        print("-" * 40)


def filtrar_por_situacao(tarefas, situacao):
    return [
        tarefa
        for tarefa in tarefas
        if tarefa.situacao == situacao
    ]


def atualizar_situacao(tarefas, id_chamado, nova_situacao):
    for tarefa in tarefas:
        if tarefa.id == id_chamado:
            tarefa.situacao = nova_situacao
            return True

    return False


def mostrar_categorias(tarefas):
    categorias = set()

    for tarefa in tarefas:
        categorias.add(tarefa.categoria)

    print("\n========== CATEGORIAS ==========")

    for categoria in sorted(categorias):
        print(f"- {categoria}")
