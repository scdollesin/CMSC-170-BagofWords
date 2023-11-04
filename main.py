# EXERCISE #4 BAG OF WORDS
# AUTHOR: Samantha Shane C. Dollesin
# STUDENT NO.: 2020-01893
# SECTION: WX-1L
# PROGRAM DESCRIPTION: This program takes a message from an input file and determines the frequency of each unique word in it.

import re
import os
import tkinter as tk
from tkinter.filedialog import askdirectory
from tkinter.filedialog import askopenfilename

spam_dict = {}
ham_dict = {}

def createBag(bag):
    folder = askdirectory()
    files_list = os.listdir(folder)
    words = []

    for file in files_list:
        file_num = file[:4]
        print(file_num)
        file = folder+"/"+ file
        input = open(file, "r")
        
        if (input.readable()):
            message = input.read()

            input.close()

            # Split compound words into two by replacing the '-' with a space
            message = re.sub('(?<=\w)-(?=\w)', ' ', message)

            # Split the message by the white spaces
            raw_words = message.split()

            for w in raw_words:
                w = ''.join(filter(str.isalnum, w))   # remove non-alphanumeric characters
                w = w.lower()                         # convert everything into lowercase
                if w != '':                     
                    words.append(w)

    # sort the list in alphabetical order and count the frequency of the words
    words.sort()

    for word in words:
        if (word in bag.keys()):
            bag[word] =  bag[word] + 1
        else:
            bag[word] = 1

    #print(bag)

# display and export the data from the frequency table
#output = open("output.txt","w")
#size = str(len(bag.keys()))
#total = str(sum(bag.values()))

#print()
#print("Dictionary Size: ", size)
#output.write("Dictionary Size: " + size + "\n")
#print("Total Number of Words: ", total + "\n")
#output.write("Total Number of Words: " + total + "\n")

#for key, value in bag.items():
#    output.write(key + " " + str(value) + "\n")
#    print(key, " ", value)

#output.close()

createBag(spam_dict)
createBag(ham_dict)