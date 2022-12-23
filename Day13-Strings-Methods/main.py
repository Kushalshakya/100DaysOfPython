# Strings Methods
# Strings are immutable

#Keywords:
    # upper()
    # lower()
    # strip()
    # rstrip()
    # replace()
    # split()
    # capitalize()
    # center()
    # count()
    # endswith()
    # find()
    # index()

a = "!!!!Kushal!!!!!!"
print(len(a))
print(a.upper())
print(a.lower())

# It does not change the strings but creates a new string so called immutable Strings

stripEl = " Hello World "
print(stripEl.strip())

print(a.rstrip("!"))
# rstrip() basically what it does is it removes a specific letter from the string but it won't be working at the beginning of a string

names = "Kushal,Ram,Rohan,Ruchi,Rahul,Rikesh"
print(names.replace("Kushal", "Riya"))
# replace() can change multiple strings with the same name

splitNames = "Aayush Aasha Ashim Ayusha Abinav"
print(splitNames.split())
#split() splits the names into lists

blogHeading = "introduction to python"
print(blogHeading.capitalize())

el= "\nThis is the text which is going for the center string method"
print(el.center(100))

print(el.count("i"))

str1 = "Welcome to the Console !!!"
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))

print(names.find("Ru"))
print(names.find("Ru"))
# print(names.index("abcd"))
# Mostly used when we are sure about the string we are finding is correct