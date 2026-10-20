texto = "AQUI ESTOU"

def imprimirQuadrado():
    numero = int(input("Digite um número: "))
    print(texto)

    def imprimirBonito():
        print("-"*20)
        print(f"Raiz quadrada dele é {numero**(1/2)}")
        print("-"*20)

    imprimirBonito()

print("-"*20)
print("Inicio do programa!")
print("-"*20)

imprimirQuadrado()

print("-"*20)
print("Fim do programa!")
print("-"*20)