altura = float(input("fale sua altuar: "))
peso = float(input("fale seu peso"))

imc = peso / (altura * altura)

print(f"seu IMC é: {imc}")

if imc < 18.5:
    print("Abaixo do peso")
elif imc < 25:
    print("Peso normal")
elif imc < 30:
    print("Sobrepeso")
else:
    print("Obesidade")
