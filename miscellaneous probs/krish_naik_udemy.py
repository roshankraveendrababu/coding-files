lst=[x for x in range(21)]
ans=lst[1:]
print(ans[0])
print(ans[-1])
print(ans[len(ans)//2])
print(ans[:5])
print(ans[len(ans)-5:])
print(ans[5:15])
lst=[x for x in ans if x%2==0]
print(lst)

grid=[][]
for i in range(3):
    for j in range(3):
        grid[i][j]=(i,j)
print(grid[1][2])