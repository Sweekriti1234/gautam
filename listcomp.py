'''#WAP to add 10 numbers from 1 to 10 in a list.
a = []
i=1 
while len(a)<10 :
    a.append(i)
    i+=1
print(a)
nums= []
for i in range(1,11):
    nums.append(i)
print(nums)

b= [i for i in range(1,11)]
print(a)
'''

'''a=[]
for i in range(1,11):
    b= i**2
    a.append(b)
print(a)

a= [i**2 for +i in range(1,11)]
print(a)'''
evens = [i for i in range(1,11) if i%2==0]
print(evens)
