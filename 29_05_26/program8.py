def userdefinelist():
    user_Define_list = list()
    while True:
        element = int(input("Enter the element (-1 for exit) : "))
        if element<0:
            break
        else:
            user_Define_list.append(element)
    return user_Define_list

