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

    def validarValor(self, valor):
        try:
            valor = int(valor)
        except ValueError:
            raise AbortarTransacao('O valor dever ser um número inteiro')
        if valor <= 0:
            raise AbortarTransacao('O valor deve ser positivo')
        return valor

    def verificarSenha(self, senha):
        if senha != self.senha:
            raise AbortarTransacao('Senha incorreta')
    
    def depositar(self, deposito):
        deposito = self.validarValor(deposito)
        self.saldo += deposito
        return self.saldo
    
    def contaSaldo(self):
        return self.saldo
    
    def sacar(self, saque):
        saque = self.validarValor(saque)
        if saque > self.saldo:
            raise AbortarTransacao('Você não pode sacar um valor maior que o saldo da sua conta')
        self.saldo -= saque
        return self.saldo

    def show(self):
        print(f'{5*'-'} \033[1m CONTA \033[0m {5*'-'}')
        print(f'  Nome: {self.nome}')
        print(f'  Saldo: R${self.saldo}')
        print(f'  Senha: {self.senha}')

    