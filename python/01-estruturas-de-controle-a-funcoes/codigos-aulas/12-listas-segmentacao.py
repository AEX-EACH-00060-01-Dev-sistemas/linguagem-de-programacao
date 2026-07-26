# VARIÁVEIS IMPORTANTES
lista = [10,20,30,40,50]

## PADRÃO
init = 0 # começo
end = len(lista) # a função len devolve o tamanho da lista; final
steps = 1 # "pulos"

# De 0 até o tamanho da lista
print(lista[init:end:steps])

## DE 2 EM 2
steps = 2

print(lista[init:end:steps])

# De 0 até tamanho da lista - 4
end = len(lista) - 4
steps = 1

print(lista[init:end:steps])

# Da 3° posição até o final da lista
init = 2
end = len(lista)

print(lista[init:end:steps])