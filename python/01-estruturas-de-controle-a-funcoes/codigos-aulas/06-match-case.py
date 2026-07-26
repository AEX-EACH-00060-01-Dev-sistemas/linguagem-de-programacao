# Definição de variáveis
mes = str(input("Digite um mês: "))
dia = int(input("Digite um dia: "))

# Match case simples
match mes:
    case "janeiro" | "março" | "maio" | "julho" | "agosto" | "outubro" | "dezembro" if dia >= 1 and dia <= 31:
        print(f"{dia}/{mes} (Termina dia 31)")
    case "abril" | "junho" | "setembro" | "novembro" if dia >= 1 and dia <= 30:
        print(f"{dia}/{mes} (Termina dia 30)")
    case "fevereiro" if dia >= 1 and dia <= 28:
        print(f"{dia}/{mes} (Fevereiro)")
    case _:
        print(f"Inválido")