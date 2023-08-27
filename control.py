# decision control instruction (if-elif-else)
# repitition control instruction

''' num1 = int(input('enter a number to compare : '))
if (num1 > 50):
    print(f'{num1} is greater than 50')
else :
    print(f'{num1} is less than 50') '''   

''' per = float(input('enter your percentage : '))
if (per>=80):
    grade = 'A'
    print(f'your grade is {grade}')

elif (per < 80) and (per >= 60):
    grde = "B"
    print(f'your grade is {grade}')
elif (per < 60) and (per >= 40):
    grade = 'C'
    print(f'your grade is {grade}')
else:
    print(' You are not graded ') '''

pur = int(input('enter the purchased amount :'))
if (pur == 100000):
    DA = 0.1 * 100000
    print(f'the discounted amount is {DA}')
elif (pur == 150000):
    DA = 0.15 * 150000
    print(f' The discounted amount is {DA}')
else:
    DA = 0.2 * pur
    print(f'the discounted amount is {DA}')


