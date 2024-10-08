saldo = 1000
opcao = 0


dicionario = {
    '07171': {'nome': 'lilica queridinha uau fofa', 'usuario': 'lilica', 'senha': '6969'},
    '07133': {'nome': 'oliver queridinho uau silly', 'usuario': 'sosofi', 'senha': '420420'},
    '07144': {'nome': 'pingo adora guardaroupa', 'usuario': 'lilica', 'senha': '6969'}
}

def senha():
    cpf = input('insira seu cpf: ')
    senhinha = input('insira a sua senha: ')
    return cpf in dicionario and dicionario[cpf]['senha'] == senhinha

def cadastro():
    cpf = input('insira cpf: ')
    if cpf in dicionario:
        print('CPF já cadastrado.')
        return
    nominho = input('Insira nome: ')
    senhanha = input('insira senha (4 a 6 caracteres): ')
    if 4 <= len(senhanha) <= 6:
        dicionario[cpf] = {'nome': nominho, 'usuario': nominho.split()[0], 'senha': senhanha}
        print(f'Seu usuário é {nominho.split()[0]}, use-o no log-on.')
    else:
        print('A senha deve ter entre 4 e 6 caracteres.')

def add_cliente():
    saber = input('qual seu nome? ')
    if saber in [info['usuario'] for info in dicionario.values()]:
        print(f'legal, {saber}, você é um cliente!')
    else:
        print('voce nao eh um cliente, voce precisa efetuar o cadastro.')

def remover_cliente():
    know = input('insira nome: ')
    if know in [info['usuario'] for info in dicionario.values()]:
        del dicionario[know]
        print('ta, foi removido')
    else:
        print('nome nao ta na lista')

def login():
    log = input('insira aqui o seu login: ')
    if log in [info['usuario'] for info in dicionario.values()]:
        senha_cliente = input('insira aqui a sua senha: ')
        if dicionario[log]['senha'] == senha_cliente:
            return True
    print('o usuário não foi encontrado, tente novamente')
    return False

while opcao == 0:
    print('olá, como gostaria de acessar o banco?')
    print('[0] cadastro')
    print('[1] log-on')
    print('[2] encerrar')
    opt = int(input())
    if opt == 0:
        cadastro()
    elif opt == 1:
        if login():
            while True:
                print('digite o numero')
                print('[1] saque')
                print('[2] deposito')
                print('[3] saldo')
                print('[4] falar com gerente')
                print('[5] saber cliente')
                print('[6] remover cliente')
                print('[0] encerrar')
                numero = int(input())
                match numero:
                    case 1:
                        if senha():
                            saque = int(input('de quanto seria o saque? '))
                            if saque > saldo:
                                print('você não tem saldo o suficiente.')
                            else:
                                saldo -= saque
                                print(f'ok, realizando contagem de notas... saldo atual = {saldo}')
                    case 2:
                        depo = int(input('de quanto seria o deposito? '))
                        saldo += depo
                        print(f'ok, deposito de {depo} efetuado com sucesso. saldo atual = {saldo}')
                    case 3:
                        print(f'seu saldo atual é {saldo} reais.')
                    case 4:
                        print('o contato do gerente é: (69) 4002-8922')
                    case 5:
                        add_cliente()
                    case 6:
                        remover_cliente()
                    case 0:
                        print('tenha um bom dia!')
                        opcao = 1
                        break
