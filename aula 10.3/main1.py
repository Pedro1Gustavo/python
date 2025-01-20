import flet as ft


def main(page: ft.Page):
    
    text1 = ft.Text("Texto 1 - Cor vermelha e tamanho grande", color="red", size=30)

    
    text2 = ft.Text("Texto 2 - Cor azul e tamanho médio", color="blue", size=20)

    
    text3 = ft.Text("Texto 3 - Cor verde e tamanho pequeno", color="green", size=15)

    
    page.add(text1, text2, text3)


ft.app(target=main)
