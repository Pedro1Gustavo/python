class Tarefa:
    def __init__(self, nome, descricao):
        self.nome = nome
        self.descricao = descricao
        self.projeto = None  

    def associar_projeto(self, projeto):
        self.projeto = projeto
        projeto.adicionar_tarefa(self)  

    def __str__(self):
        return f"Tarefa: {self.nome}, Descrição: {self.descricao}"


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []  

    def adicionar_tarefa(self, tarefa):
        if tarefa not in self.tarefas:
            self.tarefas.append(tarefa)

    def listar_tarefas(self):
        if not self.tarefas:
            return "Este projeto não tem tarefas."
        return "\n".join([str(tarefa) for tarefa in self.tarefas])

    def __str__(self):
        return f"Projeto: {self.nome}"


projeto1 = Projeto("Desenvolvimento de Website")
projeto2 = Projeto("App de Gerenciamento de Tarefas")


tarefa1 = Tarefa("Desenhar layout", "Criar o design do site")
tarefa2 = Tarefa("Implementar login", "Criar a funcionalidade de login")
tarefa3 = Tarefa("Desenvolver backend", "Configurar o servidor e banco de dados")
tarefa4 = Tarefa("testar aplicativoo", "Testar as funcionalidades do app")


tarefa1.associar_projeto(projeto1)
tarefa2.associar_projeto(projeto1)
tarefa3.associar_projeto(projeto2)
tarefa4.associar_projeto(projeto2)


print(f"Tarefas do {projeto1}:")
print(projeto1.listar_tarefas())

print("\nTarefas do", projeto2)
print(projeto2.listar_tarefas())
