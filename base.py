import modulo 

saldo = 1000
opcao = 0


dicionario = {
    '07171': {'nome': 'lilica queridinha uau fofa', 'usuario': 'lilica', 'senha': '6969'},
    '07133': {'nome': 'oliver queridinho uau silly', 'usuario': 'sosofi', 'senha': '420420'},
    '07144': {'nome': 'pingo adora guardaroupa', 'usuario': 'lilica', 'senha': '6969'}
}

 


while opcao == 0:
    print('olá, como gostaria de acessar o banco?')
    print('[0] cadastro')
    print('[1] log-on')
    print('[2] encerrar')
    opt = int(input())
    match opt:
        case 0:
            modulo.cadastro()
        case 1:
            if modulo.login():
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
                        if modulo.senha():
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
                        modulo.add_cliente()
                    case 6:
                        modulo.remover_cliente()
                    case 0:
                        print('tenha um bom dia!')
                        opcao = 1
            
        case 2:
            opcao = 1
    
                
