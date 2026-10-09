import customtkinter as ctk

# Configura o tema visual do aplicativo para o modo escuro ("dark")
ctk.set_appearance_mode("dark")

# Função responsável por ler as notas, calcular a média e exibir o resultado
def calcular():
        a = float(quantidadediarias.get())
        b = float(valordiaria.get())

        valor = a * b

        if a >= 5:
            valordodesconto = valor * 0.9
            valortotal = valor - valordodesconto
            resultado.configure(
                text=f"Hospedagem: R${valor:.1f}\nDesconto: R${valordodesconto:.1f}\nTotal a pagar: R${valortotal:.1f}",
                text_color="white"  
            )
        else:
            resultado.configure(
                text=f"Hospedagem: R${valor:.1f}\nDesconto: R$00,00\nTotal a pagar: R${valor:.1f}",
                text_color="white"
            )
        

# Inicializa a janela principal da aplicação
janela = ctk.CTk()
janela.geometry("400x500")
janela.resizable(False, False)
janela.title("Resultado de Hotel")
janela.iconbitmap("Prova/travel-holiday-vacation-328_89069.ico")
#-----------------------------


legenda_aluno = ctk.CTkLabel(janela, text="Nome do Hóspede:", font=("Arial", 12, "bold"))
legenda_aluno.pack()

#campo de entrada para o nome do aluno
nome_aluno = ctk.CTkEntry(
    janela,
    width=350,
    height=50,
    border_color="white",
    placeholder_text="Digite o nome do Hóspede"
)
nome_aluno.pack(pady=10)



quantidadediarias1 = ctk.CTkLabel(janela, text="Quantidade de diárias:", font=("Arial", 12, "bold"))
quantidadediarias1.pack()
# Campo de entrada para a 1ª nota
quantidadediarias = ctk.CTkEntry(
    janela,
    width=350,
    height=50,
    border_color="white",
    placeholder_text="Digite a quantidade de diárias"
)
quantidadediarias.pack(pady=10)
#----------------------------------------



valordiaria1 = ctk.CTkLabel(janela, text="Valor da Diária(R$):", font=("Arial", 12, "bold"))
valordiaria1.pack()
# Campo de entrada para a 2ª nota
valordiaria = ctk.CTkEntry(
    janela,
    width=350,
    height=50,
    border_color="white",
    placeholder_text="Digite o valor da diária"
)
valordiaria.pack(pady=10)
#------------------------------------------



# Botão de ação para acionar o cálculo da média
botao = ctk.CTkButton(
    janela,
    width=350,
    height=50,
    text="CALCULAR HOSPEDAGEM",
    fg_color="#0084ff",
    text_color="white",
    hover_color="#004cff",
    font=("Helvetica", 23, "bold"),
    command=calcular
)
botao.pack(pady=20)
#---------------------------------

# Rótulo reservado para exibir o resultado final na tela
resultado = ctk.CTkLabel(
    janela,
    text="",
    text_color="white",
    font=("Arial", 18, "bold")
)
resultado.pack(pady=10)
#-----------------------------------------------

janela.mainloop()