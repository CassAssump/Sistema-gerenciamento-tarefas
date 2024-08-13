from sistema.tarefas import Tarefa

class GerenciadorDeTarefas:
    
    def __init__(self):
        self.tarefas = []
        self.proximo_id = 1
        
    def adicionar_tarefa(self, titulo, descricao=""):
        tarefa = Tarefa(self.proximo_id, titulo, descricao)
        self.tarefas.append(tarefa)
        self.proximo_id += 1
        return tarefa
    
    def listar_tarefas(self):
        return self.tarefas
    
    def buscar_tarefa_por_id(self, id):
        for tarefa in self.tarefas:
            if tarefa.id == id:
                return tarefa
        return None
    
    def editar_tarefa(self, id, novo_titulo=None, nova_descricao=None):
        tarefa = self.buscar_tarefa_por_id(id)
        if tarefa:
            if novo_titulo:
                tarefa.titulo = novo_titulo
            if nova_descricao:
                tarefa.descricao = nova_descricao
            return tarefa
        return None
    def excluir_tarefa (self, id):
        tarefa = self.buscar_tarefa_por_id(id)
        if tarefa:
            self.tarefa.remove(tarefa)
            return tarefa
        return None