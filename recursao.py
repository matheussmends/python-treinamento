# Código para reduzir um número inteiro de 1 em 1.

"""def reduzirNumero(numeroInt):
    while numeroInt > 0:
        print(numeroInt)
        numeroInt -= 1


reduzirNumero(10)"""

"""
1 - chegar se o número não é igual a 0.
2 - se ele não for igual a 0 - reduzir  1 unidade

5
 4 (n - 1)
  3 (4 - 1)
   2 (3 - 1)
    1 (2 - 1)
     0 (1 - 1)
"""

"""def reduzirNumero(numeroInt):
    print(numeroInt)
    if numeroInt > 0:
        # N - 1
        reduzirNumero(numeroInt - 1)

reduzirNumero(5)"""

# Fatorial sem recursão!!
def fatorialS(numero):
    fatorial = 1
    if numero == 0:
        return 1
    else:
        for x in range(1, numero + 1):
            fatorial *= x
        return fatorial

print(fatorialS(5))

# Fatorial - Solução recursiva
def fatorialR(numero):
    if numero == 0: # Critério de parada
        return 1
    else:
        # parâmetro da chamada recursiva
        return numero * fatorialR(numero - 1)


print(fatorialR(3))
"""
5! = 5 * 4!
   = 5 * 4 * 3!
   = 5 * 4 * 3 * 2!
   = 5 * 4 * 3 * 2 * 1!


3! = 3 * 2 * 1
   = 3 * 2!
2! = 2 * 1
   = 2 * 1!
1! = 1
0! = 1

"""