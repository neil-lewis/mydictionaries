codes = {'A' : '%', 'a' : '9', 'B' : '@', 'b' : '8', 'C' : '#', 'c' : '7', 'D' : '$', 'd' : '6', 'E' : '!', 'e' : '5', 'F' : '~', 'f' : '4',
'G' : '`', 'g' : '3', 'H' : '^', 'h':'2', 'I':'&','i': '1', 'J' : '*', 'j' : '0', 'K' : '(', 'k' : '™', 'L' : ')', 'l' : '£', 'M' : '-', 'm' : '_'
, 'N' : '¢', 'n' : '∞', 'O' : '§', 'o' : '¶', 'P' : '•', 'p' : 'ª', 'Q' : 'º', 'q' : '≠', 'R' : 'œ', 'r' : '∑', 'S' : '®', 's' : '†',
'T' : '¥', 't' : '¨', 'U' : 'π', 'u' : 'ø', 'V' : 'å', 'v' : 'ß', 'W' : '∂', 'w' : 'ƒ', 'X' : '©', 'x' : '˙', 'Y' : '∆', 'y' : '˚',
'Z' : 'ç', 'z' : '√'}

infile = open('info_security.txt','r')
outfile = open('encrypted.txt', 'w')


data=infile.read()

for k,v in codes.items():
    search=k
    replace = v

    data=data.replace(search,replace)

outfile.write(data)