import os
os.system("cls")

temperatura = float(input("Digite a temperatura do local: "))

if temperatura < 15:
    print("Está frio.")
elif  15 <=temperatura <= 25:
    print("Está agradável.")
else:
    print("Está calor.")