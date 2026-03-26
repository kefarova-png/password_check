user_password = "Pass-123"

while True:
    entered_password = input("Введите пароль: ")
    if entered_password == user_password:
        print("Пароль верный! Доброго времени суток!")
        break  # веденный пароль совпал с заданным в коде ранее, завершаем цикл
    else:
        print("Неверный пароль. Попробуйте еще раз.")