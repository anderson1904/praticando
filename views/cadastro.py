import flet as ft

def cabeçalho():
    head = ft.Container(content = ft.Text("Bem-Vindo", size=30, color=ft.colors.WHITE),
                        border_radius=8,bgcolor=ft.colors.DEEP_PURPLE_ACCENT_200,
                        alignment=ft.alignment.top_center
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