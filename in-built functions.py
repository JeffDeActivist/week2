# absolute value
print(abs(-63 + 4j))
# all
x = [2, 3, 4]
print(all(x))
# ascii
name = "jeff is a very strange person"
print(ascii(name))
x = [i for i in range(100)]
print(ascii(x))
# bool
a = 4
print(bool(a))
print(bool(4 > 7))


# getattr

class Getattr:
    age = 5
    name1 = "jeff"


print(getattr(Getattr, 'age'))  # used with objects
# id
y = 4
print(id(y))
# len
c = [1, 2, 4, 7, 'g', 'r']
print(len(c))
print(len("JeffDeActivist"))
# min and max
d = [1, 2, 4, 74, 839, 393, 383, 393, 293]
print(min(d))
print(max(d))
print(max('a', 'f', 'jeff'))
# pow
print(pow(2, 3))
# setattr
setattr(Getattr, 'age', 14)  # used with objects
# sorted
print(sorted(d, reverse=True))  # returns in a descending order
print(sorted(d, reverse=False))  # return in ascending order
# type
print(type(Getattr))
print(type(d))
print(type(y))
age = 10
if isinstance(age, int):
    print(age)
i = [x for x in range(10)]
print(i)
