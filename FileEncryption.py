infile = open('info_security.txt','r')
outfile = open('encrypted.txt', 'w')

encryption = {'A' : '¡', 'a' : '™', 'B' : '£', 'b' : '¢', 'C' : '∞', 'c' : '§', 'D' : '¶', 'd' : '•', 'E' : 'ª', 'e' : 'º', 'F' : '≠',
'f' : 'œ', 'G' : '∑', 'g' : '®', 'H' : '†', 'h':'¥', 'I':'¨','i': 'ø', 'J' : 'π', 'j' : 'å', 'K' : 'ß', 'k' : '∂', 'L' : 'ƒ', 
'l' : '©', 'M' : '˙', 'm' : '∆', 'N' : '¬', 'n' : '…', 'O' : 'æ', 'o' : '≈', 'P' : 'ç', 'p' : '√', 'Q' : '∫', 'q' : 'µ', 'R' : '≤',
'r' : '≥', 'S' : '÷', 's' : '@', 'T' : '!', 't' : '#', 'U' : '$', 'u' : '%', 'V' : '^', 'v' : '&', 'W' : '*', 'w' : '(', 'X' : ')',
'x' : '+', 'Y' : '-', 'y' : '[', 'Z' : ']', 'z' : '>'}


info = infile.read()

for n,l in encryption.items():
    search = n
    replace = l

    info = info.replace(search,replace)

outfile.write(info)