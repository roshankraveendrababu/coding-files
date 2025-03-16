# give me all the main methods and definition of dictionary in python using comments
# it stored data in key-value pairs where keys are unique
# keys can be of any type but they should be immutable
# values can be of any type
# keys are case sensitive
# accessing values using keys is gives error if key is not present
# we can use get() method to avoid this error , we can also give default value to get() method in case key is not present
# we can use list of values for an key to store multiple values for each key
# del dict_name[key]- deletes the key - value pair
# dict_name.clear() - clears the dictionary
# dict_name.keys() - returns all the keys in the dictionary
# dict_name.values() - returns all the values in the dictionary
# dict_name.items() - returns all the key-value pairs in the dictionary
# Shallow Copy =  .copy() - copies the dictionary in an different memory location
# normal = assignment on dict copies the reference of the dictionary i.e, if we change the copied dictionary the original dictionary also changes
# we can also use dict() to create a dictionary
# we can use for loop to iterate over the dictionary
# we can have nested dictionaries , where the value of a key is another dictionary
# we can return values in nested dictionary using dict_name[key1][key2]
# we can also use dict_name.get(key1).get(key2) to return the value
# {x:x**2 for x in range(10)} - dictionary comprehension , returns a dictionary with key as x and value as x**2
# {x:x**2 for x in range(10) if x%2==0} - dictionary comprehension with condition , dict value--> for loop --> condition
# merged_dict={**dict1,**dict2} - merging two dictionaries, if there are same keys then the value of the second dictionary is taken , 
# if we want to take the value of the first dictionary then we can use dict2.update(dict1)

list=[1,2,3,4,5,6,7,8,9,10,1,1,2,3]
dict1={}
for val in list:
    if val not in dict1:
        dict1[val]=1
    else:
        dict1[val]+=1
print(dict1)