"""
# STRING
Todos os métodos de listas também funcionam em Strings
"""

# VARIÁVEIS
texto = "     Curso de progamação com Python (Curso)     "

## Alinhamentos
# print(texto.ljust(50, "-"))
# print(texto.rjust(50, "-"))
# print(texto.center(50, "-"))

## Busca
# print(texto.find("Curso", 0, len(texto))) # se não encontrar, retorna -1
# print(texto.rfind("Curso", 0, len(texto))) # se não encontrar, retorna -1
# print(texto.index("Curso", 0, len(texto))) # se não encontrar, retorna um error
# print(texto.rindex("Curso", 0, len(texto))) # se não encontrar, retorna um error
# print("Curso" in texto)

## Formatação
# print(texto.strip()) # remove os espaço vazios no final e começo da string
# print(texto.replace("Curso", "Estudos"))
# print(texto.capitalize())
# print(texto.upper())
# print(texto.lower())
# print(texto.title())

## Partição
# lista = ["Curso", "de", "desenvolvimento"]
# print(" ".join(lista))

# print(texto.split().split(" "))

## Verificadores
# print("abc123".isalnum())
# print("abc123".isalpha())
# print("abc123".isascii())
# print("abc123".isdecimal())
# print("abc123".isdigit())
# print("abc123".isnumeric())
# print("abc123".isprintable())
# print("abc123".isupper())
# print("abc123".islower())
# print("abc123".istitle())