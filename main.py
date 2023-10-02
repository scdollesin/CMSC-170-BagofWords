# EXERCISE #4 BAG OF WORDS
# AUTHOR: Samantha Shane C. Dollesin
# STUDENT NO.: 2020-01893
# SECTION: WX-1L
# PROGRAM DESCRIPTION: This program takes a message from an input file and determines the frequency of each unique word in it.

import re
import tkinter as tk
from tkinter.filedialog import askopenfilename

file = askopenfilename()
input = open(file, "r")

#Since the file contains only one message, readLine() is used without iteration
if (input.readable()):
    message = input.read()

input.close()

# Split compound words into two by replacing the '-' with a space
message = re.sub('(?<=\w)-(?=\w)', ' ', message)

# Split the message by the white spaces
raw_words = message.split()
words = []

for w in raw_words:
    w = ''.join(filter(str.isalnum, w))   # remove non-alphanumeric characters
    w = w.lower()                         # convert everything into lowercase
    if(w.isascii()):                      # disregard words with accented characters
        words.append(w)

# sort the list in alphabetical order and count the frequency of the words
words.sort()
frequency_tb = {}   #dictionary

for word in words:
    if (word in frequency_tb.keys()):
        frequency_tb[word] =  frequency_tb[word] + 1
    else:
        frequency_tb[word] = 1

#print(frequency_tb)

# display and export the data from the frequency table
output = open("output.txt","w")
size = str(len(frequency_tb.keys()))
total = str(sum(frequency_tb.values()))

print()
print("Dictionary Size: ", size)
output.write("Dictionary Size: " + size + "\n")
print("Total Number of Words: ", total + "\n")
output.write("Total Number of Words: " + total + "\n")

for key, value in frequency_tb.items():
    output.write(key + " " + str(value) + "\n")
    print(key, " ", value)

output.close()