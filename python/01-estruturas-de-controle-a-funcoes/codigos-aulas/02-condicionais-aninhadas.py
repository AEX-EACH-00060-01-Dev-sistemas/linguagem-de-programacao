# Declaração de variáveis
idade = int(input("IDADE: "))

# Condição simples (+complexa)
if idade < 18:
    print("Você é menor de idade!")
    if idade >= 16:
        print("Você pode votar!")
    else:
        print("Você não pode votar!")
else:
    if idade > 65 and idade < 100:
        print("Você já pode pegar passe gratuito no ônibus")
    else:
        print(f"Você tem {idade} anos")