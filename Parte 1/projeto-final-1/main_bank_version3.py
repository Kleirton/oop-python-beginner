from Conta import *

contaDic = {}
proxContaNum = 0

conta = Conta(nome='João', senha='JoãoSenha', saldo=100)
contaDic[proxContaNum] = conta
print(f'Conta do João Criada')
JoaoContNumber = proxContaNum
proxContaNum += 1

print()
contaDic[JoaoContNumber].conta()
print()

conta = Conta(nome='Maria', senha='1234', saldo=500)
contaDic[proxContaNum] = conta
print(f'Conta da Maria Criada')
MariaContNumber = proxContaNum
proxContaNum += 1

print()
contaDic[MariaContNumber].conta()
print()

print(contaDic)

# Faça a versão que receba os dados do usuário.
