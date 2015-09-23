"""
This function runs the imposter method

"""
import sims
import mechanize
from bs4 import BeautifulSoup
from nltk.tokenize import RegexpTokenizer
from collections import Counter
import numpy as np
tokenizer = RegexpTokenizer(r'[a-zA-Z]+')


def score(A,B,Bi):
    return A
     
def imposterMethod(k,rate,numberSampled,X,Y,xImposters,yImposters,sim):
    for _ in xrange(k):
        #subset half the features at random
        
        sigma = np.mean(score(X,Y,yImposters),score(Y,X,xImposters))
        return(sigma)

def cleanLinks(links):
    clean = []
    for link in links:
        try:
            start = link.index("http")
            end = link.index("&")
            clean.append(link[start:end])
        except:
            None
    return(clean)
    
def generateQueries(array):
    return array

def readLink(link,br):
    """given link and a browser instance read a link and return it as text"""
    if link[-3:] == 'pdf':
        return None
    try:
        br.open(link)
        r = br.response().get_data()
        soup = BeautifulSoup(r)
        text = " ".join([p.get_text() for p in soup.find_all("p")])
        return(text)
    except:
        return None

def searchGoogle(searchTerms):
    """ Given a list of search terms, concatenates and returns a list of links"""
    br = mechanize.Browser()
    br.set_handle_robots(False)
    br.addheaders = [('User-agent',
                 'Mozilla/5.0')]
    br.open("https://www.google.com/search?q=" + "+".join(searchTerms) + "&num=100")
    r = br.response().get_data()
    soup = BeautifulSoup(r)
    links  = [a.next.attrs["href"] for a in soup.find_all(None,class_="r")]
    links = cleanLinks(links)
    texts = []
    for link in links:
        text = readLink(link,br)
        if text is None:
            next
        try:
            tokens = tokenizer.tokenize(text)
            if len(tokens) < 500:
                next
            else:
                texts.append(" ".join(tokens))
                if len([text for text in texts if text is not None]) == 10:
                    break
        except:
            next
    print len(texts)
    return(texts)
    
def tokenizeText(textLocation):
    text = open(textLocation).read().decode("utf-8").lower()
    tokens = Counter(tokenizer.tokenize(text))
    return(tokens)

def wordList(corpusVocabulary,Min,Max):
    """ Takes a corpus Vocabulary and returns a smaller list satisfying min max frequency
    requirements.  The Min Max can be given as an integer or, if between 0,1 as a frequency
    """
    length = sum(corpusVocabulary.values())
    if type(Min) == float:
        Min = int(Min * length)
    if type(Max) == float:
        Max = int(Max*length)
    array = [word for word in corpusVocabulary.keys() 
                    if Min<=corpusVocabulary[word]<=Max]
    print "These settings give " + str(len(array)) + " possible words out of " +  str(len(corpusVocabulary.keys())) + " unique words in the corpus"
    print "All words occur at least " + str(Min) + " times and at most " + str(Max) 
    return(array)

def generateImposters(n,textLocation,vocabulary):
    """ Takes a textLocation, reads the file, and generates a set of n imposters using google"""
    wordCount = tokenizeText(textLocation)
    refinedWordCount = {word : wordCount[word] for word in wordCount.keys() if word in vocabulary}
    imposters = []
    while len(imposters) < n:
        print "The number of imposters is ", len(imposters)
        query = np.random.choice(refinedWordCount.keys(),size=np.random.choice(xrange(2,6)),replace=False)
        imposters = imposters + (searchGoogle(query))
    return(imposters)