from Word import Word
class WordSet:
    def __init__(self):
        self.elements = []

    def moveToFront(elements, word):
        found = False
        for x in elements:
            if(x.word == word.word and not found):
                found = True
                elements.remove(word)
                elements.insert(0,word)
    def showWord(elements, str):
        found = False
        output = Word(None,None,None)
        for x in elements:
            if(x.word == str and not found):
                output = x
                found = True
        return output
    def add(self, word):
        self.elements.append(word)
    def remove(self, word):
        WordSet.moveToFront(self.elements, word)
        return self.pop(0)
    def contains(self, str):
        found = False
        for x in self.elements:
            if (x.word == str and not found):
                found = True
        return found
    def removeAny(self):
        return self.elements.pop(0)
    def size(self):
        return len(self.elements)

    # Returns the Word Objecf from Word_List that has the highest count.
    #   Word_List: The list which stores Word Objects.
    def max(self):
        top = 0
        output = ""
        for x in self.elements:
            if (x.count > top):
                top = x.count
                output = x
        return output
    def increment(self,str):
        WordSet.moveToFront(self.elements, WordSet.showWord(self.elements,str))
        temp = self.elements.pop(0)
        temp.count += 1
        self.elements.append(temp)
