saldo = 1000
def saldo(x):
    global saldo
    saldo -= x
def solicitar_valor(x):
    float(input('insira valor; '))
def verificar_saldo(x):
    global saldo
    if x > saldo:
        print('negado')

valor = solicitar_valor()
if verificar_saldo(valor):
    saldo(valor)
print (saldo)
