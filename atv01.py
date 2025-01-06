tarefas = []

def adicionar_tarefa(tarefa):
    tarefas.append(tarefa)
    
def remover_tarefa(tarefa):
    if tarefa in tarefas:
        print(f"tarefa: {tarefa} foi removida com sucesso!")
        tarefas.remove(tarefa)
    else:
        print("Tarefa não encontrada")
        
def exibir_tarefas():
    for i, tarefa in enumerate(tarefas, 1):
        print(f"{i}. {tarefa}") 

def limpar_tarefas():
    confirmacao = input("Tem certeza que vc quer limpar todas as tarefas? (s/n): ").lower()
    if confirmacao == "s":
        tarefas.clear()
        print("Todas as tarefas foram limpass.")
    else:
        print("Limpeza cancelada.")
        
while True:
    opcao = input("1. Adicionar | 2. Remover | 3. Exibir | 4. Sair | 5. limpar tarefas")
    if opcao == "1":
        tarefa = input("Digite a Tarefa que deseja ADICIONAR:")
        adicionar_tarefa(tarefa)
    elif opcao == "2":
        tarefa = input("Digite a Tarefa que deseja REMOVER:")
        remover_tarefa(tarefa)
    elif opcao == "3":
        exibir_tarefas() 
    elif opcao == "5":
        limpar_tarefas()
    elif opcao == "4":
        break
    else:
        print("Opção invalida")

