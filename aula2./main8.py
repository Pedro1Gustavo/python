pessoas = {
    "pessoa1": {"nome": "Adam", "idade": 25},
    "pessoa2": {"nome": "Bruno", "idade": 30},
    "pessoa3": {"nome": "Carlos", "idade": 22}
}

for chave, info in pessoas.items():
    print(f"Nome: {info['nome']}, Idade: {info['idade']} anos")
