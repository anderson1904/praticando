import flet as ft

def cabeçalho():
    head = ft.Container(content = ft.Text("Bem-Vindo", size=40, color=ft.colors.WHITE10),
                        border_radius=8,bgcolor=ft.colors.DEEP_PURPLE_100,
                        )
    return head
def cadastro():

    nome =  ft.TextField(label="Usuário",bgcolor=ft.colors.WHITE, color = ft.colors.BLACK,
                          height=30, text_size=14)
    senha =  ft.TextField(label="Senha", password=True,
                          bgcolor=ft.colors.WHITE, color = ft.colors.BLACK,
                          height=30, text_size=14)
    confirmarSenha =  ft.TextField(label="Confirmar senha", password=True,
                                   bgcolor=ft.colors.WHITE, color = ft.colors.BLACK,
                                   height=30, text_size=14)
    
    cadastrar = ft.ElevatedButton(text="confirmar",bgcolor= '#129606')

    
    return ft.Column(
        controls=[
            nome,
            senha,
            confirmarSenha,
            cadastrar,
        ]
    )