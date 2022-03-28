from nltk.tokenize import word_tokenize
from nltk import download as n_download
n_download("punkt")

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
                    print("COMPARIBNG")
                    print(rule1)
                    print(rule2)
                    nonTerminal = rule1 + " " + rule2
                    if nonTerminal in self.nonTerminals:
                        rules.extend(self.nonTerminals[nonTerminal])
        print("FOUND RULES:", end=" ")
        print (rules)
        return rules

    def printTable(self, table):
        for row in table:
            for cell in row:
                print(cell, end=" ")
            print()

    def parse(self, sentence):
        tokenization = word_tokenize(sentence)
        wc = len(tokenization)
        table = [[Cell([], None, None) for i in range(wc)] for j in range(wc)]

        # populate diagonals
        for i, word in enumerate(tokenization):
            rules = self.terminals[word]
            table[i][i] = (Cell(rules, None, None))

        self.printTable(table)

        for diag in range(1, wc):
            print("NEW DIAG")
            for x in range(0, wc - diag): # x is row, y is column
                y = x + diag

                print("NEW CELL AT " +  str(x) + ", " + str(y))
                rules = []
                for k in range(x, x + diag):
                    print("NEW COMPARE: ", table[x][k], " AND ", table[k + 1][y])

                    # print(x, y, k)
                    print("comparing (" + str(x) + ", " + str(k) + ") and (" + str(k + 1) + ", " + str(y) + ")") 
                    cell1 = table[x][k]
                    cell2 = table[k + 1][y]
                    print(cell1, cell2)
                    rules.extend(self.compareCells(cell1, cell2))
                
                table[x][y] = Cell(rules, cell1, cell2)
        self.printTable(table)

    
    
    

cfgPath = input("Enter the name of the CFG file: ")

g = Grammer()
g.buildGrammer(cfgPath)
g.parse("i book the flight through houston")