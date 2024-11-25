# estrutura de Dados para as Tarefas (pe 1)
tarefas = []

# função para adicionar uma nova tarefa (pe 2)
def adicionar_tarefa(nome, descricao, prioridade, categoria):
    tarefa = {
        'nome': nome,
        'descricao': descricao,
        'prioridade': prioridade,
        'categoria': categoria,
        'concluida': False
    }
    tarefas.append(tarefa)

# lista de tarefas (pe 3)
def listar_tarefas():
    for tarefa in tarefas:
        print(f"Nome: {tarefa['nome']}, Descrição: {tarefa['descricao']}, Prioridade: {tarefa['prioridade']}, Categoria: {tarefa['categoria']}, Concluída: {tarefa['concluida']}")

# para marcar uma tarefa como concluida (pe 4) 
def marcar_concluida(nome):
    for tarefa in tarefas:
        if tarefa['nome'] == nome:
            tarefa['concluida'] = True
            break

#exibir por prioridades ou categoria (pe 5)
def exibir_tarefas_por_prioridade(prioridade):
    for tarefa in tarefas:
        if tarefa['prioridade'] == prioridade:
            print(tarefa)

def exibir_tarefas_por_categoria(categoria):
    for tarefa in tarefas:
        if tarefa['categoria'] == categoria:
            print(tarefa)

#menu de comandos (pe 6)
def menu():
    while True:
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Marcar Tarefa como Concluída")
        print("4. Exibir Tarefas por Prioridade")
        print("5. Exibir Tarefas por Categoria")
        print("6. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            nome = input("Nome da Tarefa: ")
            descricao = input("Descrição da Tarefa: ")
            prioridade = input("Prioridade da Tarefa: ")
            categoria = input("Categoria da Tarefa: ")
            adicionar_tarefa(nome, descricao, prioridade, categoria)
        elif escolha == "2":
            listar_tarefas()
        elif escolha == "3":
            nome = input("Nome da Tarefa a ser marcada como concluída: ")
            marcar_concluida(nome)
        elif escolha == "4":
            prioridade = input("Prioridade: ")
            exibir_tarefas_por_prioridade(prioridade)
        elif escolha == "5":
            categoria = input("Categoria: ")
            exibir_tarefas_por_categoria(categoria)
        elif escolha == "6":
            break
        else:
            print("Opção Inválida!")

if __name__ == "__main__":
    menu()

#deixei comentado para melhor entendimento 
