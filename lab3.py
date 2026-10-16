password = "123"

catalog = {
    1: ["Макарони", 159.99, 5],
    2: ["Цукерки", 99.50, 20],
    3: ["Шоколадка", 125.00, 10],
    4: ["Чай", 89.70, 7],
    5: ["Молоко", 89.00, 3],
}

cart = {}

count_price = lambda p: f"{p:.2f}грн"
is_num = lambda s: s.strip().isdigit()
item_total = lambda id, quantity: catalog[id][1] * quantity
cart_total = lambda: sum(item_total(id, q) for id, q in cart.items())


def show_catalog():
    print("\nКАТАЛОГ")
    for id, (name, price, stock) in catalog.items():
        print(f"{id}. {name} — {count_price(price)}")


def show_cart():
    print("\nКОШИК")
    if not cart:
        print("Кошик порожній")
        return
    for id, quantity in cart.items():
        name = catalog[id][0]
        print(f"{id}. {name} x{quantity} = {count_price(item_total(id, quantity))}")
    print(f"Разом: {count_price(cart_total())}")


def add_to_cart():
    show_catalog()
    id = input("Введіть id товару: ")
    quantity = input("Кількість: ")
    if not (is_num(id) and is_num(quantity)) or int(id) not in catalog or int(quantity) <= 0:
        print("Некоректні дані")
        return
    id, quantity = int(id), int(quantity)
    in_cart = cart.get(id, 0)
    if in_cart + quantity > catalog[id][2]:
        print(f"Недостатньо товару на складі (доступно: {catalog[id][2]})")
        return
    cart[id] = in_cart + quantity
    print(f"Додано: {catalog[id][0]} x{quantity}")


def remove_from_cart():
    show_cart()
    if not cart:
        return
    id = input("Введіть id товару для видалення: ")
    if not is_num(id) or int(id) not in cart:
        print("Такого товару немає в кошику")
        return
    id = int(id)
    quantity = input("Скільки видалити: ")
    if is_num(quantity) and int(quantity) > 0:
        cart[id] -= int(quantity)
        if cart[id] <= 0:
            del cart[id]
    else:
        print("Некоректна кількість")
        return
    print("Товар видалено з кошика")


def buy():
    if not cart:
        print("Кошик порожній")
        return
    show_cart()
    if input("Підтвердити покупку: ").lower() not in ("так", "т", "y", "yes"):
        print("Покупку скасовано")
        return
    for id, quantity in cart.items():
        catalog[id][2] -= quantity
    print(f"Дякуємо за покупку! Сплачено: {count_price(cart_total())}")
    cart.clear()


def admin_panel():
    if input("Введіть пароль адміністратора: ") != password:
        print("Невірний пароль")
        return
    print("\nЗалишки:")
    for id, (name, price, stock) in catalog.items():
        print(f"{id}. {name} — {count_price(price)} — залишок: {stock} шт.")


def main():
    actions = {
        "1": show_catalog,
        "2": add_to_cart,
        "3": remove_from_cart,
        "4": show_cart,
        "5": buy,
        "6": admin_panel,
    }
    while True:
        print("\n")
        print("1. Переглянути каталог")
        print("2. Додати товар в кошик")
        print("3. Видалити товар з кошика")
        print("4. Переглянути кошик")
        print("5. Купити товари з кошика")
        print("6. Вхід для адміністратора")
        print("0. Вихід")
        choice = input("\n").strip()
        if choice == "0":
            print("До побачення!")
            break
        actions.get(choice, lambda: print("Невірний пункт меню!"))()


main()