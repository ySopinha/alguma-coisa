saldo = 1000
opcao = 0
cliente = ['fulano' , 'fulana' , 'fulaninho', 'fulaninha', 'pingo', 'fifi']


dicionario = [
    {'nome': 'lilica legal uau querida', 'idade': '16', 'genero': 'feminino'},
    {'nome': 'Mr. Cowboy Ratinho Fofinho', 'idade': '2', 'genero': 'ratinho eu acho'}
]


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
        cliente.append(adic)
        print (cliente)

    def add_cliente():
        saber = input('qual seu nome? ')
        if saber in cliente:
                    print (f'legal, {saber}, você é um cliente!')
        else:
            print ('voce nao eh um cliente, voce precisa efetuar o cadastro.')
            print(cliente)
    def remover_cliente():
        know = input('insira nome')
        if know in cliente:
            cliente.remove(know)
            print('ta, foi removido')
            print(cliente)
            
        else:
            print('nome nao ta na lista, daora')
    match numero:
        case 1:
            adic = input('insira nome')
            if adic in cliente:
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
