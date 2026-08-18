import os
os.system("cls")

tentativa = input("Digite a senha para abrir a porta:")

if tentativa == "python123":
    print("A porta foi aberta com sucesso!")
else:
    print("Senha incorreta. A porta não foi aberta.")