def unique_string(string):
    unique = ""

    for x in range(len(string)):
        if string[x] in unique:
            print("Not Unique")
            return
        elif string[x] not in unique:
            unique += string[x]

    print("Unique")
