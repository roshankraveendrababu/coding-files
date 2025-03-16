from collections import OrderedDict
def ordered_dict_codes():
    od=OrderedDict()
    print("original")
    od["a"]=2
    od["b"]=3
    od["c"]=1
    for key,value in od.items():
        print(f"key:{key},value:{value}")
    
    print("after changes")
    od["c"]=9
    od.move_to_end("c",last=False)
    od=OrderedDict(reversed(list(od.items())))
    od.popitem(last=False)
    for key,value in od.items():
        print(f"key:{key},value:{value}")
    print()
    print()

def normal_dictionary():
    normal_dict={}
    print("original normal dictionary")
    normal_dict["a"]=2
    normal_dict["b"]=3
    normal_dict["c"]=1
    for key,value in normal_dict.items():
        print(f"key:{key},value:{value}")
    
    print("after changes to the normal one")
    normal_dict["c"]=9
    for key,value in normal_dict.items():
        print(f"key:{key},value:{value}")

ordered_dict_codes()
normal_dictionary()
