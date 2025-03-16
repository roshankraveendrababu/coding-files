def transpose(matrix):
    transposed=list(zip(*matrix))
    return transposed

if __name__=="__main__":
    matrix=[[1,2,3],[4,5,6],[7,8,9]]
    print(transpose(matrix))