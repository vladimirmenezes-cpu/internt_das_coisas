import os
os.system("cls")

idade = int(input("Digite a sua idade:"))

if idade <= 12:
    print("voce é uma criança.")
elif  13 <= idade <= 17:
    print("voce é um adolescente.")
elif 18 <= idade <= 59:
    print("voce é um adulto.")
else:
    print("voce é um idoso.")
