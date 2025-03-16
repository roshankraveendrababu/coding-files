def helper(original,curr):
    if not original:
        return [curr]
    return helper(original[1:],curr)+helper(original[1:],curr+[original[0]])

def generate_power_set(original):
    ans=helper(original,[])
    return ans


def for_string(original,curr):
    if original=="":
        return [curr]
    return for_string(original[1:],curr)+ for_string(original[1:],curr+original[0])

print(for_string("abc",""))