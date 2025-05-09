from string_checker import StringChecker

def main():
    s = input("Enter a string: ")
    checker = StringChecker(s)

    print(checker.has_alnum())
    print(checker.has_alpha())
    print(checker.has_digit())
    print(checker.has_lower())
    print(checker.has_upper())

if __name__ == "__main__":
    main()
