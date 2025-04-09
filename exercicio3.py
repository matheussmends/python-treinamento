"""1- faça um programa que leia 5 valores e ache o maior e o menor deles. Mostre o resultado.
"""

maior = float('-inf')
menor = float('inf')

for x in range(5):
    numero = float(input(f"Digite o {x+1}º valor: "))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f"O maior valor de todos eh: {maior}")
print(f"O menor mumero de todos eh: {menor}")
