
#index     0        1         2
lista = ["item2", "item3", "item2"]
tupla = ("item1", "item2", "item1")

#chave:valor
dados = {"nome": "Gabriel", "ano": 1993, "valor_logico": True}
dados.update({"estado": "Rio de Janeiro"})
print(dados)

dicio = dados.copy()
print(dicio)

dicio2 = dict(dados)
print(dicio2)

dados["idade"] = 27
print(dados)
print(dicio)
print(dicio2)
