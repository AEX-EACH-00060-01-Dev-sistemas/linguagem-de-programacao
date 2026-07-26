# BREAK
print("BREAK")
num = 0
while num < 5:
    num += 1

    if num == 3:
        break

    print(num, end=" ")

# CONTINUE
print("")
print("CONTINUE")
for num in range(5): # 0 1 2 3 4
    if num == 3:
        print("Encontrei o 3")
        # Executa o continue, pulando para o próximo laço
        continue
    else:
        print(num)

    print("Estou abaixo do IF")

# PASS
print("PASS")
for contador in range(10):
    pass