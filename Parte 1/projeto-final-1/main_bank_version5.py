from Banco import *

oBanco = Banco(horas='Horário: das 9 às 17', endereco='152 Bezerra, Fortaleza, Ceará, BR', celular='(55) 085 98638-9740')

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
    print('Presione i para obter infomaçẽos sobre o Banco')
    print()
    
    action = input('Ação: ')
    action = action.lower()
    action = action[0]
    print()

    try:
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

        elif action =='i':
            oBanco.obterInfo()
    
    except AbortarTransacao as erro:
        # Mostrando o texto da messagem de erro\
        print(erro)

    print()
    print('Feito!')
    print()
