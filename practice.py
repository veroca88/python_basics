# To print anything use print
print('hello world')

# Python uses Dynamic Typing (JS, C++ is statically-typed)
my_brothers = 2
type(my_brothers)
output int

# Assign to the same variable a different value
my_brothers = ["Paul", "Jonh"]
output list

# To check the length of the string
len('I love hiking')
output 13

# indexing
myString = "I love the mountains"
myString[0]
output I

# Reverse indexing
myString[-2]
output n

# Slice string starting at 2 index (up to but not included)
myString[2:]
output love the mountains

# Slice string starting from 0 to 4 index (up to but not included)
myString[:4]
output I lo

# Slice string in the middle
myString[2:6]
output love

# Catch all the string but jump "I love the mountains"
myString[::2]
output Ilv h onan

# Reverse an string
myString[::-1]
output sniatnuom eht evol I

# Concatenation or multiplication between letters and numbers
letter = 'z'
letter * 10
output 'zzzzzzzzzz'

'2' + '3' = '23'
2 + 3 = 5

# Methods

myString.upper()
output 'I LOVE THE MOUNTAINS'

myString.split()
output['I', 'love', 'the', 'mountains']

# format() method
print("Here I'm using {} method".format("FORMAT"))
output Here I'm using FORMAT method

print("Python is {} {} {}".format("intuitive", "easy", "fast"))
output Python is intuitive easy fast

print("Python is {2} {1} {0}".format("intuitive", "easy", "fast"))
output Python is fast easy intuitive

print("Python is {f} {i} {e}".format(i="intuitive", e="easy", f="fast"))
output Python is fast intuitive easy

# Float formatting -> {value:width.precision f}
result = 100/777
output 0.1287001287001287
# 3f means 3 decimals
print("The result was {r:1.3f}".format(r=result))
output The result was 0.129

# f string
name = 'Vero'
print(f'Hi, my name is {name}')
output Hi, my name is Vero

# List (JS an array)

another_list = [4, 5, "six"]
my_list = ['one', 2, "three"]
my_list[0] = 'one'
new_list = my_list + another_list
new_list = ['one', 2, 'three', 4, 5, 'six']

# Add element at the end of the list
new_list.append('seven')
new_list = ['one', 2, 'three', 4, 5, 'six', 'seven']

# Remove last element of the list
new_list.pop()
output 'seven'
print(new_list) = ['one', 2, 'three', 4, 5, 'six']

# Can save the item removed
popped_item = new_list.pop()
popped_item = "six"
print(new_list) = ['one', 2, 'three', 4, 5]

# Remove any item of the list with the index number
new_list.pop(0)
print(new_list) = [2, 'three', 4, 5]

# Sort Method
list_vowels = ['u', 'o', 'i', 'e', 'a']
list_vowels.sort()
output['a', 'e', 'i', 'o', 'u']

#  Reverse Method
list_vowels.reverse()
output
['u', 'o', 'i', 'e', 'a']

#  Dicctionaries (JS object)
prices_lookup = {'apple': 2.99, 'orange': {
    'normal': 1.99, 'organic': 3.99}, 'milk': 5.80}
prices_lookup['apple'] = 2.99
prices_lookup['orange']['organic'] = 3.99

prices_lookup.values()
output dict_values([2.99, {'normal': 1.99, 'organic': 3.99}, 5.8])

prices_lookup.keys()
output dict_keys(['apple', 'orange', 'milk'])

prices_lookup.items()
output dict_items([('apple', 2.99), ('orange', {'normal': 1.99, 'organic': 3.99}), ('milk', 5.8)])

# Tuples are immutables and uses ( ) cares about data integrity
tuple_list = (1, 2, 3)
number_list = [1, 2, 3]
type(tuple_list) = tuple
type(number_list) = list

number_list[0] = "One"
output['One', 2, 3]

tuple_list[0] = "One"
output ERROR

# Tuples has only two methods
count() Returns the number of times a specified value occurs in a tuple
index() Searches the tuple for a specified value and returns the position of where it was found

