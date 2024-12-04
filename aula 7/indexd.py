class Biblioteca:
    def __init__(self):
        self.livros = {}  # Dicionário para armazenar livros {'título': {'autor': 'autor', 'copias': número}}
        self.usuarios = {}  

    def adicionar_livro(self, titulo, autor, copias):
        """Adiciona um livro à biblioteca."""
        if titulo in self.livros:
            self.livros[titulo]['copias'] += copias
        else:
            self.livros[titulo] = {'autor': autor, 'copias': copias}
        print(f"Livro '{titulo}' adicionado/atualizado com sucesso!")

    def listar_livros(self):
        """Lista todos os livros disponíveis na biblioteca."""
        if not self.livros:
            print("A biblioteca está vazia.")
        else:
            print("\n=== Livros Disponíveis ===")
            for titulo, info in self.livros.items():
                print(f"Título: {titulo}, Autor: {info['autor']}, Cópias Disponíveis: {info['copias']}")

    def emprestar_livro(self, usuario, titulo):
        """Realiza o empréstimo de um livro."""
        if titulo in self.livros and self.livros[titulo]['copias'] > 0:
            self.livros[titulo]['copias'] -= 1
            if usuario not in self.usuarios:
                self.usuarios[usuario] = []
            self.usuarios[usuario].append(titulo)
            print(f"O livro '{titulo}' foi emprestado para {usuario}.")
        else:
            print(f"Desculpe, o livro '{titulo}' não está disponível.")

    def devolver_livro(self, usuario, titulo):
        """Recebe a devolução de um livro."""
        if usuario in self.usuarios and titulo in self.usuarios[usuario]:
            self.usuarios[usuario].remove(titulo)
            self.livros[titulo]['copias'] += 1
            print(f"O livro '{titulo}' foi devolvido por {usuario}.")
        else:
            print(f"{usuario} não tem o livro '{titulo}' emprestado.")

    def verificar_disponibilidade(self, titulo):
        """Verifica a disponibilidade de um livro específico."""
        if titulo in self.livros:
            copias = self.livros[titulo]['copias']
            print(f"O livro '{titulo}' tem {copias} cópias disponíveis.")
        else:
            print(f"O livro '{titulo}' não está na biblioteca.")

    def listar_livros_emprestados(self, usuario):
        """Mostra os livros emprestados por um usuário."""
        if usuario in self.usuarios and self.usuarios[usuario]:
            print(f"Livros emprestados por {usuario}: {', '.join(self.usuarios[usuario])}")
        else:
            print(f"{usuario} não tem livros emprestados.")

def main():
    biblioteca = Biblioteca()

    while True:
        print("\n=== Gerenciador de Livros ===")
        print("1. Adicionar Livro")
        print("2. Listar Livros")
        print("3. Emprestar Livro")
        print("4. Devolver Livro")
        print("5. Verificar Disponibilidade")
        print("6. Listar Livros Emprestados")
        print("7. Sair")
        
        escolha = input("Escolha uma opção (1-7): ")
        
        if escolha == "1":
            titulo = input("Título do Livro: ")
            autor = input("Autor do Livro: ")
            try:
                copias = int(input("Número de Cópias: "))
                biblioteca.adicionar_livro(titulo, autor, copias)
            except ValueError:
                print("Por favor, insira um número válido para as cópias.")
        
        elif escolha == "2":
            biblioteca.listar_livros()
        
        elif escolha == "3":
            usuario = input("Nome do Usuário: ")
            titulo = input("Título do Livro: ")
            biblioteca.emprestar_livro(usuario, titulo)
        
        elif escolha == "4":
            usuario = input("Nome do Usuário: ")
            titulo = input("Título do Livro: ")
            biblioteca.devolver_livro(usuario, titulo)
        
        elif escolha == "5":
            titulo = input("Título do Livro: ")
            biblioteca.verificar_disponibilidade(titulo)
        
        elif escolha == "6":
            usuario = input("Nome do Usuário: ")
            biblioteca.listar_livros_emprestados(usuario)
        
        elif escolha == "7":
            print("Encerrando o programa. Até logo!")
            break
        
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
