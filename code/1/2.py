"""
Solution for AOC Q1
"""

with open('./data/1/1.txt', 'r') as f:
    data = f.read()

ans = sum(sorted(map(lambda x: sum(map(int, x.split())), data.split('\n\n')))[-3:])
print(ans)
