# Verificação de Palíndormo

def eh_palindromo(frase):
    frase_limpo = ''.join(frase.lower().split())
    return frase_limpo == frase_limpo[::-1]

while True:
    frase = input("Digite uma palavra ou frase (ou digite 'sair' para encerrar): ")
    if frase.lower() == 'sair':
        print("Encerrando, até mais!")
        break

    if eh_palindromo(frase):
        print("Isto é um palíndromo!")
    else:
        print("Não é um palíndromo.")
