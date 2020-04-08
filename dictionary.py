"""
Create a dictionary with key value pairs to
represent words (key) and its definition (value)
"""
# establishes that word_defintions is a dictionary(object), can hold multiple keys and values
word_definitions = dict()

"""
Add several more words and their definitions
   Example: word_definitions["Awesome"] = "The feeling of students when they are learning Python"
"""
# these are objects, the key is the word and the value is the definition
word_definitions['cool'] = 'smooth, classy and never lame'
word_definitions['lame'] = 'not smooth, mood killer'

"""
Use square bracket lookup to get the definition of two
words and output them to the console with `print()`
"""
# printing by accessing word_definitions and then placing the key in the brackets, which give the value, or definition in this case
print(word_definitions['cool'])
print(word_definitions['lame'])


"""
Loop over the dictionary to get the following output:
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
    The definition of [WORD] is [DEFINITION]
"""
# for in loop, word and definition are taco/placeholders, in says go to word_definitions and with
# the .items method, return all the keys and their values, then print the key with the value
for word, definition in word_definitions.items():
    print(f'the defintion of {word} is {definition}')