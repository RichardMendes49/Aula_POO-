'''Exercício 2  Classe ContaBancaria
1. Crie uma classe chamada ContaBancaria com:
○ Atributos: titular (string), saldo (float).
○ Métodos:
■ depositar(valor) → adiciona ao saldo.
■ sacar(valor) → subtrai do saldo se houver saldo suficiente.
■ exibir_saldo() → mostra o saldo atual.
2. Crie uma conta para &quot;João&quot; com saldo inicial de 1000.
○ Deposite 500.
○ Saque 300.
○ Exiba o saldo final.'''

# Definindo a classe
class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo

    # Método para depositar
    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")


    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado. Saldo atual: R${self.saldo:.2f}")
        else:
            print("ta sem dinheiro irmão!")


    def exibir_saldo(self):
        print(f"Saldo atual da conta de {self.titular}: R${self.saldo:.2f}")



conta_joao = ContaBancaria("João", 1000.0)


conta_joao.depositar(500)   
conta_joao.sacar(300)       
conta_joao.exibir_saldo()   