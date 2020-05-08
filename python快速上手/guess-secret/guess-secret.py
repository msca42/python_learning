passwordFile = open('SecretPasswordFile.txt') #openfile
secretPassword = passwordFile.read()    # read contents
print('Enter your password:')  # input password hint
typePassword  = input()   #  input
if typePassword == secretPassword:  # judge  two strings success and fail
    print('Access granted')     
    if typePassword == '12345':
        print('That password is one that an idiot puts on their luggage')
else:
    print('Access deied')
