''' num = int(input('enter a number:'))
while num != 5:
    print(f"square is {num * num} ")
    num = int(input('enter number 5 to exit:')) '''


''' n=0
while n<10:
    print(f'{n}')
    n += 1
    ''' 
'''n = 0
while True:
    print(f'{n}')'''
    # range(1,11) = [1,2,3,4,5,6,7,8,9,10]

'''for i in range(1,11,2):
    print(i)'''
'''for i in range(0,51):
    if(i%2==0):
        print(f'{i} is even')
    else:
        print(f'{i} is odd')'''

'''name = "Sweekriti"
for i in name:
    print(i)
for i in name:
    print(i, end = " ")
print("")
name = "Sweekriti"
for i in range(0,len(name)):
    print(name[i], end = " ")'''

n = 0
while n<5:
    p = int(input('enter principle amount:'))
    t = int(input('enter time:'))
    r = int(input('enter rate:'))
    SI = (p*t*r)/100
    print(f' the simple interest is {SI}')
    n += 1







