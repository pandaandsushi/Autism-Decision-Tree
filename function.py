def convert_bool(input_str):
    if input_str.lower() == "y":
        return 1
    elif input_str.lower() == "n":
        return 0
    else:
        print("Ups, input salah, coba lagi.\n")
        return False

def getinput(question):
    not_stop = True
    while not_stop:
        user_input = input(question + " (y/n): ")
        result = convert_bool(user_input)
        if result is not False:
            not_stop = False
    return result