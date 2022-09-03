# Concatenate the string 'Thirty', 'Days', 'Of', 'Python' to a single string, 'Thirty Days Of Python'.
import string


sentence = str('Thirty ' + 'Days ' + 'Of ' + 'Python')
print(sentence)
print(type(sentence))


# Declare a variable named company and assign it to an initial value "Coding For All".
company = "Coding for All"
# Print the variable company using print().
print(company)
print(type(company))
# Print the length of the company string using len() method and print().
print(len(company))
# Change all the characters to uppercase letters using upper() method.
print(company.upper())
# Change all the characters to lowercase letters using lower() method.
print(company.lower())
# Use capitalize(), title(), swapcase() methods to format the value of the string Coding For All.
print(company.capitalize())
print(sentence.title())
print(sentence.swapcase())

# Cut(slice) out the first word of Coding For All string.
print(company[6::])


# Check if Coding For All string contains a word Coding using the method index, find or other methods.
print(bool(company.find('Coding')))

# Replace the word coding in the string 'Coding For All' to Python.
print(company.replace('Coding', 'Happiness'))

# Change Python for Everyone to Python for All using the replace method or other methods.
text = 'Python for Everyone'
new_text = text.replace('Everyone', 'All')
print(new_text)

# Split the string 'Coding For All' using space as the separator (split()) .
new_split = company.split(' ')
print(new_split)

# "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon" split the string at the comma.
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
print(companies.split(','))

# What is the character at index 0 in the string Coding For All.
string_is = 'Coding For All'
print(string_is[0])

# What is the last index of the string Coding For All.
print(string_is[-1])

# What character is at index 10 in "Coding For All" string.
print(string_is[10]) #returns space character

# Create an acronym or an abbreviation for the name 'Python For Everyone'.
phrase = "Python for Everybody"
new_phrase = phrase.split()
acronym = ""
for word in new_phrase:
  acronym = acronym + word[0].upper()
print(acronym)

# Use index to determine the position of the first occurrence of C in Coding For All.
text = "Coding For All"
print(text.find('C'))

# Use index to determine the position of the first occurrence of F in Coding For All.
text = "Coding For All"
print(text.find('F'))

# Use rfind to determine the position of the last occurrence of l in Coding For All People.
text = "Coding For All"
print(text.rfind('l'))

# Use index or find to find the position of the first occurrence of
# the word 'because' in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase.index('because'))

# Use rindex to find the position of the last occurrence of
# the word because in the following sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase.rindex('because'))

# Slice out the phrase 'because because because' in the following
# sentence: 'You cannot end a sentence with because because because is a conjunction'
phrase = 'You cannot end a sentence with because because because is a conjunction'
print(phrase.replace('because because because', ''))
