"""Listas : Coleção ordenada, mutável e que permite valores duplicados
Tuplas: Coleção ordenada, imutável e que permite valores duplicados
Dicionários: Coleção não ordenada, mutável e que não permite valores duplicados."""

#index     0        1         2
lista = ["item2", "item3", "item2"]
tupla = ("item1", "item2", "item1")

#chave:valor
dicio = {"chave1": "Gabriel", "chave2": 1993, "chave3": True}
print(dicio)

dicionario = {
    "nome": "Matheus",
    "idade": 25,
    "nacionalidade": "brasileiro",
}
print(dicionario)

print(lista[0])

print(dicionario['nacionalidade'])

print(dicionario.get("idade"))

#keys é uma função que vai retornar todas as chaves.
print(dicionario.keys())

print(len(dicionario))
print(dicionario.values())

if"idade" in dicionario:
    print("A chave idade existe")
    