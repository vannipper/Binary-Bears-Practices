word_to_index = {
    'beautiful': 1,
    'delicious': 1,
    'reliable': 1,
    'unusual': 1,
    'big': 2,
    'deep': 2,
    'small': 2,
    'tall': 2,
    'rough': 3,
    'shiny': 3,
    'thin': 3,
    'untidy': 3,
    'oval': 4,
    'round': 4,
    'square': 4,
    'rectangular': 4,
    'elderly': 5,
    'old': 5,
    'young': 5,
    'youthful': 5,
    'blue': 6,
    'green': 6,
    'red': 6,
    'yellow': 6,
    'American': 7,
    'Chilean': 7,
    'Dutch': 7,
    'Japanese': 7,
    'brass': 8,
    'plastic': 8,
    'steel': 8,
    'wooden': 8,
    'four-sided': 9,
    'general-purpose': 9,
    'L-shaped': 9,
    'U-shaped': 9,
    'cleaning': 10,
    'cooking': 10,
    'frying': 10,
    'hammering': 10
}


# adjectives=  {
#         
#     1 : ['beautiful', 'delicious', 'reliable', 'unusual'],
#     2 : ['big', 'deep', 'small', 'tall'],
#     3 : ['rough', 'shiny', 'thin', 'untidy'],
#     4 : ['oval', 'round', 'square', 'rectangular'],
#     5 : ['elderly', 'old', 'young', 'youthful'],
#     6 : ['blue', 'green', 'red', 'yellow'],
#     7 : ['American', 'Chilean', 'Dutch', 'Japanese'],
#     8 : ['brass', 'plastic', 'steel', 'wooden'],
#     9 : ['four-sided', 'general-purpose', 'L-shaped', 'U-shaped'],
#     10 : ['cleaning', 'cooking', 'frying', 'hammering']
# 
#     }
# 
# word_to_index = {word: i for i, words in adjectives.items() for word in words}

for _ in range(int(input())):
    templist = [(word_to_index.get(word, 11), word) for word in input().split()]
    sortedlist = sorted(templist, key=lambda x: x[0])

    if sortedlist != templist:
        print(f'"{" ".join(word for _, word in templist)}" is not correct - should be "{" ".join(word for _, word in sortedlist)}"')
    else:
        print(f'"{" ".join(word for _, word in sortedlist)}" is correct')