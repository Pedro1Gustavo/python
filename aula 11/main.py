class Motorista:
    def __init__(self, nome, idade, status_habilitacao, tipo_habilitacao):
        self.nome = nome
        self.idade = idade
        self.status_habilitacao = status_habilitacao
        self.tipo_habilitacao = tipo_habilitacao

motoristas = [
    Motorista("João", 25, "Apto", "B"),
    Motorista("Maria", 32, "Não Apto", "A"),
    Motorista("Pedro", 45, "Apto", "AB"),
    Motorista("Ana", 19, "Apto", "B"),
    Motorista("Carlos", 30, "Não Apto", "AB")
]

def exibir_motoristas_status(status):
    if status == "apto":
        for motorista in motoristas:
            if motorista.status_habilitacao == "Apto":
                print(f"{motorista.nome}, Idade: {motorista.idade}, Status: {motorista.status_habilitacao}, Tipo: {motorista.tipo_habilitacao}")
    elif status == "não apto":
        for motorista in motoristas:
            if motorista.status_habilitacao == "Não Apto":
                print(f"{motorista.nome}, Idade: {motorista.idade}, Status: {motorista.status_habilitacao}, Tipo: {motorista.tipo_habilitacao}")

def exibir_motoristas_por_tipo(tipo):
    for motorista in motoristas:
        if motorista.tipo_habilitacao == tipo:
            print(f"{motorista.nome}, Idade: {motorista.idade}, Status: {motorista.status_habilitacao}, Tipo: {motorista.tipo_habilitacao}")

def exibir_motoristas_maior_que_idade(idade_minima):
    for motorista in motoristas:
        if motorista.idade > idade_minima:
            print(f"{motorista.nome}, Idade: {motorista.idade}, Status: {motorista.status_habilitacao}, Tipo: {motorista.tipo_habilitacao}")

status = input("Digite 'apto' ou 'não apto' para exibir motoristas: ")
exibir_motoristas_status(status)


tipo = input("Digite o tipo de habilitação (A, B, AB): ")
exibir_motoristas_por_tipo(tipo)


idade_minima = int(input("Digite uma idade mínima: "))
exibir_motoristas_maior_que_idade(idade_minima)



