from PyDictionary import PyDictionary as dict
from nltk.stem.lancaster import LancasterStemmer
import sqlite3 as sql
from Word import Word
from WordSet import WordSet

#Constants

#A tuple of chars of punctuation symbols
punctuation = (',','.','/',';',':','—')

#Methods

#Checks if the parameter word is in the database: UselessWords.db.
#Returns true if the word is useless, false otherwise.
#   word: The word being checked. String.
#   cur: The cursor used to access the database
def useless(cur, word):
    prompt = "SELECT words FROM UselessWords WHERE words = '" + word + "'"
    cur.execute(prompt)
    x = cur.fetchone()
    if(x == None):
        return False
    else:
        return True
#If there is punctuation at the end of the word, it is removed and the word is returned.
#   word: The string in which the word being modified is stored.
#   punctuation: Tuple containing punctuation that is to be removed.
def removePunctuation(word, punctuation):
    for x in punctuation:
        if(word[len(word)-1] == x):
            word = word[0:len(word)-1]
    return word

#Main

#st = LancasterStemmer()
con = sql.connect("UselessWords.db")
cur = con.cursor()
#Word_List stores words from the input parapgraph.
Word_List = WordSet()
paragraph = input("Enter the text to be summarized: ")
#tokens: list of words in the input parargraph.
tokens = paragraph.split()
#Removes formatting from each word then adds it to Word_List.
for item in tokens:
    item = item.strip()
    item = removePunctuation(item, punctuation)
    #x = st.stem(x)
    #checks if the item is already in the Word_List.
    if(Word_List.contains(item)):
        Word_List.increment(item)
    #Checks if the word is in the database
    elif(not useless(cur, item)):
        Word_List.add(Word(item, None, 1))
#output stores the Word Object with the highest count
output = Word_List.max()
print(output.word)
con.close()


