# say hello and ask for my name
print('Hello world')
print("What's your name")
try :
 myname = str (input())
# Type Conversion change nothing , it will make any difference witch try catch
except ValueError :
 print('your input is not string')
print('It is good to meet your,' + myname)
print('The length of your name is:')
print(len(myname))
tag = True;
while tag: 
 print('What is your age')
 try: 
   myAge =  int(input())
 except ValueError: 
   print('your input is not number')
 try: 
   print('Your will be ' + str(myAge + 1) + ' in a year.')
 except NameError:
   tag = True   
   print('Please input again')   
 else:
   tag = False

