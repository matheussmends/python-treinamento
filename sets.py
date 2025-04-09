"""Listas: Coleção ordenada, mutável e que permite valores duplicados.
Tuplas: Coleção ordenada, imutável e que permite valores duplicados.
Dicionários: Coleção não ordenada, mutável e que não permite valores duplicados
Sets: Coleção não ordenada, imutável e que não permite valores duplicados.
"""
#Os sets também são conhecidos como conjuntos

"""conjunto = {"item1", 3, True, 4.7, "são paulo"}
print(type(conjunto))
print(conjunto)
print(len(conjunto))"""

"""conjunto = set((3, 7, 9, 5))
print(conjunto)
print(type(conjunto))"""

"""conjunto = {3, 7, 9, 5}
conjunto[0] = 4
print(conjunto)"""

# Acessando os itens do meu set

"""conj = {"item1", "item2", "item3", "item4", "item5"}

for x in conj:
    print(x)"""

"""conjunto = {"item", 6, 8 ,9, 1}
print(item in conjunto)
"""

#Adicionou elementos

"""set1 = {"item1", "item2", "item3"}
print(set1)
set1.add("item5")
print(set1)
set1.add(8)
set1.add(True)
print(set1)"""

"""set1 = {4, 5, 7, 8, 9, 1}
set1.update((1, 4, 7, 8, 9, 3, "item5", "item6"))
print(set1)"""

#Removendo elementos

"""set1 = {1, 3, 4, 5, 7, 8, 9, 'item5', 'item6'}
print(set1)

set1.remove("item5")
set1.discard("item6")
print(set1)

set1.clear()
print(set1)
"""

#Utilizando funcões principais dos Sets

"""conjunto1 = {1, 5, 8, 9}
conjunto2 = {3, 6, 2}

conjunto1.update(conjunto2)
print(conjunto1)"""

"""conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

conjunto1.intersection_update(conjunto2)
print(conjunto1)"""

conjunto1 = {1, 5, 3, 2}
conjunto2 = {3, 6, 2}

conjunto1.symmetric_difference_update(conjunto2)
print(conjunto1)

#Diagrama de Venn
