"""1- Escreva um programa em que sejam lidos dois números reais, X e Y, e sejam feitas chamadas a funções descritas abaixo, que deverão ser implementadas. No escopo global deve ser impresso o resultado retornado por estas funções.  

a) Uma função que receba X e Y como entrada e retorne o maior deles;  

b) Uma função que receba X e Y como entrada e retorne a média aritmética deles; """
# ------------------------------------------------------------------------------------

""" 
# Exercício A - Uma função que receba X e Y como entrada e retorne o maior deles;

print(30 * "--")
def Numero_Maior(x, y):
    return max(x, y)

# Leitura dos números reais
x = float(input(f"Digite o Primeiro número: "))
y = float(input(f"Digite o Segundo número: "))

print("O maior número é: ", Numero_Maior(x,y))
print(30 * "--")


# Exercício B - Uma função que receba X e Y como entrada e retorne a M.A. deles;


print(30 * "--")
def Media_Aritmetica(x, y):
    return ((x + y) / 2)

# Leitura dos números reais
x = float(input(f"Digite o Primeiro número: "))
y = float(input(f"Digite o Segundo número: "))

print(f"A média Aritmética é: ", Media_Aritmetica(x, y))
print(30 * "--")

"""
# -----------------------------------------------------------------------------

"""2- Escreva uma função de potenciação, em que os dados de entrada são: base e 
expoente (inteiros)."""

"""print(30 * "--")
def potenciacao(base, expoente):
    return base ** expoente

# O INT sempre vem ANTES do input, senão não funciona.
base = int(input("Digite a base: "))
expoente = int(input("Digite o expoente: "))

print(f"A potênciação é: ", potenciacao(base, expoente))
print(30 * "--")"""

# -----------------------------------------------------------------

""" Crie uma calculadora que consiga executar as funções destacadas da calculadora 
padrão do windows 10. """

import math

print("===" * 20)
def calcular():
    while True:
        print("Escolha a operação matemática. \n")
        print("1. Adição")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Divisão")
        print("5. Raiz Quadrada")
        print("6. Potência")
        print("7. Porcentagem")
        print("8. Sair\n") # Precisa dessa opção para sair do loop infinito.

        selecao = input("Selecione a opção desejada: ")

        if selecao =='1': # Me atentar se a adição está limitada a 2 numeros ou se continua...
            print("Você selecionou Adição!\n")
            numero1 = float(input("Digite o primeiro numero: ")) #uso float pois o numero pode ser decimal.
            numero2 = float(input("Digite o segundo numero: "))
            print(f"\nO seu resultado é: {numero1 + numero2}")
            print("===" * 20)
        
        elif selecao == '2':
            print("Você selecionou Subtração!\n")
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            print(f"O resultado da é: {numero1 - numero2}")
            print("===" * 20)
        
        elif selecao == '3':
            print("Você selecionou Multiplicação!\n")
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            print(f"O resultado é: {numero1 * numero2}")
            print("===" * 20)
        
        elif selecao == '4':
            print("Você selecionou Divisão!")
            numero1 = float(input("Digite o primeiro número: "))
            numero2 = float(input("Digite o segundo número: "))
            print(f"\nO resultado é: {numero1 / numero2}")
            print("===" * 20)

        elif selecao == '5':
            print("Você selecionou Raiz Quadrada! ")
            numero1 = float(input("Digite um numero para calcular a Raiz Quadrada: "))
            if numero1 < 0:
                print("Não é possível calcular a raiz quadrada de um número Negativo")
            else:
                print(f"\nO resultado da Raiz Quadrada de {numero1} é: {math.sqrt(numero1)}")
                print("===" * 20)

        elif selecao == '6':
            print("Você Selecionou Potência!")
            numero1 = float(input("Digite o número: "))
            print(f"O resultado da potência é: {numero1 ** 2}")
            print("===" * 20)
            
        elif selecao == '7':
            print("Você selecionou Porcentagem!")
            numero1 = float(input("Digite o número: "))
            porcentagem = float(input("Quantos % você quer saber do número? "))
            print(f"Resultado: {porcentagem}% de {numero1} é: {porcentagem / 100 * numero1}\n")
            print("===" * 20)

        elif selecao == '8':
            print("\nAté o próximo calculo!! :) \n")
            print("===" * 20)
            break
        else:
            print("\nOpcão inválida, tente novamente.\n")
            print("===" * 20)


calcular()