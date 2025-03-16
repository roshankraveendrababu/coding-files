#we need to pass an list in the argument 
# we use the processed and unproccesed method
def count_paths(processed,r,c,n,paths):
    if r==n and c==n:
        paths.append(processed)
    if r==n and c!=n:
        count_paths(processed+"R",r,c+1,n,paths)
    if c==n and r!=n:
        count_paths(processed+"D",r+1,c,n,paths)
    if r!=n and c!=n:
        count_paths(processed+"R",r,c+1,n,paths)
        count_paths(processed+"D",r+1,c,n,paths)

#this is the code when we can move right,down and diagonal

def print_paths_diag(processed, r, c, n, paths):
    # Exclude paths passing through (1, 1)
    if r == 1 and c == 1:
        return
    
    # Base case: reached the bottom-right corner
    if r == n and c == n:
        paths.append(processed)
        return
    
    # Move down
    if r < n:
        print_paths_diag(processed + "D", r + 1, c, n, paths)
    
    # Move right
    if c < n:
        print_paths_diag(processed + "R", r, c + 1, n, paths)
    
    # Move diagonally
    if r < n and c < n:
        print_paths_diag(processed + "d", r + 1, c + 1, n, paths)


    
paths=[]   
print_paths_diag("",0,0,2,paths)
print(paths)