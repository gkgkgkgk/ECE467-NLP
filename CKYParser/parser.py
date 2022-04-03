from nltk.tokenize import word_tokenize
from nltk import download as n_download
n_download("punkt", quiet=True)

class Rule:
    def __init__(self, rule, left, right):
        self.rule = rule
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.rule)

class Grammar:
    def __init__(self):
        self.terminals = {}
        self.nonTerminals = {}
        self.table = None

    def buildGrammar(self, cfgPath):
        cfg = open(cfgPath, "r")

        for line in cfg:
            line = line.rstrip().split(" ")
            token = line[0]

            if len(line) == 3:
                word = line[2]
                if word not in self.terminals:
                    self.terminals[word] = [token]
                else:
                    self.terminals[word].append(token)
            elif len(line) == 4:
                word = line[2] + " " + line[3]
                if word not in self.nonTerminals:
                    self.nonTerminals[word] = [token]
                else:
                    self.nonTerminals[word].append(token)
    
    def compareCells(self, rules1, rules2):
        rules = []
        if rules1 != [] and rules2 != []:
            for rule1 in rules1:
                for rule2 in rules2:
                    nonTerminal = rule1.rule + " " + rule2.rule
                    if nonTerminal in self.nonTerminals:
                        for rule in self.nonTerminals[nonTerminal]:
                            rules.append(Rule(rule, rule1, rule2))

        return rules

    def printTable(self, table):
        for row in table:
            for cell in row:
                for rule in cell:
                    print(rule, end=" ")
            print()

    def parse(self, sentence):
        tokenization = word_tokenize(sentence)
        wc = len(tokenization)

        if wc == 0:
            return False

        self.table = [[[] for i in range(wc)] for j in range(wc)]

        # populate diagonals
        for i, word in enumerate(tokenization):
            if word in self.terminals:
                rules = self.terminals[word]
                for rule in rules:
                    self.table[i][i].append(Rule(rule, word, word))

        for diag in range(1, wc):
            for x in range(0, wc - diag): # x is row, y is column
                y = x + diag
                rules = []

                for k in range(x, x + diag):
                    rules1 = self.table[x][k]
                    rules2 = self.table[k + 1][y]                    
                    rules.extend(self.compareCells(rules1, rules2))
                
                self.table[x][y].extend(rules)
        
        if self.table[0][wc - 1] != []:
            return True
        else:
            return False

    # recursion is right- double check that the left and right rules are correct...
    def parsePath(self, rule):
        if str(rule).islower():
            return rule

        left = self.parsePath(rule.left)
        right = self.parsePath(rule.right)

        if left == right:
            return '[' + rule.rule + ' ' + left + ']'
        else:
            return '[' + rule.rule + ' ' + self.parsePath(rule.left) + ' ' + self.parsePath(rule.right) + ']'
        
    def printParses(self, printTree, i = 1):
        tokenization = word_tokenize(sentence)

        if self.table == None:
            print("ERROR: Table not built yet. Please parse a sentence first in order to print it.")
            return

        for i, rule in enumerate(self.table[0][len(self.table) - 1]):
            if self.table[0][len(self.table) - 1][i].rule == "S":
                print("Valid parse #" + str(i + 1) + ":")
                print(self.parsePath(self.table[0][len(self.table) - 1][i]))

        

cfgPath = input("Enter the name of the CFG file: ")

g = Grammar()
print("Loading grammar...")
g.buildGrammar(cfgPath)
print("Do you want textual parse trees to be displayed (y/n)?")
parseTree = True if input() == "y" else False

while(1):
    print("\nEnter a sentence to parse: ")
    sentence = input()

    if sentence == "quit":
        break

    valid = g.parse(sentence)
    print("VALID" if valid else "INVALID", "SENTENCE")
    g.printParses(sentence, parseTree)