with open('sometext.txt') as text:
    for line in text:
        words = line.split() 
        uniquewords = dict((word,words.count(word)) for word in set (words))

print(uniquewords)