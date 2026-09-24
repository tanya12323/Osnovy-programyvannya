users = {
    "Valeriy": {"password": "11037", "grades": [8, 2, 10, 7, 4, 11, 5, 3]},
    "Ivan": {"password": "8970", "grades": [9, 2, 6, 5, 8, 9, 7, 10]},
    "Misha": {"password": "123", "grades": [5, 11, 4, 9, 12, 1, 8, 11]},
    "Alyosha": {"password": "143", "grades": [2, 9, 4, 11, 6, 6, 6, 7]}
}
u_login = input("Введіть логін: ")
u_password = input("Введіть пароль: ")

if u_login in users and users[u_login]["password"] == u_password:
    grades = users[u_login]["grades"]

    print("")
    print("Вхід успішний! Ласкаво просимо,", u_login)
    print("Ваш перелік оцінок:", grades)
    good = 0
    bad = 0
    for grade in grades:
        if grade >= 5 and grade <= 12:
            good += 1
        elif grade >= 1 and grade < 5:
            bad += 1
    print("Задовільні оцінки:", good)
    print("Незадовільні оцінки:", bad)
elif u_login not in users:
    print("Такого користувача не існує.")
else:
    print("Невірний пароль.")