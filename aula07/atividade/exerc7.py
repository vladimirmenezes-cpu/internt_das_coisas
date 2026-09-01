import random

numero_sorteado = random.randint(1, 20)
tentativas = 0

while True:
    palpite = int(input("Digite um número de 1 a 20: "))
    tentativas += 1

    if palpite < numero_sorteado:
        print("O número sorteado é maior!")
    
    elif palpite > numero_sorteado:
        print("O número sorteado é menor!")
    
    else:
        print(f"Parabéns! Você acertou!")
        print(f"Você precisou de {tentativas} tentativa(s).")
        break