with open('sometext.txt') as text:
    for line in text:
        word = line.split() 
        specifics = dict((word,word.count(word)) for word in set (word))

print(specifics)