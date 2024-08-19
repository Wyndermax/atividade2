# Contagem de vogais

while True:
    frase = input("Digite uma, ou 'sair' para finalizar: ")

    if frase.lower() == 'sair':
        print("Até mais...")
        break

    frase = frase.lower()

    vogais = 'aeiou'

    contagem = 0

    for letra in frase:
        if letra in vogais:
            contagem += 1

    print(f"Esta frase contém {contagem} vogais.")
