class Conta:
    
    def __init__(self, numero, titular, saldo):
        self.numero = numero 
        self.titular = titular 
        self.saldo = saldo

    def extrato(self):
        print(f'Saldo: R${self.saldo}')


    def depositar(self, valor):
        self.saldo += valor
        print(f"Valor depositado! Seu novo saldo eh: R${self.saldo}")


    def sacar(self, valor):
        self.saldo -= valor
        print(f'Você sacou R${valor}, agora seu saldo eh: R${self.saldo}!')
