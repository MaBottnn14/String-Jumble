"""
stringjumble.py
Author: maBottnn14
Credit: Mr. Heely, Andrew, and https://developers.google.com/edu/python/lists 

Assignment:

The purpose of this challenge is to gain proficiency with 
manipulating lists.

Write and submit a Python program that accepts a string from 
the user and prints it back in three different ways:

* With all letters in reverse.
* With words in reverse order, but letters within each word in 
  the correct order.
* With all words in correct order, but letters reversed within 
  the words.

Output of your program should look like this:

Please enter a string of text (the bigger the better): There are a few techniques or tricks that you may find handy
You entered "There are a few techniques or tricks that you may find handy". Now jumble it:
ydnah dnif yam uoy taht skcirt ro seuqinhcet wef a era erehT
handy find may you that tricks or techniques few a are There
erehT era a wef seuqinhcet ro skcirt taht uoy yam dnif ydnah
"""
m = str(input("Please enter a string of text (the bigger the better): "))
print('You entered "'+m+'". Now jumble it: ')
b =len(m)
#first line -- searched around after being confused and learned how to reverse a string with help from Mr. Heely(Healy?) 
def reverse(m):
    str = ""
    for i in m:
        str = i+str 
    return str
print(reverse(m))

"""second line -- different method because the previous method produced the string without a space,
even when I played around with the split and join functions. Andrew taught me how to use the double colon."""
l =[""]
o = ""
for a in m:
    if a!= "":
        o=o+a
    if a == " ":
        l.append(o) #https://developers.google.com/edu/python/lists
        o = ""
l.append(o)
b = ' '.join(l[::-1])
print(b)

#third line -- same method
y =[]
h = ""
for z in m:
    if z != " ":
        h = h + z
    if z == " ":
        y.append(h[::-1])
        h = ""
y.append(h[::-1])
z = ' '.join(y)
print(z)






