"""

Exercícios - Python

Obs: Todos os exercicios devem utilizar a função input, de forma que o usuario possa determinar os dados de entrada.

01 - área de um retângulo
02 - área de um quadrado
03 - Se o produto que você quer avaliar custa (??) reais qual será o valor do msm com desconto de (??)%.
04 - área de um círculo
05 - conversão de reais para dolar
07 - conversão de dolar para reais


# ------Exercício 01  área do retângulo

print("calcule a area de um retangulo")

base = input("Qual o tamanho da base do seu retangulo? ")
altura = input("Qual o tamanho da altura do seu retangulo? ")

area = float(base) * float(altura)

print(f'O seu retangulo possui area: {area} unidades de medida')

# ------Exercício 02 - área de um quadrado

print("Calcule a área de um quadrado")

lado = input("Qual o lado do seu quadrado? ")

area = float(lado) ** 2

print(f"O seu quadrado possui: {area} unidades de medida. ")

# ------Exercício03

print("Calcule o seu produto com o preço aplicado ")

preco_produto = input("Quanto custa o seu produto? ")
desconta = input("Quanto é o valor do desconto? ")

desconto = float(preco_produto) * float(desconta) / 100
preco_final = float(preco_produto) - desconto

print(f"O preço do produto com o desconto é: {preco_final}")

# -----Exercício 04 - calcule a área de um círculo.

print("Calcule a área do círculo. ")

raio = input("Qual o tamanho do raio? ")

area = 3.141592 * float(raio) ** 2

print(f"A área do círculo é: {area}")

# --------Exercício 05 - Conversão de reais para dolar

print("Faça a conversão de reais para Dolar. ")

reais = input("Quantos reais você quer converter para dolar? ")

conversao = float(reais) / 6.10

print(f"Você converteu R${reais} para US${conversao} no dia 13/01/25.")

"""

# -------Exercício 06 - dolar para reais

print("Faça a conversão de Dólar para Reais")

dolar = input("Quantos dólares você quer converter para reais? ")

conversao = float(dolar) * 6.10

print(f"Você converteu US${dolar} para R${conversao} no dia 13/01/25")

# comentado exercicios 1 a 6
# FINISHED.
