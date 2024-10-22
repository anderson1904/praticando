import flet as ft
from views import(
    cadastro,login
)

def rota_login(page: ft.Page):
    return ft.View(
        '/',
        controls=[
            login.cabeçalho(),
            login.login(),
            ft.Text('não está cadastrado?',size=25),
            ft.ElevatedButton('cadastre-se aqui', on_click=lambda _: page.go("/cadastro"))
        ]
    )

def rota_cadastro(page:ft.Page):
    return ft.View(
        '/cadastro',
        controls=[
            cadastro.cabeçalho(),
            cadastro.cadastro(),
            ft.Text('já possui conta?', size=25),
            ft.ElevatedButton(' faça seu login', on_click=lambda _: page.go("/"))
        ]
    )
