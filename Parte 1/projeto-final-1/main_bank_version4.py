from Conta import *

contaDic = {}
idConta = 0 

conta = Conta(nome='João', senha='1234', saldo=100)
contaDic[idConta] = conta
JoaoContNumber = idConta
idConta += 1

conta = Conta(nome='Maria', senha='1234', saldo=500)
contaDic[idConta] = conta
MariaContNumber = idConta
idConta += 1


while True:
    print(f'{5*'-'} WHAT DO YOU WANT? {5*'-'}')
    print('Pressione b para ver o saldo')
    print('Pressione d para fazer um depósito')
    print('Pressione o para criar uma nova conta')
    print('Pressione w para fazer um saque')
    print('Pression s para mostrar todas as contas')
    print('Pressione q para sair')
    print()
    
    action = str(input('Ação: ')).lower()[0]

    print()

    if action == 'b':
        print(f'{5*'-'} \033[1m SALDO DA CONTA \033[0m {5*'-'}')
        contaNum = int(input('Digite o número da conta: '))
        contaSenha = str(input('Por favor, insira a senha: '))
        conta = contaDic[contaNum]
        saldo = conta.contaSaldo(senha=contaSenha)
        if saldo is not None:
            print(f'O Saldo da conta é: \033[1m R${saldo} \033[0m')

    elif action == 'd':
        print(f'{5*'-'} \033[1m DEPÓSITO \033[0m {5*'-'}')
        contaNum = int(input('Digite o número da conta: '))
        deposito = float(input('Valor que deseja depositar: '))
        contaSenha = str(input('Por favor, insira a senha: '))
        conta = contaDic[contaNum]
        saldoNovo = conta.depositar(deposito=deposito, senha=contaSenha)
        if saldoNovo is not None:
            print(f'Seu novo saldo é: \033[1m R${saldoNovo} \033[0m')

    elif action == 'o':
        print(f'{5*'-'} \033[1m CRIANDO UMA NOVA CONTA \033[0m {5*'-'}')
        contaNome = str(input('Qual o seu nome: ')).capitalize()
        saldoIncial = float(input('Qual será o saldo inicial para está conta?: '))
        senhaConta = str(input('Coloque uma senha para essa conta: '))
        conta = Conta(nome=contaNome, senha=senhaConta, saldo=saldoIncial)
        contaDic[idConta] = conta
        print(f'O número da sua nova conta é {idConta}')
        idConta += 1
        print()

    elif action == 'w':
        print(f'{5*'-'} \033[1m FAZENDO UM SAQUE \033[0m {5*'-'}')
        contaNum = int(input('Digite o número da conta: '))
        sacar = float(input('Digite o valor que deseja sacar da conta: '))
        senhaConta = str(input('Por favor, insira a senha: '))
        conta = contaDic[contaNum]
        saldo = conta.sacar(saque=sacar, senha=senhaConta)

        if saldo is not None:
            print(f'O valor sacado foi \033[1m R${sacar} \033[0m, o seu novo saldo é: \033[1m R${saldo} \033[0m')

    elif action == 's':
        print(f'{5*'-'} \033[1m CONTAS CADASTRADAS \033[0m {5*'-'}')
        print('')
        for contaNum, conta in contaDic.items():
            conta.conta()
            print(f'O núemro da Conta é: {contaNum}')
            print()
    
    elif action == 'q':
        print('Obrigado, goodbye!')
        break

    else:  
        print('Desculpe, mas isso não é uma ação possível')
        pass
    
    print()
    print('Feito!')
    print()

