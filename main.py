import random
import string


lowercase = string.ascii_lowercase
uppercase = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

pwrd = lowercase + uppercase + numbers + symbols

def createPassword():
    print('This is The Password Generator!')
    pwrd_len = int(input('Enter desired number of characters: '))
    pwrd_full = ''.join(random.sample(pwrd, pwrd_len))
    print('Your generated password is: ', pwrd_full)

createPassword()