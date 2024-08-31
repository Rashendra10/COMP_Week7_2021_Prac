def validate_input(number, minimum):
    while number < minimum:
        print(f"Invalid. Must be at least {minimum}. Re-enter: ")
        number = int(input(""))
    return number