def imprimirQuadrado():
    numero = int(input("Digite um número: "))
    print(f"Ele ao quadrado é {numero**2}")

def imprimir(msg):
    tamanho = len(msg)+6
    print("-"*tamanho)
    print(msg.center(tamanho))
    print("-"*(tamanho))

imprimir("Início do programa")

imprimirQuadrado()

imprimir("Fim do programa")