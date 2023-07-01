nome = "dANubIA"

print(nome.upper()) # maiusculo
print(nome.lower()) # minusculo
print(nome.title()) # só o primeiro caractere maiusculo
print()

texto = " Ola, mundo    "

print(texto)
print(texto.strip() + ".")    # remove os espaços
print(texto.lstrip() + ".")   # remove os espaços a esquerda
print(texto.rstrip() + ".")   # remove os espaços a direita
print()

menu = "Python"

print("####" + menu + "####")
print(menu.center(14))
print(menu.center(14, "#"))
print("P-y-t-h-o-n")
print("-".join(menu))