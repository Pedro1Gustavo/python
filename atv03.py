def adicionar_contato(contatos):
    try:
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        contatos[nome] = telefone
        print(f"Contato de {nome} adicionado com sucesso.")
    except Exception as e:
        print(f"Erro ao adicionar contato: {e}")

def buscar_contato(contatos):
    try:
        nome = input("Buscar Nome: ")
        telefone = contatos.get(nome, 'não encontrado')
        print(f"Telefone de {nome}: {telefone}")
    except Exception as e:
        print(f"Erro ao buscar contato: {e}")

def remover_contato(contatos):
    try:
        nome = input("Remover Nome: ")
        if nome in contatos:
            contatos.pop(nome)
            print(f"Contato de {nome} removido com sucesso.")
        else:
            print(f"Contato de {nome} não encontrado.")
    except Exception as e:
        print(f"Erro ao remover contato: {e}")

def exibir_contatos(contatos):
    try:
        if contatos:
            for nome, telefone in contatos.items():
                print(f"{nome}: {telefone}")
        else:
            print("Não há contatos cadastrados.")
    except Exception as e:
        print(f"Erro ao exibir contatos: {e}")

def exibir_menu():
    try:
        print("\n1. Adicionar | 2. Buscar | 3. Remover | 4. Exibir | 5. Sair")
        opcao = input("Escolha uma opção: ")
        return opcao
    except Exception as e:
        print(f"Erro ao exibir menu: {e}")
        return None

def main():
    contatos = {}

    while True:
        opcao = exibir_menu()

        if opcao == "1":
            adicionar_contato(contatos)
        elif opcao == "2":
            buscar_contato(contatos)
        elif opcao == "3":
            remover_contato(contatos)
        elif opcao == "4":
            exibir_contatos(contatos)
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida, tente novamente.")

main()
