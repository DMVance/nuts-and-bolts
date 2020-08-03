#!/usr/bin/env python3
# This program allows the user to input a word, then breaks the word into individual
# letters and sorts alphabetically.

# Get the word(s) from the user
print("Please enter the words you would like to sort alphabetically. Press Enter when finished: ")
wrd = input("--> ")
print(wrd)
# split the string of words into individual words (eliminates spaces and obviates the need for c.pop(" ")?)
words = wrd.split()
print(words)

# Sort the letters in the list in alphabetical order
alpha = sorted(wrd.lower())

# provide the number of occurrences of each letter in each word and arrange alphabetically
import collections
c = dict(collections.Counter(alpha))
c.pop(" ") # removes spaces from the dictionary so that they are not included in the final output
print(c)

mystring = c.items()
print(mystring)

s = ""
for k,v in c.items():
    if c[k] != 1:
        #print("{}({}) ".format(k, c[k]), end="")
        s = s + str(k) + "(" + str(c[k]) + "), "
    else:
        #print("{} ".format(k), end="")
        s = s + str(k) + ", "

print(s[:-2]) # eliminates the comma after the last printed element

# Output to a usable format, such as PowerPoint, PDF, even Word or Text file

# if __name__ == '__main__': main()