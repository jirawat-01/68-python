inchar = input("Input one character: ")
if inchar >= 'A' and inchar <= 'Z':
    print("you in put upper case Letter" , inchar)
elif inchar >= 'a' and inchar <= 'z':
    print("you in put Lower case Letter" , inchar)
elif inchar >= '0' and inchar <= '9':
    print("you in put Number " , inchar)
else :
    print("It`s not a letter or number " , inchar)