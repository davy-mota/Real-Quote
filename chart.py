import matplotlib
matplotlib.use('Agg')  # Usar o backend não gráfico
import flet as ft
import matplotlib.pyplot as plt
import io
import base64
from get_price import get_currency_quote_week, get_currency_quote_annual


# Função que gera os dados para o gráfico
def obter_dados():
    # Exemplo de dados simples

    x = list(range(1, 361))
    y = get_currency_quote_annual("USD", "BRL")
    return x, y


# Função para gerar o gráfico e convertê-lo em uma imagem Base64
def gerar_imagem_do_grafico(x, y):
    # Criando o gráfico com Matplotlib
    plt.figure(figsize=(8, 4))
    plt.plot(x, y, marker="o", linestyle="-", color="b", label="Valor")
    plt.title("Gráfico de Linha", fontsize=14)
    plt.xlabel("Eixo X", fontsize=12)
    plt.ylabel("Eixo Y", fontsize=12)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.tight_layout()

    # Salvar a imagem do gráfico em um buffer de memória
    buffer = io.BytesIO()
    plt.savefig(buffer, format="png")
    buffer.seek(0)
    plt.close()

    # Converter a imagem para Base64
    imagem_base64 = base64.b64encode(buffer.getvalue()).decode("utf-8")
    return imagem_base64

# Função principal do Flet
def main(page: ft.Page):
    page.title = "Gráfico do Matplotlib no Flet"
    page.padding = 20

    # Obter os dados do gráfico através da função
    x, y = obter_dados()

    # Gerar a imagem do gráfico em formato Base64
    img_base64 = gerar_imagem_do_grafico(x, y)

    # Exibir o gráfico no Flet como uma imagem
    grafico = ft.Image(
        src_base64=f"{img_base64}",  # Passar somente a string Base64 sem o prefixo
        fit=ft.ImageFit.CONTAIN,
        width=600,
        height=400,
    )

    # Adicionar o gráfico na página
    page.add(
        ft.Column(
            [
                ft.Text("Gráfico gerado com Matplotlib", size=24, weight="bold"),
                ft.Text(get_currency_quote_week("USD", "BRL"), size=24, weight="bold"),
                grafico,
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    )

# Executar o app Flet
if __name__ == "__main__":
    ft.app(target=main)
