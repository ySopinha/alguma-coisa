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
    return

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
    cpf = input('insira aqui o seu CPF: ')
    if cpf in dicionario:
        senha_cliente = input('insira aqui a sua senha: ')
        if dicionario[senha_cliente]['senha'] == senha_cliente:
            return True
    else:
        return False
