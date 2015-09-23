
import os
import sims
from imposter import *

def loadDocs(problemsFolder):
    """ Take a problem folder and return a list of pairs. 
    Each pair is a list of file locations for articles and a file location 
    for an opinion nominally by same author"""
    items  = []
    for path, _ , fnames in os.walk(problemsFolder):
        articles = [path + "/" + i for i in (set(fnames) - {'.DS_Store','opinion.txt'})]
        opinion = path + "/" + 'opinion.txt'
        items.append((articles, opinion))
    return items
        
######### main

#constants
n= 100 #the number of imposters to acquire
k = 10 #number of times to repeat experiment
rate = 0.5 #fraction to throw out
problemsFolder = "/Users/brianlibgober/Box Sync/Summer 2015/Judicial Attribution/Problems/Texts/"
allFiles = loadDocs(problemsFolder) #remember 0 gives junk

### we need to define the limited corpus vocabulary for purposes of generating queries
corpusVocabulary = Counter()
for articles, opinion in allFiles[1:]:
    corpusVocabulary = corpusVocabulary + tokenizeText(opinion)
    for article in articles:
        corpusVocabulary = corpusVocabulary + tokenizeText(article)  

limitedVocab = wordList(corpusVocabulary,5,0.0004)
#generate the set of opinion imposters
opinionImposters = generateImposters(n,opinion,limitedVocab)
#for article in articles:
 #   articleImposters = generateImposters(n,article,limitedVocab)
  #  score = imposterMethod(k,rate,numberSampled,X,Y,xImposters,yImposters,minmax)
   # print score