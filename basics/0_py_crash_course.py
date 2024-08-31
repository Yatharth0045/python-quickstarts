# https://www.youtube.com/watch?v=VchuKL44s6E

#### Datatypes && Variables

x = 20

y = 34.8

string_a = 'abc'
string_b = "abc"
bool_val = True

#### Output and Printing

print(bool_val, x,y, end="||")

#### User Input

# name = input('Name: ')
# print(name)

#### Arithmetic Operator

print(int(1235/7))  # return int
print(1235/7)       # return float
print(1235//7)      # return int
print(string_a.count('b'))

print(type(12//4))
print(type('lol'))

#### String Operator

print('test_string'.upper().lower().capitalize().count('t'))

print(ord('A'))

#### Conditional Operator && Chained Conditionals

print(11 > 6 and not False or True)

#### If else 

if 5 < 3:
    print('yess')
else:
    print('no')
    
x = [4, True, 'nope']

print(len(x),x.append('yatharth'),x, len(string_a))

x.extend([9,8,7,6])

print(x)

print(x.pop(2),x)

try:
    print(x.pop(9),x)
except Exception as e:
    print(e)
    
print('Program running')

#### Lists

x = [1,2,3]
y = x
z = x[:]

x[1] = 10

print(x,y,z)
print(x[0:4])

#### Tuples

u = (0,0,2,3)
print(u)

#### Set

set_y = set(u)
print(set_y)


if 0 in set_y:
    print('yes')
else:
    print('no')

set_x = set([2,3,4,5,6,7,55,43,2,3,4,5,6])
print(set_x)

print(set_x.union(set(('a','v'))))

print(set_x.intersection(set((2,3,4,5,6))))

print(set_x.difference(set((2,3,4,5,6))))

#### Dict

x = {1 : 5, 2:11, 3:55, 4:25}

print(x)

print(x[2])

print(x.keys())

print(list(x.keys()))
print(list(x.values()))

print('3 exist ?', 3 in x)
del x[3]
print('3 exist ?', 3 in x)
print('11 exist in values ?', 11 in x.values())

#### For loops

for k,v in x.items():
    print(k, 'with value', v)

for k in x:
    print(k,'=',x[k])

for i in range(1,10,2):
    print(i)

#### While loops

i = 1
while(i < 10):
    print('while',i)
    i += 1
    
arr = [2,3,4,5,6,7,22,11,55,33,55]
for i in range(len(arr)):
    if i == 3:
        continue
    print(i, arr[i])
    if i == 5:
        break
    
#### slice operator

name = 'aabbcc'

print('x' in name)
print(4 in arr)
print(55 in set_x)
print(33 in set(arr))

# for i in range(len(name)):
#     for j in range(i + 1, len(name)):
#         print(name[i:j])

# for i in range(len(name)):
print(name[::-1])

# 0 1
# 0 2
# 0 3
# 0 4
# 1 2
# 1 3
# 1 4
# 2 3
# 2 4
# 3 4

# print(name)

# for i in range(len(name)):
#     print(i)

# print(name[0:8])

#### comprehensions

x = [x * 2 for x in range(5)]
x = [x for x in range(50) if x % 5 == 0 ]

print(x)

#### Functions

def d1 (x,y,z=None):
    print('Run',x,y)
    return x+y,x-y

# returns multi value as tuple
result = d1(20,15)
print(result)
print(type(result))
a,b = result
print(a,b)

#### args and kwargs

def func(*args, **kwargs):
    pass

x = [1,2,3,4,5]

print(x)
print(*x)

def sum(*args,**kwargs):
    sum = 0
    print(args)
    for i in args:
        sum += i
    print(kwargs)
    return sum

print(sum(1,2,3,4,5,6,7,8,9,10,x=11,y=12))

#### Scope local and global

x = 'tim'
y = 'tim'

def change_name(name):
    global x
    x = name
    y = name
    
print('before',x,y)
change_name('tom')
print('after',x,y)

#### Exceptions in python

try:
    if True:
        raise Exception('ErrorHere')
    else:
        print('all well')
except Exception as e:
    print('program continued with issue',e)
finally:
    print('try-catch ends here')

#### lambda

x  = lambda arg_a,arg_b : arg_a * arg_b 
print(x(12,5))

#### map and filter

x = [1,2,3,4,5,6,7,8,9,10]
even = filter(lambda e : e % 2 == 0,map(lambda i : i * 3, x))
print(list(even))

#### f strings

name = 'yatharth'
age = 29
x = f'hello {name}, with age {age}'
print(x)