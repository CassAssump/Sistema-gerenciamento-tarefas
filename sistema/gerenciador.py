import os
import json
from sistema.tarefas import Tarefa

class GerenciadorDeTarefas:
    def __init__(self, arquivo="tarefas.json"):
        self.arquivo = arquivo
        self.tarefas = []
        self.proximo_id = 1
        self.carregar_tarefas()

    def carregar_tarefas(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
                self.tarefas = [Tarefa(**tarefa) for tarefa in dados["tarefas"]]
                self.proximo_id = dados["proximo_id"]

    def salvar_tarefas(self):
        with open(self.arquivo, "w") as f:
            dados = {
                "tarefas": [tarefa.__dict__ for tarefa in self.tarefas],
                "proximo_id": self.proximo_id
            }
            json.dump(dados, f, indent=4)

    def adicionar_tarefa(self, titulo, descricao=""):
        tarefa = Tarefa(self.proximo_id, titulo, descricao)
        self.tarefas.append(tarefa)
        self.proximo_id += 1
        self.salvar_tarefas()
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
            self.salvar_tarefas()
            return tarefa
        return None

    def excluir_tarefa(self, id):
        tarefa = self.buscar_tarefa_por_id(id)
        if tarefa:
            self.tarefas.remove(tarefa)
            self.salvar_tarefas()
            return tarefa
        return None