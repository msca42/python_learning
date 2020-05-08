# 1 //1
PasswordContent = open('SecretPasswordFile.txt') 
Password = PasswordContent.read()
print('Please input password:')
inputpassword = input()
if (inputpassword == Password):
    print('Access ')
    if(inputpassword == 12345):
        print('Someone who is idiot set this password')
else:
    print('Deny')
