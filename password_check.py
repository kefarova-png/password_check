user_password = "Pass-123"


def checking_password():
    while True:
        entered_password = input("Введите пароль: ")
        if entered_password == user_password:
            print("Пароль верный! Доброго времени суток!")
            return
        print("Неверный пароль. Попробуйте еще раз.")


checking_password()