# Indentação e blocos

# Python usa indentação (espaços) para definir blocos
x = 10
if x > 5:
    print("Maior que 5")  # este print faz parte do bloco
print("Fim")  # fora do bloco

# -----------------------------------------------
# Estruturas condicionais

idade = 18

if idade >= 18:
    print("Maior de idade")
elif idade >= 13:
    print("Adolescente")
else:
    print("Criança")

# operador ternário (condição em uma linha)
status = "adulto" if idade >= 18 else "menor"
print(status)

# -----------------------------------------------
# Estruturas de repetição

# while -> repete enquanto condição for True
contador = 0
while contador < 3:
    print("Contagem:", contador)
    contador += 1

# for -> percorre uma sequência (lista, string, range)
for i in range(5):  # de 0 até 4
    print("Número:", i)

# for com lista
frutas = ["maçã", "banana", "uva"]
for fruta in frutas:
    print("Fruta:", fruta)

# break -> interrompe o loop
for n in range(10):
    if n == 5:
        break
    print("n =", n)

# continue -> pula para a próxima iteração
for n in range(5):
    if n == 2:
        continue
    print("n (sem 2) =", n)