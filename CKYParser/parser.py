from nltk.tokenize import word_tokenize
from nltk import download as n_download
n_download("punkt", quiet=True)

class Cell:
    def __init__(self, rules, left, right):
        self.rules = rules
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.rules)

class Grammer:
    def __init__(self):
        self.terminals = {}
        self.nonTerminals = {}
        self.table = None

    def buildGrammer(self, cfgPath):
        cfg = open(cfgPath, "r")
        grammer = {}
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
    
    def compareCells(self, cell1, cell2):
        rules = []
        if cell1.rules != [] and cell2.rules != []:
            for rule1 in cell1.rules:
                for rule2 in cell2.rules:
                    nonTerminal = rule1 + " " + rule2
                    if nonTerminal in self.nonTerminals:
                        rules.extend(self.nonTerminals[nonTerminal])

        return rules

    def printTable(self, table):
        for row in table:
            for cell in row:
                print(cell, end=" ")
            print()

    def parse(self, sentence):
        tokenization = word_tokenize(sentence)
        wc = len(tokenization)

        if wc == 0:
            return False

        self.table = [[Cell([], None, None) for i in range(wc)] for j in range(wc)]

        # populate diagonals
        for i, word in enumerate(tokenization):
            if word in self.terminals:
                rules = self.terminals[word]
            else:
                rules = []

            self.table[i][i] = (Cell(rules, None, None))

        for diag in range(1, wc):
            for x in range(0, wc - diag): # x is row, y is column
                y = x + diag
                rules = []

                for k in range(x, x + diag):
                    cell1 = self.table[x][k]
                    cell2 = self.table[k + 1][y]
                    rules.extend(self.compareCells(cell1, cell2))
                
                self.table[x][y] = Cell(rules, cell1, cell2)
        
        if self.table[0][wc - 1].rules != []:
            return True
        else:
            return False

    def printParses(self, printTree=False):
        if self.table == None:
            print("ERROR: Table not built yet. Please parse a sentence first in order to print it.")
            return

cfgPath = input("Enter the name of the CFG file: ")

g = Grammer()
print("Loading grammer...")
g.buildGrammer(cfgPath)
print("Do you want textual parse trees to be displayed (y/n)?")
parseTree = True if input() == "y" else False

while(1):
    print("Enter a sentence to parse: ")
    sentence = input()

    if sentence == "quit":
        break

    valid = g.parse(sentence)
    print("VALID" if valid else "INVALID", "SENTENCE")
    g.printParses()