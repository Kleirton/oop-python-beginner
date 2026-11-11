from Conta import *

class Banco():

    def __init__(self, horas, endereco, celular):
        self.contasDic = {}
        self.idConta = 0
        self.horas = horas
        self.endereco = endereco
        self.celular = celular
    
    def solicitarNumeroContaValido(self):
        numeroConta = input('Qual é o número da conta?: ')
        try:
            numeroConta = int(numeroConta)
        except ValueError:
            raise AbortarTransacao('O número da conta deve ser um inteiro')
        if numeroConta not in self.contasDic:
            raise AbortarTransacao(f'Não há conta {str(numeroConta)}')
        return numeroConta

    def buscarContaUsuario(self):
        numeroConta = self.solicitarNumeroContaValido()
        aConta = self.contasDic[numeroConta]
        self.solicitarSenhaValida(aConta)
        return aConta

    def solicitarSenhaValida(self, conta):
        senha = input('Por favor, digite sua senha: ')
        conta.verificarSenha(senha)

    def criarConta(self, userNome, userSaldoIncial, userSenha):
        self.contasDic[self.idConta] = Conta(nome=userNome, senha=userSenha, saldo=userSaldoIncial)
        novaContaId = self.idConta

        # Preparando terreno para a próxima conta
        self.idConta += 1
        
        return novaContaId

    def abrirConta(self):
        print(f'{5*'-'} \033[1m NOVA CONTA \033[0m {5*'-'}')
        userNome = str(input('Qual o seu nome?: ')).capitalize()
        userSenha = input('Por favor, insira uma nova senha: ')
        userSladoIncial = input('Insira um saldo inicial a conta: ')
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
        aConta = self.buscarContaUsuario()
        oSaldo = aConta.contaSaldo()

        print(f'O saldo da sua conta é: \033[1mR${oSaldo}\033[0m')
       

    def depositar(self):
        print(f'{5*'-'}\033[1m DEPÓSITO \033[0m{5*'-'}')
        aConta = self.buscarContaUsuario()
        userDeposito = input('Por favor, digite o valor que deseja depositar: ')
        oSaldo = aConta.depositar(userDeposito)
        print(f'Déposito de: R${userDeposito}')
        print(f'Seu novo saldo é: R${oSaldo}')

    def contas(self):
        print(f'{5*'-'}\033[1m TODAS AS CONTAS \033[0m{5*'-'}')
        print('(Normalmente, aqui pediria uma senah de adiministrador)')
        print()
        for key, conta in self.contasDic.items():
            conta.show()
            print(f'  Número da conta: {key}')
        print()

    def obterInfo(self):
        print(f'{5*'-'} \033[1m INFORMAÇÕES DO BANCO \033[0m {5*'-'}')
        print(f'Endereço: {self.endereco}')
        print(f'Telefone: {self.celular}')
        print(f'Atualmente, temos {len(self.contasDic)} contas abertas')

    def sacar(self):
        print(f'{5*'-'}\033[1m SACAR \033[0m{5*'-'}')
        aConta = self.buscarContaUsuario()
        userSaque = input('Por favor, digite o calor que deseja sacar: ')
        oSaldo = aConta.sacar(userSaque)
        print(f'Valor sacado: R${userSaque}')
        print(f'Seu novo saldo é: R${oSaldo}')
        
        print()
    