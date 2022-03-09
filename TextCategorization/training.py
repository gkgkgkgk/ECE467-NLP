import os
import nltk
from nltk.tokenize import word_tokenize

class TrainedCorpus:
    def __init__(self, path, outputFile=''):
        self.labelCount = {}
        self.wordCount = {}
        self.articles = {}
        self.fileCount = 0
        self.path = path
        self.outputFile = outputFile
        self.train(self.path, self.outputFile)

    def train(self, labelsFile, outputFile=''):
        labelCount = {}
        wordCount = {}
        articles = {}
        fileCount = 0

        d = os.path.dirname(labelsFile)

        with open(labelsFile, 'r') as labelsFile:
            for line in labelsFile:
                article, label = line.split()
                articleName = d + article[1:]

                if label not in labelCount:
                    labelCount[label] = 1
                    wordCount[label] = {}
                else:
                    labelCount[label] += 1
                
                articles[articleName] = label
                fileCount +=1
        
        for article in articles:
            label = articles[article]

            with open(article, 'r') as articleFile:
                tokenization = set(nltk.word_tokenize(articleFile.read()))

                for word in tokenization:
                    if word.isalpha():
                        if word not in wordCount[label]:
                            wordCount[label][word] = 1
                        else:
                            wordCount[label][word] += 1

        self.labelCount = labelCount
        self.wordCount = wordCount
        self.articles = articles
        self.fileCount = fileCount

        if outputFile == '':
            return

        out = open(outputFile, 'w')
        out.write(str(fileCount) + '\n')
        out.close()

        out = open(outputFile, 'a')
        for label in labelCount:
            out.write("LABEL|" + label + '|' + str(labelCount[label]) + '\n')
        
        for label in labelCount:
            for word in wordCount[label]:
                out.write("WORD|" + word + '|' + label + '|' + str(wordCount[label][word]) + '\n')
            

        out.close()