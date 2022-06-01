def make_terrain(x,y,obstacle):
    m = []
    m.append(list('#'*(y+2)))
    for _ in range(x):
        m.append(list('#'+'o'*y+'#'))
    m.append(list('#'*(y+2)))
    for ob in obstacle:
        m[ob[0]][ob[1]] = '#'
    return m
def draw_terrain(m):
    print()
    for row in m:
        for grid in row:
            if(grid=='o'):
                print(' ',end=' ')
            else:
                print(grid,end=' ')
        else:
            print()