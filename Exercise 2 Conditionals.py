#if input is integer the output says length cannot be found
def len_str(str):
    if type(str) == int:
        return"integers dont have length."
    elif type(str) == float:
        return"float dont have length."
    else:
        return len(str)
print(len_str(10.0))
