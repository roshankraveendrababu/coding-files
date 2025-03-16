'''
initialize the table as it is 
but we need string instead of count

'''
def tabu(x,y):  # stores string in table, hence space extensive
    t=[["" for _ in range(len(y)+1)] for _ in range(len(x)+1)]
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1]==y[j-1]:
                t[i][j]=x[i-1]+t[i-1][j-1]
            else:
                #call two values and store the maximum length value
                if len(t[i-1][j])>len(t[i][j-1]):
                    t[i][j]=t[i-1][j]
                else:
                    t[i][j]=t[i][j-1] 
    return t[len(x)][len(y)]

def tabu_lcs(x,y): # this code is the same as lcs one for table creation
    t=[[0 for _ in range(len(y)+1)] for _ in range(len(x)+1)]
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])

    x_axis,y_axis=len(x),len(y)
    lcs_str=[]
    while x_axis>0 and y_axis>0:
        if x[x_axis-1]==y[y_axis-1]:
            lcs_str.append(x[x_axis-1])
            x_axis-=1
            y_axis-=1
        else:
            if t[x_axis-1][y_axis]>t[x_axis][y_axis-1]:
                x_axis-=1
            else:
                y_axis-=1
    return "".join(reversed(lcs_str))

print(tabu_lcs("abac","cab"))