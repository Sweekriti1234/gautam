''' year = int(input('enter the year to check for leap year'))
if (year % 4 ==0 ):
    if (year % 12 == 0):
        print(f'{year} is leap year')
    else:
        print('nearly a leap year')
else:
    print('not even close') '''
'''
n = int(input('enter a number: '))
flag = False
if ( n > 0):
    sqr = n * n
    flag = True 
    print(f' {sqr}  ')
elif(n < 0):
    cube = n**3
    flag = True
    print(f' {cube} ')
else:
    pass

print(flag) '''
num = int(input('enter a number :'))
if (num % 2 ==0 ):
    print(f'{num} is even')
else:
    print(f'{num} is odd')
