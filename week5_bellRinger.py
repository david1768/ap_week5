# Problem Set 1: Indexing and Slicing Strings
# Basic Indexing:
# Given the string magic = 'abracadabra',
 magic = 'abracadabra',
# a. Retrieve the 5th character.
print(magic[4])
# b. Retrieve the second to last character.
print(magic[-2])
# c. Find the first occurrence of the letter 'c'.
print(magic.Index('c'))
# Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# a. Extract the letters 'hij'.
print(alphabet[7:10])
# b. Extract every second letter starting from 'a' to 'm'.
print(alphabet[:13:2])
# c. Reverse the entire string using slicing.
reversed_alphabet = alphabet[::-1] #notes
print(hig_index) #7
# Problem Set 2: Extracting Information
# From Descriptions:
# Extract the name of the famous personality from the quote "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
name = "John F. Kennedy"
print(quote.find('John F. Kennedy')) #78
personality_name = quote[78:] # cleaner
print(personality_)
# Manipulating Words:
# Given the string info = "Python is fun. Fun is good. Good is subjective.",
info = "Python is fun. Fun is good. Good is subjective."
# a. Extract the word 'subjective' without knowing its exact position.
print(info.split()[-1])
# b. Extract every third word.
print(info.split()[::3])
# c. Reverse the positions of the words, but keep the characters in each word in the same order.
' '.join(info.split()[::-1])
# Problem Set 3: String Methods
# Upper & Lower:
# Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
" MAY THE FORCE BE WITH YOU.".lower()
# String Joining and Splitting:
# Given the list motto = ["Make", "haste", "slowly."],
# a. Convert the list into a single string.
' '.join(motto)
# b. Now, split the string at every occurrence of the letter 'a'.
' '.join(motto).split('a')
# Replacing Words:
# Modify the sentence: "Life is what happens when you are busy making other plans."
# a. Replace "busy" with "distracted".
"Life is what happens when you are busy making other plans.".replace("busy", "distracted")
# b. Replace "plans" with "mistakes".
"Life is what happens when you are busy making other plans.".replace("plans", "mistakes")
# Problem Set 4: String Properties and Advanced Operations
# Repetition:
# Concatenate the word "Iteration" 7 times.
"Iteration" * 7
# Word Search:
# Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"

# Length and Count:
# a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# b. Count the number of times the letter 'i' appears in the same word/phrase.
len("Supercalifragilisticexpialidocious")
"Supercalifragilisticexpialidocious".count('i')
