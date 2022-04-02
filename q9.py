import random

games = [
    ['Metal Gear Solid'], 
    ['Driver'], 
    ['Crash Bandicoot'], 
    ['Warped'], 
    ['Tekken 3'], 
    ['Cortex Strikes Back'],
    ['Final Fantasy VIII'],
    ['Gran Turismo 2'],
    ['Final Fantasy VII'],
    ['Gran Turismo']
]

chooseGames = []
gamesEquals = False

for i in range(35):
    chooseGames.append(random.randint(0, 9))
    
for i in chooseGames:
    for n in range(10):
        if i == n:
            games[n].append(i)
print(games)

favoriteGame = len(games[0])
nameGame = games[0][0]

for i in range(10):
    if favoriteGame > len(games[i]):
        nameGame = nameGame
        favoriteGame = favoriteGame
        gamesEquals = False
    else:
        if favoriteGame == len(games[i]) and i != 0:
            gamesEquals = True
        else:
            nameGame = games[i][0]
            favoriteGame = len(games[i])

if gamesEquals:
    print('A turma não escolheu uma favorito')
else:
    print('O game escolhido pela turma foi', nameGame)