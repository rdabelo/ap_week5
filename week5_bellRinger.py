# # Problem Set 1: Indexing and Slicing Strings
# # Basic Indexing:
# Given the string_
magic = "abracadabra"
# # a. Retrieve the 5th character.
print(magic[4])
# # b. Retrieve the second to last character.
print(magic[-2])
# # c. Find the first occurrence of the letter 'c'.
# print(magic.find[c])
# # Advanced Slicing:
# Given the string alphabet = 'abcdefghijklmnopqrstuvwxyz',
# # a. Extract the letters 'hij'.
print(magic[7:10])
alphabet = "abcdefghijklmnopqrstuvwxyz"
hij_index = alphabet.index('hij')
print(hij_index)
# # b. Extract every second letter starting from 'a' to 'm'.
magic[0:13:2]# # c. Reverse the entire string using slicing.
reversed_string = magic[::-1]
print(reversed_string) # How to reverse a string
# # Problem Set 2: Extracting Information
# # From Descriptions:
# # Extract the name of the famous personality from the 
quote = "Ask not what your country can do for you — ask what you can do for your country. - John F. Kennedy"
print(quote.find("John F Kennedy")) #78
personality_name = quote[78:]
print(personality_name) # John F. Kennedy
# # Manipulating Words:
# # a. Extract the word 'subjective' without knowing its exact position.
info = " Python is fun. Fun is good. Good is subjective"
print(info.rfind("subjective"))
subjective_word = info[36:] #clearer
print(subjective_word)
# # b. Extract every third word.
info =  "Python is fun. Fun is good. Good is subjective"
every_third_word = info [0:9:3]
# # c. Reverse the positions of the words, but keep the characters in each word in the same order.
reverse_string = info [::-1]
print(reverse_string)
# # Problem Set 3: String Methods
# # Upper & Lower:
# # Convert the following text to lowercase: "MAY THE FORCE BE WITH YOU."
Star_Wars = "MAY THE FORCE BE WITH YOU"
print(Star_Wars.lower)
# # String Joining and Splitting:
# # Given the list motto = ["Make", "haste", "slowly."],
# # a. Convert the list into a single string.
mottos = ["Make", "haste", "slowly."],
single_string = "". join(motto)
print(single_string)
# # b. Now, split the string at every occurrence of the letter 'a'.

# # Replacing Words:
# # Modify the sentence: "Life is what happens when you are busy making other plans."
OG = "Life is what happens when you are busy making other plans."
# # a. Replace "busy" with "distracted".
New_string = OG.replace("distracted","busy")
print(New_string)
# # b. Replace "plans" with "mistakes".
Newer_string = OG.replace("mistakes","plans")
print(Newer_string)
# # Problem Set 4: String Properties and Advanced Operations
# # Repetition:
# # Concatenate the word "Iteration" 7 times.
Word = "Iteration"
concatenated_word = Word * 7 
print(concatenated_word)
# # Word Search:
# # Check if the word "moonlight" appears in the quote: "With freedom, books, flowers, and the moon, who could not be happy? - Oscar Wilde"
word_to_find = moonlight
if word_to_find
# # Length and Count:
# # a. Calculate the number of characters (including spaces and punctuation) in the word/phrase: "Supercalifragilisticexpialidocious".
# # b. Count the number of times the letter 'i' appears in the same word/phrase.
letter_to_count = "I"
count = phrase.count(letter_to_count)
print(f"The letter '(letter_to_count)' appears  (count) times in the phrases.")
