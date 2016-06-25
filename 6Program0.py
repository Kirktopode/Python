word = raw_input("Give me a word to reverse, for I am the reversal genie!")
wordlen = len(word)
x = 1
for char in word:
    print str(word[wordlen - x])
    x = x + 1
