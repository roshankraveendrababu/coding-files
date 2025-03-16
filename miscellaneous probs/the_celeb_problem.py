import random
def find_celeb(matrix):
    top=0
    bottom=len(matrix)-1
    while top<bottom:
        if matrix[top][bottom]==1:
            top+=1
        else: 
            bottom-=1
    for i in range(len(matrix)): 
        if i != top: 
            if matrix[top][i] == 1 or matrix[i][top] == 0: 
                return -1
    return top
if __name__=="__main__":
    matrix=[]
    matrix.append([0,1,1])
    matrix.append([0,1,1])
    matrix.append([0,0,0])
    print(find_celeb(matrix))
            
               
        