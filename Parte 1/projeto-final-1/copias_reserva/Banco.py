from Conta import *

class Banco():

    def __init__(self):
        self.contasDic = {}
        self.idConta = 0
    
    def criarConta(self, userNome, userSaldoIncial, userSenha):
        self.contasDic[self.idConta] = Conta(nome=userNome, senha=userSenha, saldo=userSaldoIncial)
        novaContaId = self.idConta

        # Preparando terreno para a próxima conta
        self.idConta += 1
        return novaContaId

    def abrirConta(self):
        print(f'{5*'-'} \033[1m NOVA CONTA \033[0m {5*'-'}')
        userNome = str(input('Qual o seu nome?: ')).capitalize()
        userSenha = str(input('Por favor, insira uma nova senha: '))
        userSladoIncial = float(input('Insira um saldo inicial a conta: '))
        novaContaId = self.criarConta(userNome=userNome, userSenha=userSenha, userSaldoIncial=userSladoIncial)

        print()
        print(f'O número da sua nova conta é: \033[1m{novaContaId}\033[0m')
        print()

    def fecharConta(self):
        print(f'{5*'-'}\033[1m FECHAR CONTA \033[0m{5*'-'}')
        userContaNum = int(input('Digite o número da conta que você deseja fechar: '))
        userSenha = str(input('Digite a senha da conta: '))

        aConta = self.contasDic[userContaNum]
        oSaldo = aConta.contaSaldo(senha=userSenha)

        if oSaldo is not None:
            print(f'O saldo na sua conta é R${oSaldo}, será retornado a você. \n A sua conta foi fechada.')
            # removendo a conta do usuário
            del self.contasDic[userContaNum]
    
    def saldo(self):
        print(f'{5*'-'}\033[1m SALDO DA CONTA \033[0m{5*'-'}')
        userContaNum = int(input('Digite o número da sua conta: '))
        userSenha = str(input('Digite a senha da sua conta: '))
        
        aConta = self.contasDic[userContaNum]
        oSaldo = aConta.contaSaldo(senha=userSenha)

        if oSaldo is not None:
            print(f'O saldo na sua conta é: \033[1mR${oSaldo}\033[0m')
       

    def depositar(self):
        print(f'{5*'-'}\033[1m DEPÓSITO \033[0m{5*'-'}')
        userContaNum = int(input('Digite o número da sua conta: '))
        userSenha = str(input('Digite a senha da sua conta: '))
        userDeposito = float(input('Digite o valor que deseja depositar: '))

        aConta = self.contasDic[userContaNum]
        novoSaldo = aConta.depositar(senha=userSenha, deposito=userDeposito)

        if novoSaldo is not None:
            print(f'O valor depósitado foi \033[1mR${userDeposito}\033[0m e seu novo saldo é \033[1mR${novoSaldo}\033[0m')

    def contas(self):
        print(f'{5*'-'}\033[1m TODAS AS CONTAS \033[0m{5*'-'}')
        print()

        for key, conta in self.contasDic.items():
            conta.conta()
            print(f'O número da conta é: {key}')
        print()

    def sacar(self):
        print(f'{5*'-'}\033[1m SACAR \033[0m{5*'-'}')
        userContaNum = int(input('Digite o número da sua conta: '))
        userSenha = str(input('Digete a senha da sua conta: '))
        userSaque = float(input('Digite o valor que deseja sacar: '))

        aConta = self.contasDic[userContaNum]
        novoSaldo = aConta.sacar(saque=userSaque, senha=userSenha)

        if novoSaldo is not None:
             print(f'O valor sacado foi \033[1mR${userSaque}\033[0m e seu novo saldo é \033[1mR${novoSaldo}\033[0m')
        print()
