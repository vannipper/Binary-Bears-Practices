import sys

text = list() # get input from command line
for line in sys.stdin:
    if line != "R0C0":
        text.append(line)
    else:
        break

powers = list() # add all powers of 26 until 300mil to a list
z = 1
powers.append(z)
while (z < 300000000):
    z *= 26
    powers.append(z)

for cell in text: # for each input given
    row = int(cell[1:cell.find('C')]) # prime row # and col #
    col = int(cell[cell.find('C') + 1:])

    tempcol = col # get tempcol to basic form
    charnum = 0
    for i in range(len(powers) - 1):
        if tempcol > powers[i + 1]:
            tempcol -= powers[i + 1]
            charnum = i + 1
    tempcol -= 1 # index, used for accurate base calculations

    output = "" # use base 26 to get character string
    for i in range(charnum, -1, -1):
        charindex = int(tempcol / powers[charnum - 1])
        tempcol -= powers[charnum - 1]*charindex
        output += chr(charindex + 65)

    output += str(row) # add row number to output string
    print(output) # print output string
