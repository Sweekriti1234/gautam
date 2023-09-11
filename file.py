#file handling
#file read
'''file1 = open("abc.txt","r")
read_content = file1.read()
print(read_content)
file1.close()'''

#writing in file

'''with open("abc.txt", "w") as file2:
    #.write() method
    file2.write("I edited this file ")
    file2.write("This is write mode")'''

'''#append
with open("abc.txt", "a") as file2:
    file2.write("This file has been edited.\n ")
    file2.write("New data has been added.")

with open("abc.txt", "r") as file2:
    file2.seek(5)
    read1 = file2.readline()
    print(read1)'''
    
count = 0
file2 = open("abc.txt", "r")
while count<17:
    print(file2.readline())
    count+=1

#writeline