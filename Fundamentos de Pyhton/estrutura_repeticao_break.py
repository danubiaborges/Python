while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break
    
    if numero % 2 == 0:
        continue

    print(numero)

# break para o laço
for numero in range(100):

    if numero == 12:
        break

    print(numero, end=" ")

print()

# continue pula o número, nesse caso só exibe os ímpares
for numero in range(100):

    if numero % 2 == 0:
        continue

    print(numero, end=" ")




