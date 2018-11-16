class Word:
  def __init__(self, word, count):
    self.word = word
    self.type = self.defineType()
    self.count = count
  def isNoun(self):
      if(self.type == "noun"):
          return True
      else:
          return False
  def defineType(self):
      return "noun"


#Constants
punctuation = (',','.','/',';',':')



words = []
paragraph = input("Enter the text to be summarized: ")
tokens = paragraph.split()
for x in tokens:
    x = format(x,punctuation)
    if(position(words, x) > -1):
        words[position(words,x)].count += 1
    else:
        words.append(Word(x,1))

def format(word,punctuation):
    word.strip()
    word = removePunctuation(word, punctuation)
    word = removePlural(word)
    return word
def removePunctuation(word, punctuation):
    for x in punctuation:
        if(word[len(word)-1] == x):
            word = word[0:len(word)-1]
    return word

def removePlural(word):
    return word
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
