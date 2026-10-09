import customtkinter as ctk

# Configura o tema visual do aplicativo para o modo escuro ("dark")
ctk.set_appearance_mode("dark")

# Função responsável por ler as notas, calcular a média e exibir o resultado
def calcular():
        a = float(unidade1.get())
        b = float(unidade2.get())

        formula = (a + b) / 2

        if formula < 5:
            resultado.configure(
                text=f"Média: {formula:.1f}\nSituação: REPROVADO",
                text_color="red"  
            )
        elif formula >= 5 and formula < 7:
            resultado.configure(
                text=f"Média: {formula:.1f}\nSituação: RECUPERAÇÃO",
                text_color="yellow"  
            )
        else:
            resultado.configure(
                text=f"Média: {formula:.1f}\nSituação: APROVADO",
                text_color="green"
            )
        

# Inicializa a janela principal da aplicação
janela = ctk.CTk()
janela.geometry("400x450")
janela.resizable(False, False)
janela.title("Resultado academico")
janela.iconbitmap("Prova/chalkboard_icon-icons.com_54408.ico")
#-----------------------------


legenda_aluno = ctk.CTkLabel(janela, text="Nome do Aluno:", font=("Arial", 12, "bold"))
legenda_aluno.pack()

#campo de entrada para o nome do aluno
nome_aluno = ctk.CTkEntry(
    janela,
    width=350,
    height=50,
    border_color="white",
    placeholder_text="Digite o nome do aluno"
)
nome_aluno.pack(pady=10)



legenda_nota1 = ctk.CTkLabel(janela, text="Nota 1:", font=("Arial", 12, "bold"))
legenda_nota1.pack()
# Campo de entrada para a 1ª nota
unidade1 = ctk.CTkEntry(
    janela,
    width=350,
    height=50,
    border_color="white",
    placeholder_text="Digite a sua nota da 1"
)
unidade1.pack(pady=10)
#----------------------------------------



legenda_nota2 = ctk.CTkLabel(janela, text="Nota 2:", font=("Arial", 12, "bold"))
legenda_nota2.pack()
# Campo de entrada para a 2ª nota
unidade2 = ctk.CTkEntry(
    janela,
    width=350,
    height=50,
    border_color="white",
    placeholder_text="Digite a sua nota da 2"
)
unidade2.pack(pady=10)
#------------------------------------------



# Botão de ação para acionar o cálculo da média
botao = ctk.CTkButton(
    janela,
    width=350,
    height=50,
    text="CALCULAR RESULTADO",
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