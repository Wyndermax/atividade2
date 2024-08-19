# tabuada

while True:
    tab = int(input("Digite o número para criação da tabuada ou '0' para sair: "))
    
    if tab == 0:
        print("Até mais...")
        break

    print(f"Tabuada do número '{tab}':")
    for a in range(1, 11):
        result = tab * a
        print(f"{tab} x {a} = {result}")
