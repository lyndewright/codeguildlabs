#version 1 ish/ 2 ish

# request word or phrase from user
word_or_phrase = input("Give me a word or phrase and I'll let you know if it's a Palindrome: ")

# close spaces and make all alphas lower case to create one uniform string
word_or_phrase = word_or_phrase.replace(" ", "").lower()

# eliminate symbols and make all characters alphas
word_or_phrase = ''.join(a for a in word_or_phrase if a.isalnum())

#identify if word or phrase is palindrome by reversing word/phrase and comparing equality
if (word_or_phrase[::1] == word_or_phrase[::-1]):
    print("Yes, it's a Palindrome.")
else:
    print("No, it's not a Palindrome.")
    quit()
