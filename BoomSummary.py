from PyDictionary import PyDictionary as dict
from nltk.stem.lancaster import LancasterStemmer
st = LancasterStemmer()

class Word:
  def __init__(self, word, count):
    self.word = word
    self.type = self.defineType()
    self.count = count
  def isNoun(self):
      for x in self.type:
          if(x == 'Noun'):
              return True
      return False
  def defineType(self):
      full = dict.meaning(self.word)
      x = list(full)
      return x


#Constants
punctuation = (',','.','/',';',':')

def removePunctuation(word, punctuation):
    for x in punctuation:
        if(word[len(word)-1] == x):
            word = word[0:len(word)-1]
    return word
def max(words):
    top = 0
    output = ""
    for x in words:
        if(x.count > top):
            top = x.count
            output = x
    return output
def position(words, word):
    i = 0
    output = 0
    found = False
    for x in words:
        if(x.word == word):
            found = True
            output = i
        i+=1
    if(found == False):
        output = -1
    return output
words = []
paragraph = input("Enter the text to be summarized: ")
tokens = paragraph.split()

for x in tokens:
    x = x.strip()
    x = removePunctuation(x, punctuation)
    x = st.stem(x)
    if(position(words, x) > -1):
        words[position(words,x)].count += 1
    else:
        words.append(Word(x,1))
output = max(words)
print(output.word)


