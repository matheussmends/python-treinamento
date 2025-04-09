#Paradigma imperativo
#imperare -> comandar

#variaveis, atribuições e sequencia
#C, Fortran, Cobol, Basic, Pascal, Ada, Modula-2
"""
print(30 * "--")
nome = "Gabriel" #variavel global

#palavra chave para definir funções é DEF

def minha_funcao():
    #bloco interno *é conhecido como corpo da função
    nome = "Ana"
    tupla = 2, 5, 6, 7, 9
    print(nome)
    print(tupla)
    if nome == "Ana":
        print("Impressão do bloco interno da condição if")
    for x in tupla:
        print(x)


print(nome)
minha_funcao()"""

"""lista = [1, 2, 3, 4, 5]
print(lista)

retorno = lista.pop()
var1 = print("Ola mundo")
print(lista)
print("Retorno da função pop: ", retorno)
print("Retorno da função print: ", var1)"""

def par_impar():
    numero = 2
    if (numero % 2) == 0:
        print("numero par")
    print("numero impar")


print("""ola mundo""")
print(par_impar())

x = 3
if x == 0:
    print("0")

print("ola")
