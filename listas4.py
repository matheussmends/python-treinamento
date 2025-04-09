"""
# index     0        1        2
lista = ["carro", "barco", "avião"]
print(lista)


texto = "meunome@gmail.com"
lista2 = list(texto)
print(lista2)

texto = texto.split('@')
print(texto)


# lista.insert(0, "bicicleta")
# print(lista)

lista.append(["bicicleta", "navio"])
# lista.extend(["bicicleta", "Navio"])

print(lista)
print(len(lista))
for x in range(len(lista)):
    print(x, lista[x])
"""

"""
# index     0        1        2
lista = ["carro", "barco", "avião"]
print(lista)
"""
# lista.pop()  serve para remover o ultimo elemento.
# lista.pop(0) serve para remover o index mencionado.
# lista.remove("barco") serve para remover um elemento específico. 

# del lista  serve para deletar.
#del lista[0]
# carrinho_de_compras.clear()  serve para apagar todos os elementos do carrinho mas não apaga o carrinho.

"""
carrinho_de_compras = ["pão", "carne", "verduras"]
#sort  serve para a ordenação
carrinho_de_compras.sort()
"""

"""
lista = [1, 50, 23, 67, 100]
print(lista)

#reverse  serve para reverter a ordem citada, mas sem estar ordenada.
# lista.sort(reverse = True)
lista.reverse()
print(lista)
"""


lista = ["Ana", "Pedro", "Marta", "Clarice", "beatriz", "ana clara"]
print(lista)

lista.sort(key = str.lower)
print(lista)

