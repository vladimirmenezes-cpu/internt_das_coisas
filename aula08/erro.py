
try:
    idade = int(input("Digite sua idade: "))
    if idade >= 18:
        print("Voce e maior de idade.")
    else:
        print("Voce e menor de idade.")
except:
    print("Ocorreu um erro ao processar a idade. Por favor, insira um valor válido.")
        