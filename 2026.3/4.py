pronouns = [
    'me',
    'you',
    'she',
    'her',
    'he',
    'him',
    'my',
    'mine',
    'your',
    'yours',
    'hers',
    'his'
]

def Kanye(word: str):
    return 'Kanye' if word.lower() in pronouns else word

for _ in range(int(input())):
    print(' '.join([Kanye(word) for word in input().split()]))
