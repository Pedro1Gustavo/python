def processador_texto(texto, **kwargs):
    
    operacoes = {
        "contar_palavras": lambda t: len(t.split()),
        "contar_letras": lambda t: sum(c.isalpha() for c in t),
        "inverter_texto": lambda t: t[::-1],
        "substituir_palavra": lambda t, antiga, nova: t.replace(antiga, nova),
    }
    
    resultado = texto  
    
    
    for operacao, valor in kwargs.items():
        if operacao == "contar_palavras":
            print(f"Contagem de palavras: {operacoes[operacao](resultado)}")
        elif operacao == "contar_letras":
            print(f"Contagem de letras: {operacoes[operacao](resultado)}")
        elif operacao == "inverter_texto" and valor:
            resultado = operacoes[operacao](resultado)
        elif operacao == "substituir_palavra":
            antiga = valor.get("antiga")
            nova = valor.get("nova")
            if antiga and nova:
                resultado = operacoes[operacao](resultado, antiga, nova)
    
    return resultado

texto = "Python é incrível como o professor! Python é uma linguagem poderosa."

resultado = processador_texto(
    texto,
    contar_palavras=True,
    contar_letras=True,
    inverter_texto=False,
    substituir_palavra={"antiga": "Python", "nova": "Programação"}
)

print("\nTexto resultante:", resultado)
