from training import TrainedCorpus
from testing import *
import nltk
from nltk.tokenize import word_tokenize
import random
import statistics

nltk.download('punkt', quiet=True)

print("Downloading NLTK data...")

corpus = 0
trainFile = input("Enter training data file: ")

print("Training...")

t = TrainedCorpus(trainFile)

if len(t.labelCount) == 5:
    corpus = 1
elif len(t.labelCount) == 2:
    corpus = 2
elif len(t.labelCount) == 6:
    corpus = 3
else:
    print("Unrecognized corpus detected. Exiting...")
    exit()

print("Successfully trained on corpus " + str(corpus) + ".")

testFile = input("Enter testing data file: ")
test = []

print("Testing...")

if corpus == 1:
    test = tester(t, testFile, 0.097, False)
elif corpus == 2:
    test = tester(t, testFile, 0.0275, True)
elif corpus == 3:
    test = tester(t, testFile, 0.0648, False)

print("Successfully tested on corpus " + str(corpus) + ".")

outputFile = input("Enter output data file: ")

writeToFile(test, outputFile)
print("Results written to " + outputFile + ".")