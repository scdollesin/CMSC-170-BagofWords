# EXERCISE #4 BAG OF WORDS
# AUTHOR: Samantha Shane C. Dollesin
# STUDENT NO.: 2020-01893
# SECTION: WX-1L
# PROGRAM DESCRIPTION: This program takes a message from an input file and determines the frequency of each unique word in it.

import os
import re
import tkinter as tk
from tkinter.filedialog import askdirectory

folders = ["Spam", "Ham", "Classify"]
spam_dictionary = {}
ham_dictionary = {}
spam_dictsize = 0
spam_total = 0
ham_dictsize = 0
ham_total = 0

for f in folders:
    folder = askdirectory(title= "Select "+ f + " Folder")
    print(folder)
    files_list = os.listdir(folder)

    for file in files_list:
        file = folder+"/"+ file
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
            #if(w.isascii()):                     
            words.append(w)

        # sort the list in alphabetical order and count the frequency of the words
        words.sort()
        if (f == folders[2]): frequency_tb = {}   # dictionary for files in the classify folder

        for word in words:
            if (f == folders[0]):
                if (word in spam_dictionary.keys()): spam_dictionary[word] =  spam_dictionary[word] + 1
                else: spam_dictionary[word] = 1
            elif (f == folders[1]):
                if (word in ham_dictionary.keys()): ham_dictionary[word] =  ham_dictionary[word] + 1
                else: ham_dictionary[word] = 1
            elif (f == folders[2]):
                if (word in frequency_tb.keys()): frequency_tb[word] =  frequency_tb[word] + 1
                else: frequency_tb[word] = 1

        #print(frequency_tb)

# display and export the data from the frequency table
#output = open("output.txt","w")

spam_dictsize = len(spam_dictionary.keys())
spam_total = sum(spam_dictionary.values())
ham_dictsize = len(ham_dictionary.keys())
ham_total = sum(ham_dictionary.values())
                    
print("HAM")
print("Dictionary Size: ", ham_dictsize)
print("Total Number of Words: ", str(ham_total) + "\n")
print("SPAM")
print("Dictionary Size: ", spam_dictsize)
print("Total Number of Words: ", str(spam_total) + "\n")

#for key, value in frequency_tb.items():
    #output.write(key + " " + str(value) + "\n")
    #rint(key, " ", value)

#print()
#output.close()