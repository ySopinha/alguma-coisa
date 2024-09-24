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
    