#Aribido Lamzey
#lamzey.m@gmail.com


print('Welcome to Authenticator')

print('Please enter your User name')
name1 = input()

print('Please enter your password')
password1 = input()

print('Thanks for Registering with us')


print('Please enter User name again')
name = input()

print('Please enter your password')
password = input()


if name == name1 and password == password1:
        print('Congratulations, Access Granted ' + name)
        print('What would you like to do? ' + name)
else:
    if name != name1 or password != password1:
        print('Access Declined, Please try again')
        
        print('Please enter User name again, last chance')
        name = input()
        
        print('Please enter your password,last chance')
        password = input()
        
    if password == password1 and name != name1:
        print('Sorry!, You have been blocked out, Contact Admin')
        
    elif name == name1 and password == password1:
        print('Congratulations, Access Granted ' + name)
        print('What would you like to do? ' + name)
    else:
         print('Sorry!, You have been blocked out, Contact Admin')
