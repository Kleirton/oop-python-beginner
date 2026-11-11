#Trazendo todas as classe do arquivo Conta.py
from Conta import *

#Comenando a lista de contas

contasLista = []

#Criando duas contas

conta = Conta(nome='João', senha='1234', saldo=100)
contasLista.append(conta)
print(f'Conta do João Criada \n')

conta = Conta(nome='Maria', senha='1234', saldo=500)
contasLista.append(conta)
print(f'Conta da Maria Criada \n')

contasLista[0].conta()
print
contasLista[1].conta()

#Chamando alguns métodos diferentes

contasLista[0].depositar(deposito=100, senha='1234')
contasLista[1].sacar(saque=250, senha='1234')

print()

contasLista[0].conta()
print()
contasLista[1].conta()

# Criando uma outra conta com as informaçõs do usuário

userNome = str(input('Qual é o nome da conta?: '))
userSenha = str(input('Qual é a senha da nova conta?: '))
userSaldo = float(input('Qual será o saldo inicial dessa nova conta?: '))

conta = Conta(nome=userNome, senha=userSenha, saldo=userSaldo)
contasLista.append(conta)

print('Nova conta criada, it is the two: ')
print()
contasLista[2].conta()
