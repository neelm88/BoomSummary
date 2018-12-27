from Word import Word
#WordSet is an Object that stores Word Objects.
class WordSet:
    def __init__(self):
        self.elements = []
#
#Class Methods        
#

#Moves the item in elements that is word, and puts it in the front of the list elements.
#   elements: This is the list of Word Objects being manipulated 
#   word: The Word object being searched for.
    def moveToFront(elements, word):
        found = False
        for x in elements:
            if(x.word == word.word and not found):
                found = True
                elements.remove(word)
                elements.insert(0,word)
                               
#Returns, but does not remove the Word Object from elements that is the string str.
#   elements: The list of Word Objects being searched.
#   str: The string that is contained in one of the Word Objects in elements.
    def showWord(elements, word):
        found = False
        output = Word(None,None,None)
        for x in elements:
            if(x.word == word.word and not found):
                output = x
                found = True
        return output
#Increases the count of a Word Object in elements that has the word value of str.    
#   word: The Word Object that is being searched for in self.
#   elements: The list of Word Objects from which one is being incremented.
    def increment(elements,word):
        WordSet.moveToFront(elements, word)
        temp = elements.pop(0)
        temp.count += 1
        elements.append(temp)

#    
#Instance Methods   
#    
        
#Adds the Word Object to self. 
#   word: A Word Object being added to self.
    def add(self, word):
        if(self.contains(word)):
            WordSet.increment(self.elements,word)
        else:
            self.elements.append(word)
        
#Removes and returns the Word Object from self.        
#   word: A Word Object being removed from self.        
    def remove(self, word):
        WordSet.moveToFront(self.elements, word)
        return self.pop(0)
    
#Returns true if the Word Object word is in self, false otherwise.
#   word: The Word Object that is being searched for in self.
    def contains(self, word):
        found = False
        for x in self.elements:
            if (x.word == word.word and not found):
                found = True
        return found
    
#Removes and returns one item from self.
    def removeAny(self):
        return self.elements.pop(0)
    
#Returns the size of self.
    def size(self):
        return len(self.elements)

# Returns the Word Object from self that has the highest count.
    def max(self):
        top = 0
        output = ""
        for x in self.elements:
            if (x.count > top):
                top = x.count
                output = x
        return output

