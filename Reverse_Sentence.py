def reverseSentence(sentence):
  # parsing first
  l = list()
  s = ""

  for i in sentence:
      if(i == " "):
          l.append(s)
          l.append(i)
          s = ""
      else:
          s+=i

  l.append(s)
  print(l)
  s = ""
  size = len(l)

  for j in range(size):
      s+=l[size-j-1]

  return s


input_sent = "This is the sentence"
print(reverseSentence(input_sent))

line = input('Type a sentence: ')
returnedline = reverseSentence(line)
print(returnedline)
