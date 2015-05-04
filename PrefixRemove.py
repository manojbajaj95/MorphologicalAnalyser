import re, enchant

'''
import nltk
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
import enchant

d = enchant.Dict("en_US")
porter = nltk.PorterStemmer();
lancaster = nltk.LancasterStemmer()
wnl = WordNetLemmatizer()
snowball = SnowballStemmer("english")
'''

d = enchant.Dict("en_US")

def stemi(word):
    regexp = r'^(.*?)(ing|ly|ed|ious|ies|ive|es|s|ment|ise|tion|al|ist)?$'
    stem, suffix = re.findall(regexp, word)[0]
    if not (d.check(stem)):
        print ('Stemming is done wrong. Some suggestions')
        print(d.suggest(stem))
        
    print (stem)
    print (suffix)
    if suffix!='' :
        stemi(stem)

word = input('Enter a word\n')
stemi(word)