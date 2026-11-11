from Banco import *

oBanco = Banco()

oBanco.criarConta(userNome='Joao', userSenha='1234', userSaldoIncial=100)

while True:
    print(f'{5*'-'} \033[1mWHAT DO YOU WANT?\033[0m {5*'-'}')
    print('Pressione b para ver o saldo')
    print('Pressione d para fazer um depósito')
    print('Pressione o para criar uma nova conta')
    print('Presione k para deletar uma conta')
    print('Pressione w para fazer um saque')
    print('Pression s para mostrar todas as contas')
    print('Pressione q para sair')
    print()
    
    action = str(input('Ação: ')).lower()[0]

    print()

    if action == 'b':
       oBanco.saldo()

    elif action == 'd':
        oBanco.depositar()

    elif action == 'o':
        oBanco.abrirConta()

    elif action == 'w':
        oBanco.sacar()

    elif action == 's':
        oBanco.contas()
    
    elif action == 'k':
        oBanco.fecharConta()

    elif action == 'q':
        print('Obrigado, goodbye!')
        break

    else:  
        print('Desculpe, mas isso não é uma ação possível')
        pass
    
    print()
    print('Feito!')
    print()
