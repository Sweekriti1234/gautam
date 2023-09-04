''' def add():
    return 2 + 3
print(add())

def sub(num1, num2):
    subt= num1 - num2
    return subt

output = sub(2, 3)
print(output) 

def name(first, sur):
    full = first + " " + sur
    return full
output = name("Sweekriti", "Gautam")
print(output)

pi = 3.141 #global variable
def area_circle(radius):
    pi = 3.14 # local variable
    area= pi * radius**2
    return area
print(area_circle(5))
print(area_circle(3))

def circumference(rad):
    perimeter= 2* pi* rad
    return perimeter

print(circumference(10))
print(circumference(5)) 

#default parameters
def add(num1=0, num2=0):
    sum = num1 + num2
    return sum
print(add())

def conv(hour):
    min = hour * 60
    sec = hour * 60 * 60
    return min, sec
print(conv(1))
print(conv(3))
min, sec = conv(2)
print(min, sec)'''

def mult(pos, *args, **kwargs):
    print(f'First arguement : {pos}')
    prod = 1
    for arg in args:
        prod *= arg
        print(prod)
    for kw in kwargs:
         print(kw, kwargs[kw])

mult(1, 2, 3, 4, 5, 6, 7, 8, 9, a = "meh", b = "huh")