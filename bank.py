saldo = 1000
opcao = 0


dicionario = {
     '07171' : {'nome' : 'lilica queridinha uau fofa', 'usuario' : 'lilica', 'senha' : '6969' },
     '07133' : {'nome' : 'oliver queridinho uau silly', 'usuario' : 'sosofi', 'senha' : '420420' },    
     '07144' : {'nome' : 'pingo adora guardaroupa', 'usuario' : 'lilica', 'senha' : '6969' }
}



while opcao == 0:
    def cadastro():
            cpf = input('insira cpf: ')
            dicionario.get(cpf)
            nominho = input('Insira nome: ')
            senhanha = input('insira senha 4 a 6 : ')
            lista = nominho.split()
            usuario = lista[0]
            qtd_senha = len(senhanha)
            
            dicionario[cpf] = {'nome' : 'pingo adora guardaroupa', 'usuario' : usuario, 'senha' : '6969' }
                
            print(usuario)
            print(f'Seu usuário é {usuario}, use-o no log-on.')
            

    def add_cliente():
            saber = input('qual seu nome? ')
            if saber in dicionario:
                        print (f'legal, {saber}, você é um cliente!')
            else:
                print ('voce nao eh um cliente, voce precisa efetuar o cadastro.')
                print(dicionario)
    def remover_cliente():
            know = input('insira nome')
            if know in dicionario:

                print('ta, foi removido')
                print(dicionario)
                
            else:
                print('nome nao ta na lista, daora')
    def login():
            log = input('insira aqui o seu login: ')
            if log in dicionario:
                senha_cliente = input('insira aqui a sua senha: ')
            else:
                print ('o usuário não foi encontado, tente novamente')
    while opcao == 0:
        print ('olá, como gostaria de acessar o banco insira nome do banco?')
        print ('[0] cadastro')
        print ('[1]log-on')
        print ('[2]encerrar')
        opt = int(input())
        opcao = 1
    if opt == 0:
        cadastro()

opcao = 1

     



print ('digite o numero')
print ('[1] saque')
print ('[2] deposito')
print ('[3] saldo')
print ('[4] falar com gerente')
print ('[5] saber cliente')
print ('[6] remover cliente')
print ('[7] caixote')
print ('[0] encerrar')
numero = int(input())
while opcao == 0:
    def cadastro():
        adic = input('insira nome')
        dicionario.append(adic)
        print (dicionario)
     
    def add_cliente():
        saber = input('qual seu nome? ')
        if saber in dicionario:
                    print (f'legal, {saber}, você é um cliente!')
        else:
            print ('voce nao eh um cliente, voce precisa efetuar o cadastro.')
            print(dicionario)
    def remover_cliente():
        know = input('insira nome')
        if know in dicionario:

            print('ta, foi removido')
            print(dicionario)
            
        else:
            print('nome nao ta na lista, daora')
    match numero:
        case 1:
            adic = input('insira nome')
            if adic in dicionario:
               saque = int(input('de quanto seria o saque?'))
            if saque > saldo:
                print ('você não tem saldo o suficiente.')
            else:
                print ('ok, realizando contagem de notas... ... .. .... ... ... ...')
                print (f'saldo atual = {saldo - saque}')
        case 2:
            depo = int(input('de quanto seria o deposito?'))
            print (f'ok, deposito de {depo} efetuado com sucesso')
            print (f'saldo atual = {saldo + depo}')
        case 3:
            print (f'seu saldo atual é {saldo} reais.')
        case 4:
            print ('o contato do gerente fulano de tal (whatsapp) é: (69) 4002-8922, caso queira entrar em contato via e-mail, é rogerinhopirocadelinguiçadefeijaoqueimadotortaoqueveioenvergadotortaopraesquerdaaa@operagx.com! o primeiro navegador gamer com limitadores de gpu e ram, e ad blocker embutido!')
            opcao = 1
        case 0:
            print ('tenha um bom dia!')
            opcao = 1
        case 5:
            add_cliente()
            opcao = 1
        case 6:
              remover_cliente()
              opcao = 1
        case 7:
              cadastro()
              opcao = 1
