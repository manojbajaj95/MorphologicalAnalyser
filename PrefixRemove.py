import re, enchant

import nltk
from nltk.stem import SnowballStemmer
from nltk.stem import WordNetLemmatizer
from nltk import word_tokenize

porter = nltk.PorterStemmer();
lancaster = nltk.LancasterStemmer()
wnl = WordNetLemmatizer()
snowball = SnowballStemmer("english")

d = enchant.Dict("en_US")

#predict closest match
#use the word after removing the stem as well as suffix to decide the closest word
def closest(stem,word):
    a = 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'
    for x in d.suggest(stem):
        if (len(x)>len(stem) and x.startswith(stem) and len(x)-len(stem)<3 and len(x)<len(a) and x!=word):
            a = x
    if (a!='zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'):
        return a
    
    
#prefixRemover
#Remove the regular prefixes directly without modification
def prefixR(word):
    regexp = r'^(.*?)(inter|intra|over|sub|in|cent|tri|uni|circum|counter|dis|im|in|pre|re|un|bi|a|mis)?'
    stem,prefix = re.findall(regexp, word)[0]
    stem =word[len(prefix):]
    print ("prefix: "+ prefix)
    print("word: " + stem)
    return stem

#suffixRemove
#Remove the suffix using regular expression
def stemi(word):
    #make a regular expression of all the common prefixes
    regexp = r'^(.*?)(liness|ness|able|ably|ment|ious|tion|ies|ible|ing|ive|ate|ise|ist|ies|ble|ist|ful|erly|ed|es|er|al|ed|s)?$'
    stem, suffix = re.findall(regexp, word)[0]
    #stem is fter cutting the regular expression
    #handling some exceptional cases
    if (suffix=='tion'):
        stem += 'te'
    if (suffix == 'ate'):
        stem += 'e'
    #check if the removed word exists 
    if not (d.check(stem)):
        possiblestem = closest(stem,word)
        # get a closest match to the word
        if not possiblestem :
        	stem = word
        	suffix = ''
        else:
        	stem = possiblestem
    #print ("word: " + stem)
    #print ("suffix: " + suffix)
    #recursively check if more of the suffixes can be removed
    if (suffix!='' and len(stem)>5) :
        return stemi(stem)
    else:
        return stem

#TakeInput
#word = input('Enter a word\n')
#prefixR(word)

raw = input('Enter a series of  words which you wish to stem\n')
a,b,c=0,0,0
#raw = """DENNIS: Listen, strange women lying in ponds distributing swords is no basis for a system of government.  Supreme executive power derives froma mandate from the masses, not from some farcical aquatic ceremony."""
tokens = word_tokenize(raw)
for word in tokens:
    
    print('The word is: '+word)
    stem1 =stemi(word)
    print("Stem by my Stemmer: ",end="")
    print(stem1)
    stem = porter.stem(word)
    if stem==stem1:
        a = a+1
    print ("Stem by Porter: " + stem)
    stem = lancaster.stem(word)
    if stem==stem1:
        b=b+1
    print ("Stem by Lancaster: " + stem)
    stem = snowball.stem(word)
    if (stem1==stem):
        c = c+1
    print ("Stemming by word net lemmatizer: " +stem)
    print('\n --------------------------------------------------------')
    
print ("No of Matches:")
print("With Porter:")
print(a)
print("With Lancaster:")
print(b)
print("With Snow ball Stemmer:")
print(c)
