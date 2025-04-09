#Argumentos nomeados

"""def imprimir_nome(nome, sobrenome, idade):
    print("Nome: ", nome)
    print("Sobrenome: ", sobrenome)
    print("Idade: ", idade)


sobrenome = "Mendes"
idade = 35
imprimir_nome(sobrenome=sobrenome, idade=idade, nome="Matheus")"""

# Parâmetro Padrão - Define argumentos não obrigatórios

"""def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None):
    print("----------")
    print("Título: " , nomeImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)"""
    

"""print()
"""
# Exemplos de nº argumentos <= ao nº de parametros

"""imprimir_imovel("Casa 3 Quartos - SP", 3)
imprimir_imovel("Apartamento - MG", 2, 1)"""

# Exemplos de nº de argumentos > nº dos parametros
# imprimir_imovel("Loja Comercial", 2, 5, "desconto")

# O argumento arbitrário *args - Essa função recebe argumentos que serão atribuídos em uma tupla

"""def imprimir_imovel(nomeImovel, n_quartos, vagasGaragem=None, *telefones):
    print("----------")
    print("Título: " , nomeImovel)
    print("Quartos: ", n_quartos)
    if vagasGaragem != None:
        print("Vagas na garagem: ", vagasGaragem)
    print("telefones: ", telefones)

imprimir_imovel("Loja Comercial", 2, 5, "61 555-5555", "21 555-555")"""

"""def imprimir_nomes(*nomes):
    print(nomes[0])
    print(type(nomes))

lista = ["Ana","Beatriz", "Pedro", "João"]
imprimir_nomes(*lista)"""


# Argumento Abitrário **kwargs - Keyword Arguments
# Essa função recebe argumentos que serão atribuídos em um dicionário

def imprimir_nomes(**nomes):
    print(f"{nomes["nome"]} {nomes['sobrenome']}")

imprimir_nomes(nome="ana", sobrenome="julia")