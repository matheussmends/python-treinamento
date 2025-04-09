"""
Função input() - Função para receber dados do usuário
"""

"""
1º forma

nome = input("Qual eh o seu nome? ")
print("Olá, " ,nome)

idade - input("Qual a sua idade? ")
print("Sua idade eh: " +idade)
"""

"""
2º forma

nome = input("Qual eh o seu nome? ")
idade = input("Qual a sua idade? ")

print("Seu nome eh: {0} e Sua idade eh {1}".format(nome,idade))
"""

nome = input("Qual eh o seu nome? ")
idade = input("Qual a sua idade? ")

print(f'Seu nome eh: {nome} e Sua idade eh: {idade} ')
