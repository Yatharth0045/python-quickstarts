## concepts of python - 101
## https://youtu.be/mMv6OSuitWw

## Immutable and Mutable datatypes

def get_max(list):
    list.sort()
    return list[-1]

my_list = [7,4,6,1,9,3,2]
print(my_list)
max = get_max(my_list)
print(my_list)

## Immutable 

x = (1,2)
y = x
x = (1,2,3)

print(x,y)

x = [1,2]
y = x
x[0] = 100

print(x,y)

## List comprehensions

x = [x for x in range(10) if x % 2 == 0]
print(x)

## Funtion argument and parameter types
# Positional arg
# Keyword arg
# optional arg | default value
# *args -> any no of positional arguments
# **kwargs -> any no of keyword arguments

def fun(x,y,z=None, *args, **kwargs):
    if z == None:
        print(x,y)    
    else:
        print(x,y,z)
    print(args) # stored as a tuple
    print(type(args))
    print(kwargs) # stored as a dict
    print(type(kwargs))
    print(kwargs.keys())
    pass

fun(1,2)
fun( y = 1, x = 2)
fun(1, y=2)
fun(1, y=2, z = 3)
fun(1,2,3,4,5,6)
fun(1,2,3,4,5,6,m='a',n='b')