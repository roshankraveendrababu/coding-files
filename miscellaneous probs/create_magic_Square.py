def create_magic_square(dim, start_value):
    if dim%2==0:
        print("enter an odd value for dimension  you clown!!!")
        return
    mid_col=(dim//2)
    row=0
    col=mid_col
    matrix=[[0 for i in range(dim)]for _ in range(dim)]
    matrix[row][col]=start_value
    for num in range(start_value+1,start_value+(dim*dim)):
        next_row=(row-1+dim)%dim
        next_col=(col+1)%dim
        if matrix[next_row][next_col]!=0:
            next_row=(row+1)%dim
        row=next_row
        col=next_col
        matrix[row][col]=num
    for row in range(dim):
        for col in range(dim):
            print(matrix[row][col],end=" ")
        print()

create_magic_square(5,9)

# the same code in c language "https://onlinegdb.com/SDfrn0Dt5"

