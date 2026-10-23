import customtkinter as ctk
import qrcode
from PIL import Image

ctk.set_appearance_mode("dark")

# Janela--------------
janela = ctk.CTk()
janela.geometry("400x500")
janela.title("Sistema gerador de QRCODE")
janela.resizable(False, False)
#--------------------------



# Elementos da janela ------------
titulo = ctk.CTkLabel(
    janela,
    text="Sistema Gerador de Qrcode",
    text_color="yellow",
    font=("Arial", 30) 
)
titulo.pack(pady=10)
#---------------

# CAIXA-----------------
entrada = ctk.CTkEntry(
    janela,
    width=300,
    height=40,
    placeholder_text="Digite a URL ou o pix"
)
entrada.pack(pady=10)
#-------------------

# Criando o botão----------------
botao = ctk.CTkButton(
    janela,
    width=120,
    height=30,
    fg_color="white",
    text="Gerar Qrcode",
    text_color="black",
    hover_color="silver",
    cursor="hand2",
)
botao.pack(pady=10)
#---------------------

# Resultado ------------------------
resultado = ctk.CTkLabel(
    janela,
    text=""
)
resultado.pack(pady=20)

janela.mainloop()