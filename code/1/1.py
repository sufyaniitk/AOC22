"""
Solution for AOC Q1
"""

with open('./data/1/1.txt', 'r') as f:
    data = f.read()

ans = max(map(lambda x: sum(map(int, x.split())), data.split('\n\n')))
print(ans)
