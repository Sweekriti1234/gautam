num = [1, 2, 3, 4, 5, "1", "one", 1]
''' print(num)
emp = [] #emp list
print(type(num))

#accessing elements using index 

a = num[0]
last = num[-1]
length_list = len(num)
 #slicing like strings
sliced = num[0:5] #var[start_index : end_index+1]
print(sliced)

 #looping in lists using while and for

for i in num:
    print(i)'''

i=0
while i<len(num):
    print(num[i])
    i += 1
#list concatention
num1 = [1, 2, 3, 4]
num2 = [5, 6, 7]
print(num1 + num2)

#converting tuple and string to list
name = "Sweekriti"
new_name = list(name)
print(new_name)



