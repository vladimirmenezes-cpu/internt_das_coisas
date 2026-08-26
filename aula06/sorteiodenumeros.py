import os, random,time

numero_secreto = random.randint(1, 100)
tentativas = 0

while True:
    numero = int(input('Digite o numero secreto: '))
    tentativas +=1
    if(numero == numero_secreto):
        print(f"Parabens voce acertou o numero em {tentativas}")
        break
    elif(numero_secreto>numero):
        print(f"O numero secereto é maior!! - {tentativas} tentativas")
        time.sleep(2)
        os.system('cls')
    else:
        print(f"o numero secreto é menor!! - {tentativas} Tentativas!")
        time.sleep(2)
        os.system('cls')