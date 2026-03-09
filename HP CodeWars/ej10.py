dungeon = input()
actions=[]
mapa=[ch for ch in dungeon]
for x in mapa:
    if x=='_':
        actions.append('w')
    elif x=='G':
        actions.append('f')
        actions.append('w')
    elif x=='E':
        actions.append('ff')
        actions.append('w')
    elif x=='S':
        actions.append('fff')
        actions.append('w')
    elif x=='T':
        actions.append('ffff')
        actions.append('w')
print(''.join(actions))
