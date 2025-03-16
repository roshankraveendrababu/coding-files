#comma seperated values are stored as tuple in default
packed=1,"roshan","first"
print(packed)

#tuples can be unpacked without specific indexing like in the case of list
# a,b,c=packed
# print(a)

#unpacking using * operator
#* operator is used to unpack the elements of the tuples from the first 1ndex to the last by default or till the index where the 
#initialization starts from the end .
first,*middle=packed
print(middle)


#nested tuples work the same way as nested list

#iterating over a tuple is also similar to iterating over a list

