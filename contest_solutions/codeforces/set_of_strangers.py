# You are given a table of n
#  rows and m
#  columns. Initially, the cell at the i
# -th row and the j
# -th column has color ai,j
# .

# Let's say that two cells are strangers if they don't share a side. Strangers are allowed to touch with corners.

# Let's say that the set of cells is a set of strangers if all pairs of cells in the set are strangers. Sets with no more than one cell are sets of strangers by definition.

# In one step, you can choose any set of strangers such that all cells in it have the same color and paint all of them in some other color. You can choose the resulting color.

# What is the minimum number of steps you need to make the whole table the same color?

def color_cnt(color_pos,grid):
    val=1
    neighbours=[[1,0],[-1,0],[0,1],[0,-1]]
    for dx,dy in color_pos:
        for nx,ny in neighbours:
            new_x,new_y=dx+nx,dy+ny
            if (new_x,new_y) in color_pos:
                val+=1
                return val
    return val


def no_of_iter(n,m,grid):
    color_map={}
    cnt=0
    for i in range(n):
        for j in range(m):
            if grid[i][j] not in color_map:
                color_map[grid[i][j]]=set()
            color_map[grid[i][j]].add((i,j))
    for co_ordinates in color_map.values():
        cnt+=color_cnt(co_ordinates,grid)

    if cnt>len(color_map):
        return cnt-2
    else:
        return cnt-1

if __name__=="__main__":
    t=int(input())
    for _ in range(t):
        n,m=map(int, input().split())
        grid=[]
        for _ in range(n):
            grid.append(list(map(int, input().split())))
        print(no_of_iter(n,m,grid))