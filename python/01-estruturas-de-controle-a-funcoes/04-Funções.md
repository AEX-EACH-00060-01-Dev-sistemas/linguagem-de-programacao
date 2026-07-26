# FUNÇÕES
Pensa na seguinte situação: você está fazendo um programa que recebe uma temperatura em fahrenheit, mas o restante do código precisa da temperatura em celsius. Se precisar converter apenas algumas vezes, não tem problema. Vejamos o código abaixo:
```pyhton
temperatura1 = 100
temperatura2 = 255
temperatura3 = 300

# Converter temperaturas de fahrenheit para celsius
celsius1 = (temperatura1-32)*5/9
celsius2 = (temperatura2-32)*5/9
celsius3 = (temperatura3-32)*5/9
```

Pode-se parecer simples em primeira vista, mas imagina fazer isso milhares de vezes! É o mesmo código sendo repetido diversas vezes, e para fazer manutenção depois se torna cansativo ter que mudar um a um (imagina o celsius começar a ser "apenas" 5 vezes maior que o feahrenheit, ia ser muito trabalhoso mudar toda a fómula para colocar o `5*` em cada temperatura).

Aqui que entra as **FUNÇÕES**! Elas são blocos de códigos que podem ser chamados toda fez que precisar e que faz uma certa ação, economizando linhas de código. Veja sua sintaxe abaixo:
```python
def acao():
    print("-"*20) # aqui vai printar 20 vezes o sinal negativo (-)
    print("Uma mensagem".center(20)) # centraliza o texto em 20 espaços
    print("-"*20)
```

O bloco de cima é uma função, em que a palavra reservada `def` indica isso. O `acao` indica o nome da função que vai ser usado para invocar ela. Os parênteses (`()`) completam a sintaxe da função, e eles são sados para passar parâmetros (informações que serão usadas na função). Quando não é escrito alguma parâmetro, e que a função não precisa de um.

Para invocar uma função, chama o nome dela com os parênteses: `acao()`. O exemplo completo fica assim:
```python
def acao():
    print("-"*20) # aqui vai printar 20 vezes o sinal negativo (-)
    print("Uma mensagem".center(20)) # centraliza o texto em 20 espaços
    print("-"*20)

acao() # chamando a função
```

## Parâmetros
Como dito anteriormente, toda a função pode possuir seus parâmetros, e eles são usados dentro da função. Podemos fazer uma função chamada `ao_quadrado` que vai receber um número como parâmetro e imprimir o número ao quadrado:
```python
def ao_quadrado(numero):
    x = numero*numero
    print(f"{numero} elevado a 2 é {x}")

ao_quadrado(10) # 100
ao_quadrado(0) # 0
ao_quadrado(2) # 4
```

Veja que quando passamos o 10 entre os parênteses, ele é "jogado" dentro de `numero` e é usado dentro da função. Isso acontece para os outros números.

Não ficamos limitados em dois parâmetros, podemos escrever quantos quiser, como exemplo uma função que calcula a soma de 3 valores:
```python
def add3(x1,x2,x3):
    print(x1+x2+x3)

add3(10,20,50) # 80
```

Mas caso queira passar apenas dois, e não os três, podemos ter os valores padrões para os parâmetros:
```python
def add3(x1,x2,x3=0):
    print(x1+x2+x3)

add3(10,20) # 30
```

Também podemos indicar qual é a ordem dos parâmetros que queremos:
```python
def add3(x1,x2,x3):
    print(x1+x2+x3)

add3(x2=10,x3=20, x1=50) # 80
```

## Escopo
Tá, mas dá para guardar os valores que geramos dentros das função em variáveis? SIM, mas antes vamos entender o que seria um escopo e depois vamos falar dos `retornos`!

O escopo é a delimitação de um bloco basicamente. Veja o exemplo abaixo:
```python
def funcao1():
    # Escopo 1
    x = 10
    print(x)

def funcao2():
    # Escopo 2
    y = 20
    print(y)

def funcao3():
    # Escopo 3
    z = 40
    print(z)

# ESCOPO GLOBAL
numero = 40

if numero > 50:
    # Escopo do IF
    print("Maior que cinquenta")
else:
    # Escopo do else
    print("Menor ou igual a 50")

for c in range(5):
    # Escopo do for
    print(c)

while(numero < 50):
    # escopo do while
    print(numero)
    numero+=1
    if(numero == 50):
        # escopo do if
        print("Numero maior que 50")
```

Podemos acima ver diversos tipos de escopos, em que cada uma das funções, laços e condicionais tem o seu. Temos também um **escopo global**, que seria o que engloba tudo e todos os outros escopos podem acessar livremente ele, contanto que o que se queira já tenha sido declarado antes.

Temos uma hierarquia de escopos: aqueles mais para fora não podem acessar os dados dos mais internos, e isso se dá por conta de não puderem "enxergar" esse outra camada. Todavia, os escopos mais para dentro podem acessar os valores dos mais externos, pois eles conseguem "exerguar" os de fora.

```python
x = 10
def funcao():
    y = 20
    print(y*x) # 200

funcao()
print(y) # o Python reclama que o y não foi declarado e não executa o código
```

## Retorno `(return)`
E caso queira guardar o resultado da função para usar mais tarde? A forma mais recomendável é a função retornar o valor gerado em uma variável através da palavra `return`:
```python
def ao_quadrado(numero):
    x = numero*numero
    return x

x = ao_quadrado(10) # 100
y = ao_quadrado(4) # 16
```

O `return`, como o nome já diz, retorna um resultado qualquer, pode ser texto, número ou até mesmo outra função.

