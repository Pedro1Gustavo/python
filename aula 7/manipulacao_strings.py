def inverter_string(texto):
    """Inverte a string fornecida."""
    return texto[::-1]

def contar_palavras(texto):
    """Conta o número de palavras em uma string."""
    return len(texto.split())

def verificar_palindromo(texto):
    """Verifica se a string é um palíndromo (ignora espaços e diferenças de maiúsculas/minúsculas)."""
    texto_limpo = texto.replace(" ", "").lower()
    return texto_limpo == texto_limpo[::-1]
