class Tarefa:
    def __init__(self, titulo, descricao, prioridade, categoria, id_chamado):
        self.id = id_chamado
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.categoria = categoria
        self.situacao = "Pendente"

    def concluir(self):
        self.situacao = "Concluída"

    def exibir_resumo(self):
        return (
            f"ID: {self.id} | "
            f"Título: {self.titulo} | "
            f"Prioridade: {self.prioridade} | "
            f"Situação: {self.situacao} | "
            f"Categoria: {self.categoria}"
        )

