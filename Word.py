from PyDictionary import PyDictionary as dict
from nltk.corpus import wordnet as wn
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
      return self.type[0] == "noun"
#Returns a list of parts of speech associated with the word.
  def defineType(self):
    x = []
    synsets = wn.synsets(self.word, wn.NOUN)
    if(len(synsets) > 0):
        x.append("noun")

    synsets = wn.synsets(self.word, wn.ADJ)
    if(len(synsets) > 0):
        x.append("adjective")

    synsets = wn.synsets(self.word, wn.VERB)
    if(len(synsets) > 0):
        x.append("verb")

    synsets = wn.synsets(self.word, wn.ADV)
    if(len(synsets) > 0):
        x.append("adverb")
    return x