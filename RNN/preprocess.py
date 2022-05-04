rawText = open("starwars.txt", 'rb').read().decode('utf-8')
newText = []
chars = [' ', '-']


for i in range(len(rawText)):
    if rawText[i] == '\n' and i > 0:
        if rawText[i-1] in chars:
            newText.append('')
        else:
            newText.append(rawText[i])
    else:
        newText.append(rawText[i])

rawText = rawText.split("\n")

lineText = []
j = 0
line = "|LINE| "

for i in range(len(rawText)):
    if rawText[i] == '':
        lineText.append(line)
        line = "|LINE| "
    else:
        if rawText[i].isupper() and rawText[i + 1] != '':
            if line == "|LINE| ":
                line += "|DIALOGUE|: "
            line += rawText[i] + ": "
        elif rawText[i].isupper():
            if line == "|LINE| ":
                line += "|SETTING|: "
            line += rawText[i]
        else:
            if line == "|LINE| ":
                line += "|EXPOSITION|: "
            line += rawText[i]

# write lineText to file
with open("starwarsnew.txt", "w") as f:
    for line in lineText:
        f.write(line + "\n")
