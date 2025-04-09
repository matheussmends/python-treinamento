"""

Implemente um programa que receba a idade de uma pessoa e imprima a mensagem de acordo com os critérios

"""
# Exercício 1
"""
print("Digite a idade para a verificação de critérios. ")

idade = input("Qual é a sua idade? ")

if int(idade) < 16:
    print("Essa pessoa é MENOR de idade. ")
elif int(idade) > 18:
    print("Essa pessoa é MAIOR de idade ")
else:
    print("Essa pessoa é EMANCIPADA ") 
"""

#Exercício 2

print("Vamos avaliar a categoria do nadador com base na idade. ")

idade = input("Olá nadador! Digite sua idade: ")

if int(idade) >= 5 and int(idade) <= 7:
    print("Voce faz parte da categoria INFANTIL A ")
elif int(idade) >= 8 and int(idade) <= 10:
    print("Voce faz parte da categoria INFANTIL B ")
elif int(idade) >= 11 and int(idade) <= 13:
    print("Voce faz parte da categoria JUVENIL A ")
elif int(idade) >= 14 and int(idade) <= 17:
    print("Voce faz parte da categoria JUVENIL B")
else:
    print("Sua idade não faz parte dos critérios necessários. ")
