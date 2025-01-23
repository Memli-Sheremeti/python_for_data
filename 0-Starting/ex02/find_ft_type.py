def all_thing_is_obj(object: any) -> int:
    if object.__class__ == list:
        print("List :", type(object))
    elif object.__class__ == tuple:
        print("Tuple :", type(object))
    elif object.__class__ == set:
        print("Set :", type(object))
    elif object.__class__ == dict:
        print("Dict :", type(object))
    elif object.__class__ == str:
        print(object, "is in the kitchen :", type(object))
    else:
        print("Type not found")
    return 42
