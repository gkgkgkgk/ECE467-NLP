from training import TrainedCorpus 
import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')

t = TrainedCorpus("./corpora/corpus1_train.labels", "output.txt")

with open("./corpora/corpus1_test.list") as testFiles:
    labelProbs = {}
    
    for testFile in testFiles:
        with open('./corpora' + testFile[1:].strip()) as testFile:
            tokenization = nltk.word_tokenize(testFile.read())

            # for word in tokenization:
                

