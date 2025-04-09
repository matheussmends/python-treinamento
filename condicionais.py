"""
Python - Comandos de controle condicional

if, else, e elif -> (else if)
"""

"""
x = 3
y = 3

if y > x:
    print("y eh maior do que x")
# "if" Verifica uma condição se for verdadeira.
elif y < x:
    print("y eh menor do que x")
# "elif" verifica outra condição caso a condição do "if" seja falsa.
else:
    print("y nao eh maior nem menor do que x")
# "else" So Sera executado quando tds as condiçoes "if" e "elif" forem falsas.

print("Código fora do bloco condicional")
print(y > x)
print(y < x)
print(y == x)
"""

a = 8
b = 3
c = 2

"""if b > a: print("b eh maior que a")
print("Codigo fora do bloco if")"""

"""print("B") if b < a else print("A") #Operador ternário, Expressões Condicionais """

if a > b:
    if a > c:
        print("A eh maior que B e que C")
