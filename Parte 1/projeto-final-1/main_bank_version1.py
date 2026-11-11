# Importando a classe do arquivo Conta com todas as sua funções
from Conta import *

# Criando uma formulário para criar contas

userName = str(input('Qual é o seu nome para a nova conta?: '))
userSaldo = float(input('Qual o seu saldo inicial para essa conta?: '))
userSenha = str(input('Qual a senha que você quer usar para essa conta?: '))

NovaConta = Conta(nome=userName, saldo=userSaldo, senha=userSenha)

print()
NovaConta.conta()

# Create two accounts

joao = Conta(nome='João', senha='1234', saldo=100)

maria = Conta(nome='Maria', senha='1234', saldo=100)

joao.depositar(deposito=500, senha='1234')


