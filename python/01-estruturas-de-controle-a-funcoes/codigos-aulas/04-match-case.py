# Definição de variáveis
mes = str(input("Digite um mês: "))

# Match case simples
match mes:
    case "janeiro":
        print("JANEIRO")
    case "fevereiro":
        print("FEVEREIRO")
    case "março":
        print("MARÇO")
    case _:
        print("OUTROS ELEMENTOS")