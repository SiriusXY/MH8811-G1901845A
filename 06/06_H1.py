import passgen

n=int(input('Please input the length for your password:'))
print('The random password generated for you is:{}'.format(passgen.genPassword(n)))