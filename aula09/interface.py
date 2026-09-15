import customtkinter as ctk

ctk.set_appearance_mode("system")

#janela -------------
janela = ctk.CTk()

#definir o tamanho da janela
janela.geometry("500x500")

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














janela.mainloop()