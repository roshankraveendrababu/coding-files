def count_paths(r,c,n):
    if r==n and c==n:
        return 1
    if r==n:
        return count_paths(r,c+1,n)
    if c==n:
        return count_paths(r+1,c,n)
    if r!=n and c!=n:
        left=count_paths(r,c+1,n)
        down=count_paths(r+1,c,n)
        return left+down
    
print(count_paths(1,1,3))