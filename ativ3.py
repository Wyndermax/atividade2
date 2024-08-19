def obter_float(msgm):
    while True:
        try:
            valor = float(input(msgm))
            if valor <= 0:
                print("O valor ser maior que zero, tente novamente.")
            else:
                return valor
        except ValueError:
            print("Informação invalida! Favor, insira um número válido.")

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc
peso = obter_float("Digite seu peso em Kg: ")
altura = obter_float("Digite sua altura em metros: ")

imc = calcular_imc(peso, altura)

print(f"Seu IMC é: {imc:.2f}")

if imc < 18.5:
    print("Você esta abaixo do peso.")
elif 18.5 <= imc <24.9:
    print("Você está com seu peso em dia.")
elif 25 <= imc < 29.9:
    print("Você está acima do seu peso.")
else:
    print("Cuidado, você está na obsidade.")
