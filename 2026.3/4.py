pronouns = {
    'me' : 'Kanye',
    'you' : 'Kanye',
    'she' : 'Kanye',
    'her' : 'Kanye',
    'he' : 'Kanye',
    'him' : 'Kanye',
    'my' : 'Kanye\'s',
    'mine' : 'Kanye\'s',
    'your' : 'Kanye\'s',
    'yours' : 'Kanye\'s',
    'hers' : 'Kanye\'s',
    'his' : 'Kanye\'s'
}

def Kanye(word: str):
    if word.lower() in pronouns:
        return pronouns[word.lower()]
    else:
        return word

for _ in range(int(input())):
    strmap = [c for c in input()]
    buildString = ''
    firstPointerIdx, secondPointerIdx = 0, 0
    
    for c in strmap:
        if not c.isalnum():
            word = ''.join(strmap[firstPointerIdx:secondPointerIdx])
            buildString += Kanye(word) + c
            firstPointerIdx = secondPointerIdx + 1
        secondPointerIdx += 1

    if firstPointerIdx < len(strmap):
        word = ''.join(strmap[firstPointerIdx:])
        buildString += Kanye(word)

    print(buildString)
