import flet as ft


def main(page: ft.Page):
   
    page.title = "Tela de Login"

    
    email_input = ft.TextBox(label="Email", autofocus=True, width=300)
    senha_input = ft.TextBox(label="Senha", password=True, width=300)

    
    def toggle_senha(e):
        senha_input.password = not senha_input.password
        page.update()

    
    show_hide_btn = ft.ElevatedButton("Mostrar/Ocultar Senha", on_click=toggle_senha)

    
    def login(e):
        email = email_input.value
        senha = senha_input.value
        
        if email == "usuario@exemplo.com" and senha == "12345":
            page.add(ft.Text("Login realizado com sucesso!", color="green"))
        else:
            page.add(ft.Text("Email ou senha inválidos!", color="red"))

    
    login_btn = ft.ElevatedButton("Login", on_click=login)

    
    def esqueci_senha(e):
        page.add(ft.Text("Link para recuperação de senha enviado para o seu email!", color="blue"))

    esqueci_senha_btn = ft.TextButton("Esqueci minha senha", on_click=esqueci_senha)

   
    page.add(email_input, senha_input, show_hide_btn, login_btn, esqueci_senha_btn)


ft.app(target=main)
