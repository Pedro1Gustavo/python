import flet as ft


def main(page: ft.Page):
    
    page.title = "Troca de Cor do Nome"
    
    
    nome = ft.TextField(label="Qual é o seu nome?", autofocus=True)
    texto_nome = ft.Text("Seu nome aparecerá aqui!", size=30)

    
    def mostrar_nome(e):
        texto_nome.value = f"Olá, {nome.value}!"
        page.update()
    
    
    def mudar_cor_azul(e):
        texto_nome.color = ft.colors.BLUE
        page.update()

    def mudar_cor_verde(e):
        texto_nome.color = ft.colors.GREEN
        page.update()

    def mudar_cor_vermelho(e):
        texto_nome.color = ft.colors.RED
        page.update()

    
    page.add(
        nome,  
        ft.ElevatedButton("Mostrar Nome", on_click=mostrar_nome),  
        texto_nome,  
        ft.Row(  
            [
                ft.ElevatedButton("Cor Azul", on_click=mudar_cor_azul),
                ft.ElevatedButton("Cor Verde", on_click=mudar_cor_verde),
                ft.ElevatedButton("Cor Vermelha", on_click=mudar_cor_vermelho),
            ]
        )
    )


ft.app(target=main)