# Sets only acepts uniques values
myset = set()
myset.add(2)
output {2}
myset.add(1)
output {1, 2}
# Return unique values in the list
mylist = [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 4]
set(mylist)
output {1, 2, 3, 4}

set([1, 1, 2, 3])
output {1, 2, 3}

# Create a .txt file from Jupiter-notebook
% % writefile myfile.txt
Hello this is a text file
this is second line

myfile = open('myfile.txt')
myfile.read()
output 'Hello this is a text file\nthis is second line\n'

myfile.read()
output ''
#  it looks like empty file but we need to put the cursor at the begining of the file

myfile.seek(0)
myfile.read()
output 'Hello this is a text file\nthis is second line\n'

myfile.seek(0)
myfile.readlines()
output['Hello this is a text file\n', 'this is second line\n']

# file location
pwd
# after open() a file best practice is always close it
myfile.close()

# to avoid errors due open files and not close it we can use with
# READ
with open('myfile.txt') as new_file:
    contents = new_file.read()

    contents
    output 'Hello this is a text file\nthis is second line\n'

# Depends on the mode
# r = read
# w = write (OVERWRITE OR CREATE A NEW ONE)
# a = append (ADD TO FILES)
# r+ = reading and writing
# w+ = writing and reading (OVERWRITE OR CREATE A NEW ONE)
with open('myfile.txt', mode='r') as readfile:
    contents_read = readfile.read()

with open('myfile.txt', mode='w') as readfile:
    contents_read = readfile.read()
    output ERROR

# WRITE
with open('myfile.txt', mode='w') as readfile:
    readfile.write("Check this new line")

with open('myfile.txt', mode='r') as readfile:
    print(readfile.read())
    output 'Hello this is a text file
    this is second line
    Check this new line'

#  Chaining Comparison Operators

1 < 2 < 3 = True
1 < 2 and 2 > 3 = False
1 == 1 or 2 == 2 = True
"h" == "h" or "i" == "j" = True
not (1 == 1) = False
1 != 1 = False

# If elif else Statements-> Control flow

if some_condition:
    # execute some code
elif some_other_condition:
    # do something different
else:
    # do something else

animal = 'cat'

if animal == 'dog':
    print("Wuau wuau")
elif animal == 'cat':
    print('Miauuu')
else:
    print("no animal")

# For loops
numbers_list = [1, 2, 3]
for number in numbers_list:
    print(number)
output
1
2
3

for number in numbers_list:
    if number % 2 == 0:
        print(number)
    else:
        print(f'Odd number {number}')
output
Odd number 1
2
Odd number 3

for number in numbers_list:
    list_sum = list_sum + number
    print(list_sum)
output
1
3
6

for letter in 'Hello World':
    print(letter)
output
H
e
l
l
o

W
o
r
l
d

groupLetters = [(1, 'a', 2), (3, 'b', 4), (5, 'c', 6), (7, 'd', 8)]
for a, b, c in groupLetters:
    print(b)
output
a
b
c
d

objectKeyValue = {'k1': 1, 'k2': 2, 'k3': 3}
for item in objectKeyValue:
    print(item)
output
k1
k2
k3

for item in objectKeyValue.items():
    print(item)
output
('k1', 1)
('k2', 2)
('k3', 3)

for key, value in objectKeyValue.items():
    print(value)
output
1
2
3

# While loop
# break: breaks out the current closest enclosing loop.
# continue: goes to the top of the closest enclosing loop.
# pass: does nothing at all

mystring = 'Sammy'
for letter in mystring:
    if letter == 'a':
        continue
    print(letter)
output
S
m
m
y

for letter in mystring:
    if letter == 'a':
        break
    print(letter)
output
S

# Useful operators

ascendingNumbers = [1, 2, 3, 4]
for number in range(-2, 11, 2):
    # start in -2,
    # goes to 11 but it does not include,
    # jump each 2
    print(number)
output
-2
0
2
4
6
8
10

# To put all those numbers inside a list
list(range(-2, 11, 2))
output
[-2, 0, 2, 4, 6, 8, 10]
