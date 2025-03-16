def all_permutations(proc,unproc,answer):
    if unproc=="":
        return answer.append(proc)         
    ch=unproc[0]
    for i in range(len(proc)+1):
        new_proc=proc[0:i]+ch+proc[i:]
        all_permutations(new_proc,unproc[1:],answer)

def count_perm(proc,unproc):
    if unproc=="":
        return 1
    count=0
    ch=unproc[0]
    for i in range(len(proc)+1):
        new_proc=proc[0:i]+ch+proc[i:]
        count+=count_perm(new_proc,unproc[1:])
    return count
result=[]    
print(count_perm("","abc"))
#print(result)


