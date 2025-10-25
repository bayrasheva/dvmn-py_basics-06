PASSWORD = input("Введите пароль: ")

len(PASSWORD) >= 12


def has_digit(PASSWORD):
    return any(symbol.isdigit() for symbol in PASSWORD)


def has_upper_letters(PASSWORD):
    return any(symbol.isupper() for symbol in PASSWORD)


def has_lower_letters(PASSWORD):
    return any(symbol.islower() for symbol in PASSWORD)


def has_symbols(PASSWORD):
    return any(
        not symbol.isdigit() and not symbol.isalpha()
        for symbol in PASSWORD
    )


checks = [
    len,
    has_digit,
    has_upper_letters,
    has_lower_letters,
    has_symbols
]

score = 0

for check in checks:
    if check(PASSWORD):
        score = score + 2

print("Рейтинг пароля:", score)
