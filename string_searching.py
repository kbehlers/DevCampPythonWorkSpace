

#Generally regex will be a more powerful option than these

sentence = "The quick brown fox jumped over the lazy dog."

#finds the index of the substring
#returns -1 if not found
query = sentence.find("quick")

print(query)

#index also returns the index of the substring
#returns an error (ValueError) if not found
query = sentence.index("quick")


#MOST USED, and most pythonic and pairs nicely with an if statement
#returns True or False
query = "fox" in sentence

print(sentence.lstrip("quick"))