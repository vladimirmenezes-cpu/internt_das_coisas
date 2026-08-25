# 5) Validação de Dados com Laço Indeterminado (Estruturas de Repetição)
# Enunciado: Escreva um programa que simule o cadastro de uma senha. O
# programa deve solicitar que o usuário digite uma senha de 4 dígitos numéricos.
# • Enquanto o usuário digitar uma senha que não tenha exatamente 4
# caracteres ou que não seja composta apenas por números, o programa
# deve exibir "Senha Inválida" e solicitar novamente.
# • Quando a senha for válida, exibir "Senha cadastrada com sucesso".
# Dica: Use while e a função len() para verificar o comprimento.

while True:
    senha = input("Digite a senha de 4 digitos:")

    if len(senha) == 4 and senha.isdigit():
        print("Cadastrada com sucesso")
        break
    else:
        print("Senha invalida")
