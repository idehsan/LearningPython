#The Zen of Python by Tim Peters
import this

#_____Arithmetic Operators_____
x = 5
y = 2
# division
result1 = x/y
# multiplication
result2 = x*y
# floor division
result3 = x//y
# to the power of
result4 = x**y
# mod
result5 = x % y
print(result1, result2, result3, result4, result5)
# ----------------------------------------------------------------------------


# redefine the type of the objects
make_string = str(12)
make_int = int('12')
print(type(make_string))
print(type(make_int))


# _____STRING BASIC FUNCTIONS_____
my_string = 'my Hello World'
# capitalize first letter of string
out1 = my_string.capitalize()

# get number of defined sub string in the main string
out2 = my_string.count('l')

# boolean function for checking that string star or end with defined substring
out3 = my_string.endswith('d')
out4 = my_string.startswith('H')

# get the index of sub string with difference of not finding sub string
# 'find' gets -1 if it doesnt find anything
out5 = my_string.find('o')
out6 = my_string.find('z')
# 'index' gets error if doesnt find anything
out7 = my_string.index('o')
out8 = my_string.index('z')

# merge strings to one
output1 = '-'.join(['1', '2', '3', '4', '5', '6', '7'])
print(output1)

# lower and upper function in strings
lower_str = 'sALAm'.lower()
upper_str = 'sALAm'.upper()
print(lower_str, upper_str)

# replace sub strings with another one in string
my_string = 'my Hello World'
new_string1 = my_string.replace('l', '9')
# split string by a sub string
new_string2 = my_string.split('l')
new_string3 = [i for i in new_string2 if len(i) != 0]
print(new_string1, new_string2, new_string3)
# ----------------------------------------------------------------------------


# _____Arrays_____
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
r1 = my_list[0]
# reverse indexing from 1
r2 = my_list[-1]
r3 = my_list[3:4]
r4 = my_list[2:-1]
r5 = my_list[:-2]
# [begin:end:step]
r6 = my_list[1:9:2]
# reverse list
r7 = my_list[::-1]
print(r1, r2, r3, r4, r5, r6, r7)

# adding element at the end of the string
my_list.append(7)
# Out[47]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 7]

# adding element with indexing
my_list.insert(3, 12)
# Out[49]: [1, 2, 3, 12, 4, 5, 6, 7, 8, 9, 7]

# remove element by defining itself(removing the first '12' in the string)
my_list.remove(12)
# Out[60]: [1, 2, 3, 4, 5, 6, 7, 8, 9, 7]

# remove elements with indexing
my_list.pop(0)
# Out[61]: [2, 3, 4, 5, 6, 7, 8, 9, 7]

# reverse the list
my_list.reverse()
# Out[76]: [9, 8, 6, 5, 4, 3, 2, 1]

# remove all elements
my_list.clear()
# ----------------------------------------------------------------------------


# _____Dictionary_____
my_Dic = {'Alex': 12, 4: 0, 'my': []}
o1 = my_Dic['Alex']
my_Dic.keys()
# ----------------------------------------------------------------------------


# _____LOOP_____
list(range(1, 10))
# [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(1, 5):
    print(i)

list1 = [1, 3, 5, 7, 9]
for j in list1:
    print(j, end=" ")
# ----------------------------------------------------------------------------


# _____Function_____
def my_func(num1, num2, num3):
    return num1+num2+num3

# Lambda function is a small anonymous function.
# Syntax lambda arguments : expression
func1 = lambda a,b: a*b
print(func1(2, 3))
# ----------------------------------------------------------------------------


# _____Input & Output_____
my_input = float(input("Enter Your Number:"))
print(my_input)

# input number in one line
a, b = input().split()
a = int(a)
b = int(b)
print(a+b)
# ----------------------------------------------------------------------------


# _____Input & Output_____
print('The first variable is {} and the second variable is {}'.format('one', 'two'))

print('{:10}'.format('Alireza'))
print('{:10}'.format('Mona'))

print('{:>10}'.format('Alireza'))
print('{:>10}'.format('Mahsa'))
print('{:_>10}'.format('test'))

print('{:d}'.format(42))
print('{:04d}'.format(42))

print('{:2.3f}'.format(42))
print('{:06.4f}'.format(3.141592653589793))
# ----------------------------------------------------------------------------


# _____Class_____
from numpy import mean


class Classroom:
    def __init__(self, name, teacher, number_of_students, marks):
        self.name = name
        self.teacher = teacher
        self.number_of_students = number_of_students
        self.marks = marks
        assert len(marks) == number_of_students, 'Number of students does not match the marks list.'

    def average(self):
        print(mean(self.marks))


classroom_1 = Classroom('A', 'Javad', 5, [20, 19, 17, 19, 16])
classroom_1.number_of_students
classroom_1.average()


class Power:
    def __init__(self, pow_):
        self.pow = pow_

    def __call__(self, x):
        for i in x:
            print(i ** self.pow)


x = [1, 2, 3, 4, 5, 6]
pow2 = Power(2)
pow2(x)
# ----------------------------------------------------------------------------
