from training import TrainedCorpus
from testing import *
import nltk
from nltk.tokenize import word_tokenize
import random
import statistics

nltk.download('punkt', quiet=True)

def customTestCorpus1(amount, factorRange, useStopWords):
    results = []
    t = TrainedCorpus("./corpora/corpus1_train.labels")

    r = factorRange[1] - factorRange[0]
    step = round(r / amount, 5)
    factors = []
    for i in range(amount):
        factors.append(factorRange[0] + (i * step))

    for i in range(amount):
        a = factors[i]
        successRate = verify(tester(t, "./corpora/corpus1_test.list", a, useStopWords), "./corpora/corpus1_test.labels")
        results.append({'percentage': successRate, 'a': a})

    # return a with max success rate
    return (results)

def customtest(percentage, amount, factorRange, corpus, useStopWords):
    results = []

    # evenly divide range into amount of tests
    r = factorRange[1] - factorRange[0]
    step = round(r / amount, 5)
    factors = []
    for i in range(amount):
        factors.append(factorRange[0] + (i * step))
    
    for i in range(amount):
        a = factors[i]
        resultsa = []

        for j in range(5):
            print("Starting test " + str(j) + " for a = " + str(factors[i]))
            train = []
            test = []   
            
            with open("./corpora/corpus"+str(corpus)+"_train.labels") as testFiles:
                for testFile in testFiles:
                    if random.random() < percentage:
                        train.append(testFile)
                    else:
                        test.append(testFile)

            out = open("./corpora/train.txt", 'w')
            for line in train:
                out.write(line)
            out.close()

            out = open("./corpora/test.txt", 'w')
            for line in test:
                out.write(line)
            out.close()

            out = open("./corpora/actual.txt", 'w')
            for line in test:
                out.write(line)
            out.close()
            print("Training")
            t = TrainedCorpus("./corpora/train.txt")
            successRate = verify(tester(t, "./corpora/test.txt", a, useStopWords), "./corpora/actual.txt")
            print("Testing")
            resultsa.append(successRate)
            os.remove("./corpora/train.txt")
            os.remove("./corpora/test.txt")
            os.remove("./corpora/actual.txt")

        results.append({'percentage': statistics.mean(resultsa), 'a': a})

    return (results)

# print(customtest(0.85, 25, [0.005, 0.12], 3, True))
print(customTestCorpus1(25, [0.005, 0.12], False))