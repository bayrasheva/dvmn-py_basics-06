def has_digit(password):
    return any(symbol.isdigit() for symbol in password)


def has_upper_letters(password):
    return any(symbol.isupper() for symbol in password)


def has_lower_letters(password):
    return any(symbol.islower() for symbol in password)


def has_symbols(password):
    return any(
        not symbol.isdigit() and not symbol.isalpha()
        for symbol in password
    )


def is_long_enough(password):
    return len(password) >= 12


def main():
    password = input("Введите пароль: ")


    checks = [
        len,
        has_digit,
        has_upper_letters,
        has_lower_letters,
        has_symbols
    ]

    score = 0

    for check in checks:
        if check(password):
            score = score + 2

    print("Рейтинг пароля:", score)


if __name__ == '__main__':
    main()
