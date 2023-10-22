#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result = []
    for numb in my_list:
        if numb == search:
            result.append(replace)
        else:
            result.append(numb)
    return result
