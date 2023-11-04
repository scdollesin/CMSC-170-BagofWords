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

def getWords(message, words_list):
    # Split compound words into two by replacing the '-' with a space
    message = re.sub('(?<=\w)-(?=\w)', ' ', message)

    # Split the message by the white spaces
    raw_words = message.split()

    for w in raw_words:
        w = ''.join(filter(str.isalnum, w))   # remove non-alphanumeric characters
        w = w.lower()                         # convert everything into lowercase
        if w != '':                     
            words_list.append(w)

def createBag():
    folder = askdirectory()
    files_list = os.listdir(folder)
    words = []
    bag = {}

    for file in files_list:
        file_num = file[:4]
        file = folder+"/"+ file
        input = open(file, "r")

        if (input.readable()):
            message = input.read()
            
        input.close()
        
        getWords(message, words)

    # sort the list in alphabetical order and count the frequency of the words
    words.sort()

    for word in words:
        if (word in bag.keys()):
            bag[word] =  bag[word] + 1
        else:
            bag[word] = 1

    return bag, len(files_list)
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

spam_dict, spam_count = createBag()
ham_dict, ham_count = createBag()
spam_dictsize = len(spam_dict.keys())
ham_dictsize = len(ham_dict.keys())
spam_total = sum(spam_dict.values())
ham_total = sum(ham_dict.values())
P_Spam = spam_count/(spam_count+ham_count)
P_Ham = 1 - P_Spam

def filterSpam():
    folder = askdirectory()
    files_list = os.listdir(folder)
    
    for file in files_list:
        words = []
        frequency_tb = {}
        spamprob_tb = {}
        hamprob_tb = {}    
        
        file_num = file[:4]
        file = folder+"/"+ file
        input = open(file, "r")

        if (input.readable()):
            message = input.read()
            
        input.close()
        
        getWords(message, words)

        # sort the list in alphabetical order and count the frequency of the words
        words.sort()

        for word in words:
            if (word in frequency_tb.keys()):
                frequency_tb[word] =  frequency_tb[word] + 1
            else:
                frequency_tb[word] = 1
        
        for word in frequency_tb.keys():
            spamprob_tb[word] = frequency_tb[word]/spam_total       #P(w|Spam)
            hamprob_tb[word] = frequency_tb[word]/ham_total         #P(w|Ham)

        P_m_Spam = 1                        #P(message|Spam)
        for p in spamprob_tb.values():
            P_m_Spam = P_m_Spam * p

        P_m_Ham = 1                        #P(message|Ham)
        for p in hamprob_tb.values():
            P_m_Ham = P_m_Ham * p

        if (file_num == "1129"):
            print("ham total: ", ham_total)
            for i in frequency_tb.items():
                print(i)
            for i in hamprob_tb.items():
                print(i)           

            print("P(message|Ham): ",P_m_Ham)



filterSpam()