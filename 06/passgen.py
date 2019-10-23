import random
import string

def genPassword(n):
    if (n>=4) & (type(n) is int):
        lc='qwertyuiopasdfghjklzxcvbnm'
        uc='QWERTYUIOPASDFGHJKLZXCVBNM'
        symbol=string.punctuation
        all_random='0123456789'+lc+uc+symbol
        my_password=''
        my_password+=str(random.randint(0,9))
        my_password+=random.choice(lc)
        my_password+=random.choice(uc)
        my_password+=random.choice(symbol)
    

        for i in range(n-4):
            my_password+=random.choice(all_random)

        my_passwordlist=list(my_password)
        random.SystemRandom().shuffle(my_passwordlist)
        my_password=''.join(my_passwordlist)
        return(my_password)
    else:
        print('Please input a valid length for your password! Notice that the length should be at least 4.')
        exit()


if __name__ == '__main__':
    print(genPassword(12))
else:
    print('The passgen module has been imported successfully.')
