#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from terrain import make_terrain,draw_terrain
from queue import Queue
def bfs(row,col,wall,S,E):
    m = make_terrain(row,col,wall)
    q = Queue()
    q.put(S)
    m[S[0]][S[1]] = 0
    while not q.empty():
        x,y = q.get()
        neighbor = (x-1,y),(x+1,y),(x,y-1),(x,y+1)
        for i,j in neighbor:
            if m[i][j] == 'o':
                m[i][j] = m[x][y] + 1
                q.put((i,j))
    #以下为构建路径
    path_map = make_terrain(row,col,wall)
    x,y = E[0],E[1]
    path_map[x][y] = 'E'
    while m[x][y] != 0:
        neighbor = (x-1,y),(x+1,y),(x,y-1),(x,y+1)
        for i,j in neighbor:
            v = m[i][j]
            if v !='#' and v < m[x][y]:
                x,y = i,j
                path_map[x][y] = '*'
                break
    else:
        path_map[x][y]='S'
    return path_map


# wall = ((3,3),(4,3),(5,3),(4,6),(5,6))
# S,E  = (3,2),(4,7)
# draw_terrain((bfs(7,7,wall,S,E)))

