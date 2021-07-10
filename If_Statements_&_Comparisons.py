# If Statements & Comparisons
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))


def max_num(num1, num2, num3):
    if "dog" == "dog" and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))


def max_num(num1, num2, num3):
    if num1 == num2 and num1 >= num3:   # Equal to
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))


def max_num(num1, num2, num3):
    if num1 != num2 and num1 >= num3:  # Not equal to
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))


def max_num(num1, num2, num3):
    if num1 > num2 and num1 >= num3:   # Greater than
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))


def max_num(num1, num2, num3):
    if num1 < num2 and num1 >= num3:  # Lesser than
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))


def max_num(num1, num2, num3):
    if num1 <= num2 and num1 >= num3:  # Lesser than or equal to
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))


def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:  # Greater than or equal to
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


print(max_num(300, 40, 5))
