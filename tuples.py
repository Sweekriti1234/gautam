#tuples 
'''a = (1, 2, "hello", 1.01, (1, 2, 3))

a[0] = 3
'''
#dictionary
roll_no = {1: "SWEEKRITI", 2: "SARINA", 3: "SUMINA"}
#accessing value using print
print(roll_no[1])
print(roll_no[2])
print(roll_no[3])

#updating data using keys
roll_no[1] = "Rohit"
roll_no[4] = "nEw StuDENT"
print(roll_no)

for ele in roll_no:
    print(ele)
# looping in dictionaries
#iterating over key-value pairs
for key, value in roll_no.items():
    print(f'{key}: {value}')
    print('-'*10)

#iterate over keys
for k in roll_no.keys():
    print(k)

 print("*" * 10)

#for simple ways in key
for k in roll_no:
    print(k)

#iterate over values
for v in roll_no.values():
    print(v)