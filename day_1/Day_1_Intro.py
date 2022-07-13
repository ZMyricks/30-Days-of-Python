# compute the following operations. the operands are 3 and 4
# addition
print(3 + 4)
# subtraction
print(3 - 4)
# multiplication
print(3 * 4)
# modulus - remainder
print(3 % 4)
# division
print(3 / 4)
# exponential
print(3 ** 4)
# floor division operator - answer with no remainder
print(10 // 3)

# examples of strings
print('Raja')
print('Monet X Change')
print('Slay the house down boots!!!')

# check the data types using the type() function
print(type(10))
print(type(9.8))
print(type(4-4j))
print(type('Lola Bewood'))
print(type(['Katya', 'Willow Pill', 'Jada Essence Hall']))

# here are the data types
# number
print(1) #integer
print(type(1))
print(4.5) #float
print(type(4.5))
print(5-5j) #complex
print(type(5-5j))

# String
print('Hey Kitty Girl')
print(type('Hey Kitty Girl'))

# Boolean
a = True
b = False
print(type(a))
print(type(b))

# List
queens = ['Raja', 'Monet X Change', 'Katya']
print(queens[1])
print(type(queens))

# Tuple - a list that cannot be changed and uses parenthesis
tuple1 = (0, 1, 2, 3)
print(tuple1[1])
print(type(tuple1))

# Set - unordered, prints to console different each time, indexing has no weight
queen_set = {'Trinity the Tuck', 3, 'Legend'}
print(queen_set)
print(type(queen_set))
queen_set.add('Pearl') # add a single element
print(queen_set)
queen_set.update(['lola, 2'], {4, 'kitty'}) #update is to add multiple elements
print(queen_set)

# Dictionary - hold a Key:Value pair
my_Dict = {
  'love': "ganja",
  'need': "veggies",
  'study': "python",
  'year_written': 2022
}
print(my_Dict)
print(my_Dict['study'])

# Euclidian Distance equation {d(p,q)=|p-q|.}
p = 100
q = 20
d = abs(p - q) # abs() is the absolute function - the measure of a numbers distance from zero
print(d)
