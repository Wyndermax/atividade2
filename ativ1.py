#Calculando o Fatorial

def calcular_fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial

def main():
    while True:
        try:
            num = int(input("Digite um número inteiro: "))
            if num < 0:
                print("Fatorial e números negativos não combinam. ")
            else:
                result = calcular_fatorial(num)
                print(f"O fatorial de {num} é {result}")
                break
        except ValueError:
            print("Favor, digite um número inteiro corretamente.")

if __name__=="__main__":
    main()
