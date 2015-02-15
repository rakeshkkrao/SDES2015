def is_array(var):
    return isinstance(var, (list, tuple))


def each_element_number(lst):
    var_to_return=True
    for each in lst:
        var=isinstance(each, (int, float, long))
        if var==False:
            var_to_return=False
    return(var_to_return)
