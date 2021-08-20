def getlist(dictionary):
    global list_format
    base_list = []
    for i in dictionary.keys():
        base_list.append(i)
        list_format = ", ".join(base_list)

    return list_format
