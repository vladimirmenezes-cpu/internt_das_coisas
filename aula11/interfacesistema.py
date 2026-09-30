import customtkinter as ctk

ctk.set_appearance_mode("dark")

def calcular():
    a = float(primeiranota.get())
    b = float(segundanota.getr())
    c = float(terceiranota.get())

    formula = a + b + c / 3

    resultado.configure(text=f"O resultado das notas é: {formula}")


janela = ctk.CTk()
janela.geometry("600x450")
janela.resizable(False,False)
janela.title("Sistema Escolar 2026")
janela.iconbitmap("")

titulo = ctk.CTkLabel(janela,
text="Sistema Escola",
text_color="yellow",
font=("Helvetica",33,"blod"))
titulo.pack(pady=20)

unidade1 = ctk.CTkEntry(janela)