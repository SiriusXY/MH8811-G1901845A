def program1():
    a=('Hello, world!')
    print(a)

def program2():
    name=input('Please input your name：')
    print('Hello,{}!'.format(name))

def program3():
    c=float(input('Please input the Celsius:'))
    F=c*1.8+32
    print('The corresponding Fahrenheit temperature is {}'.format(F))

    

while True:
    n=input('Please input the program you want to run (1,2 or 3), enter exit for terminating:')
    if n=='1':
        program1()
    elif n=='2':
        program2()
    elif n=='3':
        program3()
    else:
        print('Thanks for using!')
        break
    


