import re

input = open("input.txt")

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
    if(w.isascii()):                         # disregard words with accented characters
        words.append(w)

words.sort()
frequency_tb = {}

for word in words:
    if (word in frequency_tb.keys()):
        frequency_tb[word] =  frequency_tb[word] + 1
    else:
        frequency_tb[word] = 1

#print(frequency_tb)

output = open("output.txt","w")

size = str(len(frequency_tb.keys()))
total = str(len(frequency_tb.keys()))

print()
print("Dictionary Size: ", size)
output.write("Dictionary Size: " + total + "\n")
print("Total Number of Words: ", size + "\n")
output.write("Total Number of Words: " + total + "\n")

for key, value in frequency_tb.items():
    output.write(key + " " + str(value) + "\n")
    print(key, " ", value)