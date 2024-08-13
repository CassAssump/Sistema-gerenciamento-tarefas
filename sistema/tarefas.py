class Tarefa:
    def __init__(self, id, titulo, descricao="", concluida=False):
        self.id = id
        self.titulo = titulo
        self.descricao = descricao
        self.concluida = concluida

    def marcar_como_concluida(self):
        self.concluida = True

    def __str__(self):
        status = "Concluída" if self.concluida else "Pendente"
        return f"Tarefa: {self.titulo} - {status}\nDescrição: {self.descricao}"
        