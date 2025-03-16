
def lcm_cnt(a,b):
    product=a*b
    if a<b:
        a,b=b,a
    while b:
        a,b=b,a%b
    lcm=product//a
    return lcm


    

def plane_takeoff_cnt(N,p,q,r):
    total=0
    total+=((N//p)+(N//q)+(N//r))
    lcm_total_cnts=(N//lcm_cnt(p,q))+(N//lcm_cnt(q,r))+(N//lcm_cnt(r,p))
    triple_overlap=N//lcm_cnt(lcm_cnt(p,q),r)
    ans=total-(2*lcm_total_cnts)+(3*triple_overlap)
    return ans


# Test case
print(plane_takeoff_cnt(43441, 80, 50, 41))  # Expected output: 3670


