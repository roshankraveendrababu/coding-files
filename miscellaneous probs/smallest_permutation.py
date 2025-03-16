def smallest_permutation(num):
    copy=num
    nod=0
    while copy:
        nod+=1
        copy//=10
    nod_in_main=nod
    is_not_complete=True
    while(is_not_complete):
        power=1
        result=0
        i=1
        copy=num
        while copy:
            digit=copy%10
            if digit==i:
                result=result+digit*power
                power*=10
            copy//=10
        i+=1
        if i==10:
            is_not_complete=False
    copy_result=result
    nod_in_nonzero_main=0
    while copy_result:
        nod_in_nonzero_main+=1
        copy_result//=10
    number_of_zeroes=nod_in_main-nod_in_nonzero_main
    first_element=(result//10**(nod_in_nonzero_main-1))*10**number_of_zeroes
    end_number=first_element*(10**nod_in_nonzero_main-1)+result%10**(nod_in_nonzero_main-1)
    print(end_number)

smallest_permutation(105096)


