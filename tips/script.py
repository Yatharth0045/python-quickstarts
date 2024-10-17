from functools import reduce

## 1. print end and sep

print('apple','mango')
print('apple','mango',end='||\n', sep=';')

## 2. // and % at same time

q = 37 // 10
r = 37 % 10

print(q,r)
print(divmod(37,10))

## 3. check all or any in list

print(all([True, True, False]))
print(any([True, True, False]))

## 4. Operation on Class Attributes

class Dog:
    def __init__(self,name,age):
        self.name, self.age = name,age
        
dog = Dog('rocky', 11)

print(vars(dog))
print(hasattr(dog, 'nickname'))
print(getattr(dog, 'name'))
setattr(dog, 'nickname', 'tommy')
print(vars(dog))
delattr(dog, 'age')
print(vars(dog))

## 5. enumerate

alpha = ['a','b','c']

for i,x in enumerate(alpha):
    print(f"{i=} {x=}")
    
## 6. map. reduce, filter

my_list = list(range(1,11))
print(my_list)
# map
str_list = list(map(str, my_list))
print(str_list)
# filter
even_list = list(filter(lambda e:e%2==0, my_list))
print(even_list)
# reduce
total = reduce(lambda a,b:a+b, even_list)
print(total)

## 7. sort vs sorted

list = [1,5,3,8,2,7,6]
list2 = sorted(list)
list.sort()
print(list)
print(list2)

## 8. sort custom condition

p_list = ['pp', 'pppp', 'p', 'ppp', 'pppppp', 'ppppp']

# using function
def condition(char):
    return len(char)
p_list.sort(key=condition)
# or using lambda
p_list.sort(key=lambda x:len(x))

print(p_list)

## 9. Key in max and min

ls = ['four','six','sevenxx','threee']
print(max(ls, key=lambda x:len(x)))
print(min(ls, key=lambda x:len(x)))