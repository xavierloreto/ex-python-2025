def main():
    plate = input("Plate: ").upper()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(plate):

    if not is_valid_length(plate):
        return False

    if not is_valid_alpha(plate):
        return False

    if not is_valid_alphanumeric(plate):
        return False

    if not numbers_only_at_end(plate):
        return False

    return True

def is_valid_length(plate):
    length = len(plate)
    return length <= 6 and length >= 2

def is_valid_alpha(plate):
    return plate[:2].isalpha()

def is_valid_alphanumeric(plate):
    return plate.isalnum()

def numbers_only_at_end(plate):
    has_number = False
    for char in plate:
        if char.isdigit():
            if not has_number:
                if char == '0':
                    return False
                has_number = True
        elif has_number:
            return False

    return True


main()

