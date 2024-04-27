def flatten(lst):
    """
    returns a 1 list, where are all unpacked list
    >>> flatten([1,[2]])
    [1, 2]
    >>> flatten([1,2,[3,[4,5],6],7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten([])
    []
    >>> flatten([[]])
    []
    """
    resulted_lst=[]
    if not isinstance(lst,list):
        return None
    for elem in lst:
        if type(elem)!=list:
            resulted_lst.append(elem)
        else:
            resulted_lst += flatten(elem)
    return resulted_lst