user_password = "Pass-123"
entered_password = ""

while entered_password != user_password:
    entered_password = input("Введите пароль: ")
    if entered_password != user_password:
        print("Неверный пароль. Попробуйте еще раз.")
print("Пароль верный! Доброго времени суток!")