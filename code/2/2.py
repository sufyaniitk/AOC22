with open('data/2/2.txt', 'r') as f:
    data = f.read()
games = data.strip().split('\n')

def result(opp, me):
    if opp == me: return 'Y'
    if opp == 'A':
        if me == 'B': return 'Z'
        else: return 'X'
    if opp == 'B':
        if me == 'C': return 'Z'
        else: return 'X'
    if opp == 'C':
        if me == 'A': return 'Z'
        else: return 'X'


def score_fn(end, me):
    return (ord(end) - ord('X')) * 3 + ord(me) - ord('A') + 1

score = 0
for g in games:
    opp = g[0]
    end = g[2]
    sol = None
    for m in 'ABC':
        if result(opp, m) == end:
            sol = m
            break
    assert sol is not None
    score += score_fn(end, sol)

print(score)
