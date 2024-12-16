import flet as ft

def main(page: ft.Page):
    
    page.title = "Verificação de Idade"

    
    idade_input = ft.TextField(label="Qual sua idade?", autofocus=True)
    resposta_texto = ft.Text("Responda a pergunta para ver sua classificação.", size=20)

    
    def verificar_idade(e):
        idade = int(idade_input.value)  
        
        if idade < 18:
            resposta_texto.value = "Você é menor de idade."
            resposta_texto.color = ft.colors.RED  
        elif idade == 18:
            resposta_texto.value = "Você tem exatamente 18 anos."
            resposta_texto.color = ft.colors.YELLOW  
        else:
            resposta_texto.value = "Você é maior de idade."
            resposta_texto.color = ft.colors.GREEN  
        
        page.update()  

    
    page.add(
        idade_input,  
        ft.ElevatedButton("Verificar Idade", on_click=verificar_idade),  
        resposta_texto  
    )


ft.app(target=main)
