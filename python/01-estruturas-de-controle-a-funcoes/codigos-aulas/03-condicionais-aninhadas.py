# Declaração de variáveis
idade = int(input("IDADE: "))

# Condição simples (+complexa)
if idade < 18:
    print("Você é menor de idade!")
    if idade >= 16:
        print("Você pode votar!")
    else:
        print("Você não pode votar!")
elif idade > 65:
    print("Você já pode pegar passe gratuito no ônibus")
else:
    print("Sua idade está entre 18 e 65")