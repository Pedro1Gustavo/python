cores = {"vermelho", "azul", "verde", "amarelo", "preto", "branco", "cinza", "roxo", "laranja"}

def cores_com_mais_de_quatro_letras(conjunto):
    cores_longas = {cor for cor in conjunto if len(cor) > 4}
    return cores_longas


cores_resultado = cores_com_mais_de_quatro_letras(cores)
print("Cores com mais de quatro letras:", cores_resultado)
