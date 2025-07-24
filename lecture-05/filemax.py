def find_max(*args):
    if not args:
        return None
    max_balue = args[0]
    for number in args:
        if number > max_balue:
            max_balue = number
    return
result = find_max(3,5,7,2,7,8)
print(f"the maximum value is : {result}")