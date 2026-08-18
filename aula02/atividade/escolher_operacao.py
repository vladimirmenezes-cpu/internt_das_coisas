import os 
os.system("cls")

num1 = int(input("Digite o primeiro numero inteiro: "))
num2 = int(input("Digite o segundo numero inteiro:"))
operacao = input("Digite a operação desejada (+, -, *, /): ")

if operacao == "+":
    resultado = num1 + num2
    print(f"O resultado da soma é: {resultado}")
elif operacao == "-":
    resultado = num1 - num2
    print(f"O resultado da subtração é: {resultado}")
elif operacao == "*":
    resultado = num1 * num2
    print(f"O resultado da multiplicação é: {resultado}")
elif operacao == "/":
    if num2 != 0:
        resultado = num1 / num2
        print(f"O resultado da divisão é: {resultado}")
    else:
        print("Erro: Divisão por zero não é permitida.")
else:
    print("Operação inválida. Por favor, escolha entre +, -, * ou /.")