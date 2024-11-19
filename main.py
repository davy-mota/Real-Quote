import flet as ft
import pyrebase
from get_price import get_currency_quote, get_currency_quote_week


firebaseConfig = {
  'apiKey': "AIzaSyB9JN6MNaaeLuNdVOwSlWfNfSciiK0Z5Xc",
  'authDomain': "realquote-2adbc.firebaseapp.com",
  'projectId': "realquote-2adbc",
  'storageBucket': "realquote-2adbc.firebasestorage.app",
  'databaseURL': 'https:realquote.firebaseio.com',
  'messagingSenderId': "518666255598",
  'appId': "1:518666255598:web:99c34712247769507347ff",
  'measurementId': "G-6VNG5HC17H"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()



def main(page: ft.Page):
    page.title = "Login Mobile"
    page.padding = 20
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.scroll = ft.ScrollMode.AUTO
    page.theme_mode = ft.ThemeMode.DARK

    # Função de Login
    def login(e):
        try:
            auth.sign_in_with_email_and_password(email_login.value, password_login.value)
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="Login realiazado com sucesso!"
                ),
                bgcolor='green',
                action='OK',
                duration=3000
            )
            page.snack_bar.open = True
            email_login.value = None
            password_login.value = None
            load_main_screen()
            page.update()
        except:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="Email ou senha invalidos!"
                ),
                bgcolor='red',
                action='OK',
                duration=3000
            )
            page.snack_bar.open = True
            page.update()

        page.update()

    # Função para trocar para a tela de cadastro
    def go_to_register(e):
        page.controls.clear()  # Limpa os controles da tela de login
        load_register_screen()  # Carrega a tela de cadastro
        page.update()

    # Função para trocar para a tela de login
    def go_to_login(e):
        page.controls.clear()  # Limpa os controles da tela de cadastro
        load_login_screen()  # Carrega a tela de login
        page.update()

    # Função para cadastro de novo usuário
    def register(e):
        try:

            auth.create_user_with_email_and_password(email_register, password_register)
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="Registrado com sucesso!"
                ),
                bgcolor='green',
                action='OK',
                duration=3000
            )
            page.snack_bar.open = True
            email_register.value = None
            password_register.value = None
            page.update()
        except:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                    value="Algo deu errado!"
                ),
                bgcolor='red',
                action='OK',
                duration=3000
            )
            page.snack_bar.open = True
            page.update()

        page.update()

    # Função para carregar a tela de login
    def load_login_screen():
        # Campos de entrada e botão de login
        global email_login, password_login
        email_login = ft.TextField(label="Nome de Usuário", width=page.window_width * 0.8)
        password_login = ft.TextField(label="Senha", password=True, width=page.window_width * 0.8)

        page.add(
            ft.Column(
                [
                    ft.Text("Login", size=24, weight="bold"),
                    email_login,
                    password_login,
                    ft.ElevatedButton(text="Login", width=page.window_width * 0.8, on_click=login),
                    ft.TextButton("Cadastrar", on_click=go_to_register),  # Botão para tela de cadastro
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )

    # Função para carregar a tela de cadastro
    def load_register_screen():
        global email_register, password_register
        email_register = ft.TextField(label="E-mail", width=page.window_width * 0.8)
        password_register = ft.TextField(label="Senha", password=True, width=page.window_width * 0.8)

        # Campos de entrada e botão de cadastro
        page.add(
            ft.Column(
                [
                    ft.Text("Cadastrar", size=24, weight="bold"),
                    email_register,
                    password_register,
                    ft.ElevatedButton(text="Cadastrar", width=page.window_width * 0.8, on_click=register),
                    ft.TextButton("Voltar para o Login", on_click=go_to_login),  # Botão para voltar ao login
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
    def coin_origin(event):
        global value_coin_origin
        value_coin_origin = event.control.value
    def coin_destination(event):
        global value_coin_destination
        value_coin_destination = event.control.value




    def load_main_screen():
        page.controls.clear()  # Limpa os controles da tela de login
        menubar_coin_origin = ft.Dropdown(
            label="Moeda de Origem",
            helper_text="Selecione a moeda de origem",
            options=[
                ft.dropdown.Option("BRL"),
                ft.dropdown.Option("USD"),
                ft.dropdown.Option("BTC"),
                ft.dropdown.Option("EUR"),
            ],
            on_change = coin_origin
        )
        menubar_coin_destination = ft.Dropdown(
            label="Moeda de Destino",
            helper_text="Selecione a moeda de destino",
            options=[
                ft.dropdown.Option("BRL"),
                ft.dropdown.Option("USD"),
                ft.dropdown.Option("BTC"),
                ft.dropdown.Option("EUR"),
            ],
            on_change=coin_destination
        )


        global text_currency
        global value_conversion


        value_conversion = ft.TextField(label="Digite o valor para a conversão", width=page.window_width * 0.8, keyboard_type=ft.KeyboardType.NUMBER,)
        value_currency = ft.Text("", size=30, weight="bold", color="green")
        text_currency = ft.Text("",size=15, weight="bold", color="white")


        def convert_currency(event):
            selection_coin_origin = value_coin_origin
            selection_coin_destination = value_coin_destination
            currency = get_currency_quote(selection_coin_destination, selection_coin_origin)
            currency = float(currency) * float(value_conversion.value)
            value_currency.value = f"{currency:.2f} {selection_coin_origin}"
            text_currency.value = f"Para ter {value_conversion.value} {selection_coin_destination} você precisa de {currency:.2f} {selection_coin_origin}"
            page.update()



        page.add(
            ft.Column(
                [
                    ft.Text("Bem-vindo!", size=30, weight="bold", color="green"),
                    ft.Text(f"Realize a sua conversão!", size=18),
                    menubar_coin_origin,
                    menubar_coin_destination,
                    value_conversion,
                    ft.ElevatedButton(text="Converter", on_click=convert_currency),
                    value_currency,
                    text_currency
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            )
        )
        page.update()


    # Inicialmente, carrega a tela de login
    load_login_screen()

if __name__ == "__main__":
    ft.app(target=main)