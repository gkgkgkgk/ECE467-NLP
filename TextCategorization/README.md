# Text Categorization with Naive Bayes
## Instructions:
This program was written in Python, and developed and tested in Ubuntu and Windows 10. Follow these instructions in order to run the program:
* Install all dependencies by running pip install -r requirements.txt
* Run python3 ./main.py
* After being prompted with "Enter training data file:", type in the path of the training file
* If the model successfully trains, the user will be prompted with "Enter testing data file:"
* Finally, if the file was successfully tested, the user can input the path to the desired output file

## Background
This program uses Naive Bayes as its machine learning method. NLTK was used to tokenize each article. In order to improve performance, many different techniques were used for each corpus in order to maximize the accuracy of the model. The following features were tested:
* Smoothing: Laplace smoothing was used in order to account for words that appear in the test set but not in the training set. The alpha parameter for smoothing was found for each corpus by testing a range of alphas on multiple unique datasets, and finding which one performed the best.
* Stop Words: For some of the corpora, it was advantageous to not consider stop words in the articles. The NLTK stop words dictionary was used in order to determine which words should be excluded.
* Part of Speech Tagging: Using the POS Tagger from NLTK, each word / tag combination was considered as a unique token. For example: bowl as a noun (the one used for cereal) would be considered a different token than bowl as a verb (the sport with bowling balls and pins).

## Testing the Features
### Corpus 1
The first data set has a known test and training set. A wide range of smoothing parameters were tested, and each alpha was tested under each of the following conditions: including stop words / no POS tagging, excluding stop words / no POS tagging, including stop words / yes POS tagging, excluding stop words / yes POS tagging. The following graph was produced:

The best option here was to use a smoothing factor of 0.097, without stop words or POS tagging. This yielded an accuracy of 90.7%.

### Corpus 2
This data set was unknown, so a random test set was generated based on the training set. Approximately 15% of the original training set was used as a test set for the other 85% which was used for training. Tests ran for thirty different alphas ranging between 0.005 to 1.2, and for each alpha, ten different data sets were created and tested, from which the average was used to represent that alpha. After running some tests on corpus 2, the following graph was produced:

The numbers seemed to be all over the place, but the best result was 84.39% accuracy with POS tagging and including stop words. However, there was a close runner up at 84.28% accuracy which included stop words and not POS tagging. I chose the second option, because the average score for stop words / no POS tagging was higher than the stop words / POS tagging test by about 2%. Because I don’t have the exact dataset, I chose the option that on average was better, despite its maximum accuracy being the second highest.

### Corpus 3
Finally, for corpus 3, the following graph was produced:

The maximum accuracy, whose group also had the highest average accuracy, was the test that excluded stop words and POS tagging, which yielded an average of 89.2% and a maximum of 90.4%.

## Conclusion
After running all of these tests, I decided on the following parameters for each corpus:

1: a = 0.097, exclude stop words

2: a = 0.0275, include stop words

3: a = 0.1108, exclude stop words

While testing on these specific training sets, it didn’t seem that POS tagging was much of a help. Another way to implement POS tagging is to only allow certain types of words in the model, or maybe weigh different types of words differently (nouns may be weighted differently than adjectives or prepositions). Additionally, the results may have been further improved by implementing a different type of smoothing.

### References
* https://towardsdatascience.com/laplace-smoothing-in-na%C3%AFve-bayes-algorithm-9c237a8bdece
