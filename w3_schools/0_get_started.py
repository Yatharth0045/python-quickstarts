import sys
import random

print(sys.version)
print(sys.version_info)
print(sys.platform)

## Single line comments

"""
Multiline
comments
use in python    
"""

x = 5
y = float(7)
print(type(y))

a, b, c = 'one', 'two', 'three'

fruits = ["apple", "banana", "cherry"]
x, y, z = fruits

print(x,y,z)

# Global variables

name = 'Yatharth'

def person():
    global age 
    age = 10
    
person()
print(name,age)

# Data types
""" 
Text Type:	    str
Numeric Types:	int, float, complex
Sequence Types:	list, tuple, range
Mapping Type:	dict
Set Types:	    set, frozenset
Boolean Type:	bool
Binary Types:	bytes, bytearray, memoryview
None Type:	    NoneType
"""

# Setting data types
a = 'name'
a = str(5)
a = 20
a = int(30)
a = 20.7
a = 35e3 # 35000.0
a = int(35E3) # 
print(a)
a = float(19)
a = 1j # j is imagianry part
a = complex(1j)
a = ['a','b','c'] # list
a = list(('a','b','c'))
a = ('a','b','c') # tuple
a = tuple(('a','b','c'))
a = range(6) # 0-5
a = {'name': 'Yatharth', 'age': 29} # dict
a = dict(name='Yatharth', age=29)
a = {'a','b','c'} # set
a = set(('a','b','c'))
a = frozenset({'a','b','c'})
a = True
a = bool(5)
a = b'Hello'
a = bytes(5)
a = bytearray(5)
a = memoryview(bytes(5))
a = None

random_no = (random.randrange(1,10)) # 1 to 9
print(random_no)