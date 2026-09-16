import customtkinter as ctk 

ctk.set_appearance_mode("dark")

#Funcoes

def calcular():
    d = int(distancia.get())
    c = float(consumo.get())
    p = float(preco.get())

    formula = (d/c)*p

    resultado.configure(text=f"O valor para a viagem é de R$ {formula:.2f}")

#--------------------------



# JANELA ------------
janela = ctk.CTk()
janela.geometry("500x400")
janela.resizable(False, False)
janela.title("Calculadora de viagem!")
janela.iconbitmap("aula10/icon-icons.ico")

#Corpo da janela ------------------

titulo = ctk.CTkLabel(janela,
text="APP VIAGEM",
text_color="white",
font=("Helvetica",33,"bold"))
titulo.pack(pady=20)

#------------

#criando login

distancia = ctk.CTkEntry(janela,
width=400,
height=50,
border_color="white",
placeholder_text="Digite a distancia da viagem em KM!")
distancia.pack()

#---------------

#Criando consumo

consumo = ctk.CTkEntry(janela,
width=400,
height=50,
border_color="white",
placeholder_text="Digite o consumo do seu veiculo",)
consumo.pack(pady=29)

#-----------------------

#criando combustivel

preco = ctk.CTkEntry(janela,
width=400,
height=50,
border_color="white",
placeholder_text="Digite o preço atual do combustivel!",)
preco.pack()

#---------------------

#criando botao

botao = ctk.CTkButton(janela,
width=200,
height=50,
text="Calcular Gasto",
fg_color="#f06979",
text_color="black",
cursor ="spider",
font=("helvetica", 23, "bold"),
command=calcular)
botao.pack(pady=10)

#------------------

#CRIANDO RESULTADO -------------

resultado = ctk.CTkLabel(janela,
text='',
text_color="white",
font=("arial",20))
resultado.pack(pady=10)


























janela.mainloop()