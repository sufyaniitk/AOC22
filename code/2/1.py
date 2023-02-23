with open('../../data/2/2.txt', 'r') as f:
    games = f.read()

games = games.strip().rsplit('\n')

w = ['A Y', 'B Z', 'C X']
d = ['A X', 'B Y', 'C Z']
points = {'X': 1, 'Y': 2, 'Z': 3}

score = 0
for game in games:
    score += points[game[2]]
    if game in w: score += 6
    elif game in d: score += 3

print(score)
