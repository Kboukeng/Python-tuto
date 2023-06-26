word = "HELLO"
letters: set[str] = set(word)
print(letters)

sentence = "the day is bright"
lett: set[str] = set(sentence)
print(lett)

# Convert the sentence to a list of words
word_list = sentence.split()
print(f"Words: {word_list}")

# Extract unique words
unique = set(word_list)
print(f"Unique: {unique}")

# Update the set
unique.update(["and", "calm"])
print(f"Unique: {unique}")

# Remove an item from the set
unique.remove( "calm")
print(f"Unique: {unique}")
