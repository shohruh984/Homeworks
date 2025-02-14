def square_number(value):
    return value * value

def reverse_string(value):
    return "".join(reversed(value))

def invert_boolean(value):
    return not value

def reverse_list(value):
    return list(reversed(value))

def reverse_tuple(value):
    return tuple(reversed(value))

def swap_dict(value):
    if len(set(value.values())) == len(value):
        return {v: k for k, v in value.items()}
    return value
  
type_handlers = {
    int: square_number,
    float: square_number,
    str: reverse_string,
    bool: invert_boolean,
    list: reverse_list,
    tuple: reverse_tuple,
    dict: swap_dict
}
def typeBasedTransformer(**kwargs):
    transformed = {}
    for key, value in kwargs.items():
        handler = type_handlers.get(type(value), lambda x: x)
        transformed[key] = handler(value)
    return transformed
  
print(typeBasedTransformer(
    num=4, 
    text="Hello", 
    flag=True, 
    numbers_list=[1, 2, 3], 
    my_tuple=(10, 20, 30), 
    my_dict={"a": 1, "b": 2}, 
    unknown_type={1, 2, 3}
))
