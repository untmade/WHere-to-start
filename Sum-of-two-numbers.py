#this code asks for two numbers and calculates their sum

def sum(a, b):
    return (a + b)

a = int(input('Enter 1st number: '))
b = int(input('Enter 2nd number: '))

print(f'Sum of {a} and {b} is {sum(a, b)}')

"""
If anything other than a number is given by the user the program throws an error

to fix this I added these lines so that no error comes up no matter what the user inputs
"""

def sum(a, b):
    return (a + b)
a =''
while a == '':
    try:
        no=0
        a = int(input('Enter 1st number: '))
        no+=1
    except:
        print('Input an integer you bitch')
b= ''
while b=='':
    try:
        b = int(input('Enter 2nd number: '))
    except:
        if no>0:
            print('Again fucker?')
        else:
            print("don't be a bitch")
        
print(f'Sum of {a} and {b} is {sum(a, b)}')
