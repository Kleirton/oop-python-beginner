# Definindo a Classe Conta Bancária
# Erros são indicados por instruções "raise"

#Definindo uma exceção personalizada

class AbortarTransacao(Exception):
    ''' Lance(raise) essa exceção para abortar uma transação bancária '''
    pass

class Conta():
    
    ## Definindo as Propriedaes do Objeto
    ## Variáveis de Instância
    def __init__(self, nome, senha, saldo):
        self.nome = nome
        self.senha = senha
        self.saldo = self.validarValor(saldo)
    
    ## Métodos do objeto

    def validarValor(self, saldo):
        try:
            saldo = int(saldo)
        except ValueError:
            raise AbortarTransacao('O saldo dever ser um valor inteiro')
        if saldo <= 0:
            raise AbortarTransacao('O saldo deve ser positivo')
        return saldo

    def verificarSenha(self, senha):
        if senha != self.senha:
            raise AbortarTransacao('Senha incorreta')
    
    

    def sacar(self, saque, senha):
        if senha != self.senha:
            print('Senha incorreta')
            return None

        elif saque > self.saldo:
            print(f'Saque R${saque} maior que saldo na conta: R${self.saldo}')
            return None

        elif saque < 0:
            print('Impossível sacar valores negativos')
            return None
        
        elif saque <= self.saldo and senha == self.senha:
            self.saldo -= saque
            return self.saldo 

    def depositar(self, deposito, senha):
        if senha != self.senha:
            print('Senha incorreta!')
            return None

        elif deposito < 0:
            print('Its not possible depositar valores negativos!')
            return None
        
        elif senha == self.senha:
            self.saldo += deposito
            return self.saldo
    
    def contaSaldo(self, senha = ''):
        if senha != self.senha:
            return None
        
        elif senha == self.senha:
            return self.saldo

    def conta(self):
        print(10*'-', "CONTA",10*'-')
        print(f'O nome da conta é: {self.nome}')
        print(f'A senha da conta é: {self.senha}')
        print(f'O saldo da conta é: {self.saldo}')  
    
    # adicionado para Debug (posteriormente)

    def show(self):
        print(f'  Nome: {self.nome}')
        print(f' Saldo: {self.saldo}')
        print(f' Senha: {self.senha}')

