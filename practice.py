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
