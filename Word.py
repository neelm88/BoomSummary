from PyDictionary import PyDictionary as dict
#The Word object represents one word and stores:
#   word: the word itself as a string
#   type: the part of speech as a list
#   count: the number of occurances of the word as an int
class Word:
  def __init__(self, word, type, count):
    if(word == None):
        self.word = None
        self.type = None
        self.count = None
    else:
        self.word = word
        self.type = self.defineType()
        self.count = count
  #Returns true if the word is a noun, and false otherwise.
  def isNoun(self):
      for x in self.type:
          if(x == 'Noun'):
              return True
      return False
  #Returns a list of parts of speech associated with the word.
  def defineType(self):
    x = list()
    if(dict.meaning(self.word) != None):
        x = list(dict.meaning(self.word))
    return x