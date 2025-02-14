def transform_value(value):
    if hasattr(value, "__mul__") and callable(getattr(value, "__mul__")):
        try:
            return value * value
        except TypeError:
            pass
    if hasattr(value, "__getitem__") and hasattr(value, "__len__"):
        try:
            return value[::-1]
        except TypeError:
            pass
    if isinstance(value, bool):
        return not value
    if isinstance(value, dict):
        if len(set(value.values())) == len(value):
            return {v: k for k, v in value.items()}
    return value

def typeBasedTransformer(**kwargs):
    return {key: transform_value(value) for key, value in kwargs.items()}

