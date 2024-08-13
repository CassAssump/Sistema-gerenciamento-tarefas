from sistema.tarefas import Tarefa
from sistema.gerenciador import GerenciadorDeTarefas

if __name__ == "__main__":
    gerenciador = GerenciadorDeTarefas()
    print(f"Tipo de gerenciador: {type(gerenciador)}")
    while True:
        print("\n=== Gerenciador de Tarefas ===")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Editar Tarefa")
        print("4. Excluir Tarefa")
        print("5. Marcar Tarefa como Concluída")
        print("6. Sair")
        opcao = input("Escolha uma opção: ")
        
        gerenciador.adicionar_tarefa("Comprar leite", "Ir ao mercado e comprar leite.")
        gerenciador.adicionar_tarefa("Estudar Python", "Fazer exercícios de orientação a objetos.")
        
        
        if opcao == "1":
            titulo = input('Digite o título da tarefa: ')
            descricao = input('Digite a descrição da tarefa')
            gerenciador.adicionar_tarefa(titulo, descricao)
            print ("Tarefa adicionada com sucesso!")
            
        elif opcao == "2":
            tarefas = gerenciador.listar_tarefas()
            if tarefas:
                for tarefa in tarefas:
                    print (tarefa)
            else: 
                print ("Nenhuma tarefa encontrada")
                
        elif opcao == "3":
            id_tarefa = int(input("Deseja o ID da tarefa que deseja editar"))
            novo_titulo = input("Digite o novo título: ")
            nova_descricao = input('Digite a nova descrição: ')
            tarefa_editada = gerenciador.editar_tarefa(id_tarefa, novo_titulo,nova_descricao)
            if tarefa_editada:
                print ("Tarefa editada com sucesso! ")
            else:
                print ("Tarefa não encontrada")
                
        elif opcao == '4':
            id_tarefa = int(input("Deseja o ID da tarefa que deseja excluir: "))
            tarefa_excluida = gerenciador.excluir_tarefa(id_tarefa)
            if tarefa_excluida:
                print ("Tarefa excluida com sucesso! ")
            else:
                print ("Tarefa não encontrada.")
                
        elif opcao == "5":
            id_tarefa = int(input('Coloque o ID da tarefa que deseja marcar como conluída: '))
            tarefa = gerenciador.buscar_tarefa_por_id(id_tarefa)
            if tarefa:
                Tarefa.marcar_como_concluida
            else:
                print ('Tarefa não encontrada')
        
        elif opcao =='6':
            print ("Saindo do gerenciador de tarefas")
            break
        
    else:
        print ("Opção inválida. Tente novamente.")     