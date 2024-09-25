saldo = 1000
print ('digite o numero')
print ('[1] saque')
print ('[2] deposito')
print ('[3] saldo')
print ('[4] falar com gerente')
print ('[0] break')
numero = int(input())
match numero:
    case 1:
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
        print ('o contato do gerente fulano de tal (whatsapp) é: (69) 4002-8922, caso queira entrar em contato via e-mail, é rogerinhopirocadelinguiçadefeijaoqueimadotortaoqueveioenvergadotortaopraesquerdaaa@operagx.com')
    case 0:
        print ('tenha um bom dia!')
