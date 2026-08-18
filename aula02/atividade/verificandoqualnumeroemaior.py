import os 
os.system("cls")

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro:"))

if num1 > num2:
    print(f"O primeiro numero {num1} é maior que o segundo numero {num2}.")
elif num1 < num2:
    print(f"O segundo numero {num2} é maior que o primeiro numero {num1}.")
else:
    print(f"Os numeros {num1} e {num2} sao iguais.")