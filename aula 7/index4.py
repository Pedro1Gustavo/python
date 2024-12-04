import random

def jogo_adivinhacao():
    print("Bem-vindo ao Jogo de Adivinhação!")
    print("O programa escolheu um número entre 1 e 100.")
    print("Tente adivinhar qual é! Você receberá dicas se o número é maior ou menor.")


    numero_secreto = random.randint(1, 100)
    tentativas = 0

    while True:
        try:
        
            palpite = int(input("Digite seu palpite (entre 1 e 100): "))
            tentativas += 1

            if palpite < 1 or palpite > 100:
                print("Por favor, digite um número válido entre 1 e 100.")
                continue

            if palpite < numero_secreto:
                print("O número secreto é maior!")
            elif palpite > numero_secreto:
                print("O número secreto é menor!")
            else:
                print(f"Parabéns! Você acertou o número secreto em {tentativas} tentativa(s).")
                break

        except ValueError:
            print("Por favor, insira um número válido.")

if __name__ == "__main__":
    jogo_adivinhacao()
