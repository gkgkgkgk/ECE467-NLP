# CKY Parsing
## Instructions:
This program was written in Python, and developed and tested in Ubuntu and Windows 10. Follow these instructions in order to run the program:
* Install all dependencies by running pip install -r requirements.txt
* Run python3 ./parser.py
* After being prompted with "Enter the name of the CFG file:", type in the path of the grammer file
* If the grammer is valid, you will be prompted with the option to display parse trees
* Finally, type in a sentence to parse
* If the sentence is valid according to the provided grammer, it will output the valid parses.

## Background
This program is able to take a grammer that is in Chomsky Normal Form and then parse sentences based on the provided grammer. The program uses the Cocke–Kasami-Younger algorithm to parse the sentences. Given a sentence, the program can provide every possibility for a sentence parsing, as well as display the parse tree.
