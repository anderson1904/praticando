import flet as ft

def cabeçalho():
    head = ft.Container( 
        border_radius=12,
        content = ft.Text(
            "Página de Login",size=30,
            color= ft.colors.WHITE,
            ),
        bgcolor= ft.colors.DEEP_PURPLE_ACCENT_200, 
        alignment=ft.alignment.top_center,            

    )
    return head


def login():
    nome =  ft.TextField(label="Usuário",bgcolor=ft.colors.WHITE, 
                         color = ft.colors.BLACK, height=30, text_size=14)
    
    senha =  ft.TextField(label="Senha", password=True,bgcolor=ft.colors.WHITE,
                          color = ft.colors.BLACK, height=30, text_size=14)
    
    esqueci = ft.ElevatedButton(text="ESQUECI MINHA SENHA",
                                color=ft.colors.WHITE)
    confirmar = ft.ElevatedButton(text="confirmar", bgcolor= '#129606',color=ft.colors.WHITE)
    return ft.Column(
        controls=[
            nome,
            senha,
            esqueci,
            confirmar,
        ]
    )
