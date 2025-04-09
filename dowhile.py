"""
do while

Código para adivinhar um número

"""
from random import randint

palpite = 0
numero = randint(1, 10)

while True: #Nós executamos sem verificar
    print("Qual o número correto?")
    palpite = int(input())
    if palpite == numero: #Estamos verificando nosso codigo
        print('Parabens você acertou!')
        break
    else:
        print("Você errou!")
else:
    print("Erro na aplicação")
    print(bool(palpite))
    