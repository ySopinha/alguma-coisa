'''
esse aqui eh o codigo antes da alteração com funções

num = int(input('insira numero aqui'))
num2 = int(input('insira outro numero aqui'))
sim = input('insira um operador (+, -, /, *)')#sim significa simbolo
match sim:
    case  '+':
        print (num + num2)
    case '-':
        print (num - num2)
    case  '*':
        print (num * num2)
    case '/':
        print (num / num2)
'''    

num = int(input('insira numero aqui'))
num2 = int(input('insira outro numero aqui'))
sim = input('insira um operador (+, -, /, *)')#sim significa simbolo
def soma(x,y):
    print(x + y)
def sub(x,y):
    print(x - y)
def mult(x,y):
    print(x*y)
def div(x,y):
    print(x/y)
match sim:
    case  '+':
        soma(num, num2)
    case '-':
        sub (num, num2)
    case  '*':
        mult (num, num2)
    case '/':
        div (num, num2)
    
