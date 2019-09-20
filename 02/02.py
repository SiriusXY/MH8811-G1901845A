## Program1
#1
Name=input('Input your name:')
print('Hello,{}!'.format(Name))

## Program 2

C=float(input('Input the Celsius:'))

while type(C) != float:
    print('Your input is invalid!')
    C=float(input('Input a floating number:'))

F=C*1.8+32
print(F)
