def has_digit(password):
    return any(num.isdigit() for num in password)


def is_very_long(password):
    return len(password) > 12


def has_letters(password):
    return any(letter.isalpha() for letter in password)


def has_upper_letters(password):
    return any(up.isupper() for up in password)


def has_lower_letters(password):
    return any(dw.islower() for dw in password)


def has_symbols(password):
    return any(not symbols.isalpha() and not symbols.isdigit() for symbols in password)


def password_score(password):
    table_score = [
        has_digit,
        is_very_long,
        has_upper_letters,
        has_lower_letters,
        has_symbols,
    ]
    score = 0
    for check in table_score:
        if check(password):
            score += 2
    return score 


def main():
    password = input("Введите пароль: ")
    score = password_score(password)
    print("Рейтинг пароля:", score)


if __name__ == "__main__":
    main()
