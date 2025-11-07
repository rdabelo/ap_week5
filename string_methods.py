
def string_method():


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