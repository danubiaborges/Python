# Desafio
# Paulinho tem em suas mãos um novo problema. Agora a sua professora lhe pediu que construísse um programa para verificar, à partir de dois valores muito grandes A e B, se B corresponde aos últimos dígitos de A.

# Entrada
# A entrada consiste de vários casos de teste. A primeira linha de entrada contém um inteiro N que indica a quantidade de casos de teste. Cada caso de teste consiste de dois valores A e B maiores que zero, cada um deles podendo ter até 1000 dígitos.

# Saída
# Para cada caso de entrada imprima uma mensagem indicando se o segundo valor encaixa no primeiro valor, confome exemplo abaixo.

N = input()
n = int(N)

while(n > 0):
    A, B = input().strip().split(' ')

    if(0 < len(A) <= 1000) and (0 < len(B) <= 1000):
        if A.endswith(B):
            print("encaixa")
        else:
            print("nao encaixa")
    else:
      print("nao encaixa")
      
    n -= 1
    