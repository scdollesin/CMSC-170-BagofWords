# EXERCISE #5 SPAM FILTERING
# AUTHOR: Samantha Shane C. Dollesin
# STUDENT NO.: 2020-01893
# SECTION: WX-1L
# PROGRAM DESCRIPTION: This program uses Naive Bayes classification to determine if files from the 'classify' folder
#                      contains a spam or ham message based on existing data ('spam' and 'ham' folder)

import os
import re
import tkinter as tk
from tkinter.filedialog import askdirectory
import decimal
from decimal import Decimal

folders = ["Spam", "Ham", "Classify"]
spam_dictionary = {}
ham_dictionary = {}
spam_dictsize = 0
spam_total = 0
ham_dictsize = 0
ham_total = 0
classification = []

count_spam = 0
count_ham = 0
P_spam = 0
P_ham = 0

output = open("classify.out","w")

for f in folders:
    folder = askdirectory(title= "Select "+ f + " Folder")
    files_list = os.listdir(folder)
    if (f == folders[0]): count_spam = len(files_list)
    elif (f == folders[1]): count_ham = len(files_list)

    for file in files_list:
        file_num = file[:4]
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
            if w != '':                     
                words.append(w)

        # sort the list in alphabetical order and count the frequency of the words
        words.sort()
        frequency_tb = {}   # dictionary for files in the classify folder
        spam_probability_tb = {}    # P(word|Spam)
        ham_probability_tb = {}     # P(word|Ham)

        for word in words:
            if (f == folders[0]):
                if (word in spam_dictionary.keys()): spam_dictionary[word] =  spam_dictionary[word] + 1
                else: spam_dictionary[word] = 1
            elif (f == folders[1]):
                if (word in ham_dictionary.keys()): ham_dictionary[word] =  ham_dictionary[word] + 1
                else: ham_dictionary[word] = 1
            elif (f == folders[2]):
                if (word in frequency_tb.keys()): frequency_tb[word] =  frequency_tb[word] + 1
                else: 
                    frequency_tb[word] = 1

                    if (word in spam_dictionary.keys()): 
                        spam_probability_tb[word] = spam_dictionary[word]/spam_total  #print("/ " , word)  # frequency of word IN spam / total words in spam  
                    else: 
                        spam_probability_tb[word] = 0; #print("X " , word)
                    if (word in ham_dictionary.keys()): 
                        ham_probability_tb[word] = ham_dictionary[word]/ham_total  # frequency of word IN ham / total words in ham
                    else: 
                        ham_probability_tb[word] = 0;
       
        if (f == folders[2]):
            #print(spam_probability_tb)
            P_messageSpam = 1
            for p in spam_probability_tb.values(): P_messageSpam = P_messageSpam*Decimal(p)
            #print("P_messageSpam: ", P_messageSpam)

            print(ham_probability_tb)
            P_messageHam = 1
            for p in ham_probability_tb.values(): P_messageHam = P_messageHam*Decimal(p)
            #print("P_messageHam: ", P_messageHam)

            P_message = (P_messageSpam* Decimal(P_spam)) + (P_messageHam*Decimal(P_ham))
            #print("P_message: ", P_message)
            try:  P_spamMessage = (P_messageSpam * Decimal(P_spam)) / P_message
            except (ZeroDivisionError, decimal.DecimalException): P_spamMessage = 0
           
            classification = ''
            if P_spamMessage < 0.5: classification = folders[1]
            else: classification = folders[0]

            output.write(file_num+ " " + classification + "\t" + str(P_spamMessage) + "\n")

    spam_dictsize = len(spam_dictionary.keys())
    spam_total = sum(spam_dictionary.values())
    ham_dictsize = len(ham_dictionary.keys())
    ham_total = sum(ham_dictionary.values())
 
    P_spam = count_spam/(count_spam+count_ham)
    P_ham = 1 - P_spam










# sort the words alphabetically
spam_dictionary = dict(sorted(spam_dictionary.items()))
ham_dictionary = dict(sorted(ham_dictionary.items()))

# display and write the results
print("HAM")
print("Dictionary Size: ", ham_dictsize)
print("Total Number of Words: ", str(ham_total) + "\n")

ham_bag = open("ham.out", "w")
ham_bag.write("HAM" + "\n")
ham_bag.write("Dictionary Size: " + str(ham_dictsize) + "\n")
ham_bag.write("Total Number of Words: " + str(ham_total) + "\n")
for key, value in ham_dictionary.items():
    ham_bag.write(key + " " + str(value) + "\n")

print("SPAM")
print("Dictionary Size: ", str(spam_dictsize))
print("Total Number of Words: ", str(spam_total) + "\n")

spam_bag = open("spam.out", "w")
spam_bag.write("SPAM" + "\n")
spam_bag.write("Dictionary Size: " + str(spam_dictsize) + "\n")
spam_bag.write("Total Number of Words: " + str(spam_total) + "\n")
for key, value in spam_dictionary.items():
    spam_bag.write(key + " " + str(value) + "\n")

output.close()
ham_bag.close()
spam_bag.close()