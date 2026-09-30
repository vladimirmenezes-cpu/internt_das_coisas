import customtkinter as ctk

# Configura o tema visual do aplicativo para o modo escuro ("dark")
ctk.set_appearance_mode("dark")

# Função responsável por ler as notas, calcular a média e exibir o resultado
def calcular():
        a = float(unidade1.get())
        b = float(unidade2.get())
        c = float(unidade3.get())

        formula = (a + b + c) / 3

        if formula >= 5:
            resultado.configure(
                text=f"Média: {formula:.1f} - Aluno Aprovado!!",
                text_color="green"  
            )
        else:
            resultado.configure(
                text=f"Média: {formula:.1f} - Aluno em Recuperação!!",
                text_color="red"   
            )

# Inicializa a janela principal da aplicação
janela = ctk.CTk()
janela.geometry("500x450")
janela.resizable(False, False)
janela.title("Sistema Escolar 2026")
janela.iconbitmap("aula11/ic_school_128_28729.ico")
#-----------------------------

# Rótulo de título estilizado no topo da tela
titulo = ctk.CTkLabel(
    janela,
    text="Sistema Escola",
    text_color="yellow",
    font=("Helvetica", 33, "bold")
)
titulo.pack(pady=20) 
#--------------------------------------

# Campo de entrada para a 1ª nota
unidade1 = ctk.CTkEntry(
    janela,
    width=300,
    height=50,
    border_color="yellow",
    placeholder_text="Digite a sua nota da 1ª Unidade"
)
unidade1.pack(pady=10)
#----------------------------------------

# Campo de entrada para a 2ª nota
unidade2 = ctk.CTkEntry(
    janela,
    width=300,
    height=50,
    border_color="yellow",
    placeholder_text="Digite a sua nota da 2ª Unidade"
)
unidade2.pack(pady=10)
#------------------------------------------

# Campo de entrada para a 3ª nota
unidade3 = ctk.CTkEntry(
    janela,
    width=300,
    height=50,
    border_color="yellow",
    placeholder_text="Digite a sua nota da 3ª Unidade"
)
unidade3.pack(pady=10)
#------------------------------------------

# Botão de ação para acionar o cálculo da média
botao = ctk.CTkButton(
    janela,
    width=200,
    height=50,
    text="Resultado",
    fg_color="yellow",         
    text_color="black",        
    hover_color="#cccc00",      
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