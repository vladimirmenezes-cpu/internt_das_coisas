# 2) O Somador Infinito (while True + append)
# Crie um programa que peça números ao usuário indefinidamente.
# Se o usuário digitar 0, o programa para.
# Cada número digitado (exceto o 0) deve ser guardado em uma lista.
# No final, mostre a lista completa e a soma de todos os itens usando sum().

numeros_finais = []

while True:
    numero = int(input(f'Digite numeros que deseja somar, para parar digite 0: '))
    if(numero ==0):
        break
    else:
        numeros_finais.append(numero)

soma = sum(numeros_finais)

print(f"Soma total da lista {soma:.2f} \nLista total dos numeros {numeros_finais:.2f}.")