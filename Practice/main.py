# Azarm Piran
# Udemy - NLP - Natural Language Processing with Python by Jose Portilla


# 02-26-2023
# Section 2 - Python Text Basics
# F-string literals
x = "Azarm"
print(f"My name is {x}")

# a dictionary
MyDictionary = {'a':123, 'b':"abc"}
print(MyDictionary['a'])
print(f"my number is {MyDictionary['b']}")

MyList = [6,2,3]
print(f"my list is {MyList[0]}")

# Alignment / Example of tuples:
library = [('Author', 'Topic', 'Pages'), ('Twain', 'Rafting', 601), ('Feynman', 'Physics', 95), ('Hamilton', 'Mythology', 144)]
print(library)

for book in library:
    print(book)

# Lets say I only wanna see the Author Name
for book in library:
    print(f"The author name is: {book[0]}")

# Another way of accessing this tuple: important
for author,topic,pages in library:
    print(f"the Author is: {author}")