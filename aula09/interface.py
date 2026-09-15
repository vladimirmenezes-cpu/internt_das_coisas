import customtkinter as ctk

ctk.set_appearance_mode("system")

#janela -------------
janela = ctk.CTk()

#definir o tamanho da janela
janela.geometry("500x300")

#definir se a janela pode ser redimensionada
janela.resizable(False, False)

#definir o título da janela
janela.title("Sistema de acesso - 2026")

#definir o ícone da janela
janela.iconbitmap('aula09/Accesssystem_783.ico')
#-------------------------------

#Corpo da janela -----------------

#criando um label
titulo = ctk.CTkLabel(janela,
text="sistema de login",
text_color="black",
font=("sans", 53, "bold"))

#chamando a variável titulo para aparecer na tela
titulo.pack()

#----------------

#criando login 

login = ctk.CTkEntry(janela,
width=400,
height=50,
border_color="black",
placeholder_text="Digite seu login")
login.pack(pady=31)

#--------------------

#criando senha

senha = ctk.CTkEntry(janela,
width=400,
height=50,
border_color="black",
placeholder_text="Digite sua senha",
show="*")
senha.pack()

#--------------------

#criando botão

botao = ctk.CTkButton(janela,
width=200,
height=50,
text="Acessar",
fg_color="blue",
text_color="white",
cursor ="spider",
font=("sans", 20, "bold"))
botao.pack(pady=30)

#-----------------------------












janela.mainloop()