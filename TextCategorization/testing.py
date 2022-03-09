from doctest import testfile
from training import TrainedCorpus 
import nltk
from nltk.tokenize import word_tokenize
import math
import os
from nltk.corpus import stopwords

nltk.download('stopwords', quiet=True)
stopwords = set(stopwords.words('english'))

def tester(t, path, a, useStopWords=True):
    guesses = {}
    
    with open(path) as testFiles:    
        for testFile in testFiles:
            labelProbs = {}
            fileName = testFile.split()[0]

            with open(os.path.dirname(path) + testFile[1:].split()[0].strip()) as testFile:
                tokenization = nltk.word_tokenize(testFile.read())

                for label in t.wordCount:
                    labelCount = t.labelCount[label]
                    labelProbs[label] = math.log(labelCount / t.fileCount)
                    k = len(t.wordCount)

                    for word in tokenization:
                        if word.isalpha() and (useStopWords or word not in stopwords):
                            count = 0

                            if word in t.wordCount[label]:
                                count = t.wordCount[label][word]

                            labelProbs[label] += math.log((count + a)/(labelCount + (a*k)))
                            
            guesses[fileName] = max(labelProbs, key=labelProbs.get)


    return guesses

def verify(guesses, path):
    right = 0

    with open(path) as testFiles:
            for testFile in testFiles:
                label = testFile.split()[1]
                filename = os.path.basename(testFile.split()[0])
                if label == guesses[filename]:
                    right += 1

    return (right / len(guesses))

def writeToFile(guesses, path):
    with open(path, 'w') as out:
        for filename in guesses:
            out.write(filename + " " + guesses[filename] + "\n")

# https://towardsdatascience.com/laplace-smoothing-in-na%C3%AFve-bayes-algorithm-9c237a8bdece