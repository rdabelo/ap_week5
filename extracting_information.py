def extract_information():

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