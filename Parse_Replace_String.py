def parseWords(sentence):
    l = list()
    s = ''
    for i in sentence:
        if(i == ' '):
            l.append(s)
            s = ''
        elif(i == '.' or i == ',' or i == '!' or i == "''" or i == '-'):
            l.append(s)
            l.append(i)
            s = ''
        else:
            s += str(i)
    l.append(s)
    return l

def replaceWord(a,b,sent): # replacing a with b in l
    s = ''
    l = parseWords(sent)
    print(l)
    for j in l:
        if(j == a):
            j = b
        # if(j == '.' or j == ',' or j == '!' or j == "''" or j == '-'):
            # s += ' '
        s += str(j)
        s += ' '
        # print(s)
    return s

# ------------ tests ------------- #

line = input('Type a sentence: ')
a = input('Replace: ')
b = input('with: ')
# line = "Google Steve Jobs"
# a = "Google"
# b = "Gennison"

# line = "Google   Steve  Jobs"
# a = "Google"
# b = "Gennison"

returnedline = replaceWord(a,b,line)
print(returnedline)
