def custom_max(n1: int, n2:int):
    """_summary_

    Args:
        n1 (int): _description_
        n2 (int): _description_

    Returns:
        _type_: _description_
    """
    if (n1 > n2):
        return n1
    elif (n2 > n1):
        return n2
    else:
        raise Exception("Los valores no pueden ser iguales")

print(custom_max(1,2))