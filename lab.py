def getlist(dict):
    base_list = []
    for i in dict.keys():
        base_list.append(i)
        list_format = ", ".join(base_list)

    return list_format

