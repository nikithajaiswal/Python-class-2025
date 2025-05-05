if __name__ == '__main__':
    s = input()

    # Check for alphanumeric characters
    has_alnum = False
    for c in s:
        if c.isalnum():
            has_alnum = True
            break
    print(has_alnum)

    # Check for alphabetical characters
    has_alpha = False
    for c in s:
        if c.isalpha():
            has_alpha = True
            break
    print(has_alpha)

    # Check for digits
    has_digit = False
    for c in s:
        if c.isdigit():
            has_digit = True
            break
    print(has_digit)

    # Check for lowercase characters
    has_lower = False
    for c in s:
        if c.islower():
            has_lower = True
            break
    print(has_lower)

    # Check for uppercase characters
    has_upper = False
    for c in s:
        if c.isupper():
            has_upper = True
            break
    print(has_upper)

