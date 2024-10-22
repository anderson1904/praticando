import flet as ft
from rotas import(
    rota_cadastro,
    rota_login,
)

def main(page: ft.Page):
    page.window_width=300
    page.window_height=400
    page.update()

    def paginação(route):
        page.views.clear()
        if page.route == "/":
            page.views.append(rota_login(page))
        elif page.route == "/cadastro":
            page.views.append(rota_cadastro(page))
    page.update()
    page.on_route_change = paginação
    page.go(page.route)


    
ft.app(target=main)
