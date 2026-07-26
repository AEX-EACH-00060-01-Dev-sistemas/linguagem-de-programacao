# Definição de variáveis
mes = str(input("Digite um mês: "))

# Match case simples
match mes:
    case "janeiro" | "fevereiro" | "março":
        print("Os três primeiros meses do ano")
    case _:
        print("OUTROS ELEMENTOS")