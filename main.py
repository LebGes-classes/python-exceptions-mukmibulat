from menu import Menu
from product_card import ProductCard


def main() -> None:
    """
    Класс для запуска консольного интерфейса для работы с данными карточки.
    """

    system = Menu()

    while True:
        print("1 - Создать карточку")
        print("2 - Изменить карточку")
        print("3 - Просмотреть карточку")
        print("4 - Списать карточку")
        print("5 - Список всех карточек")
        print("6 - Выход")

        choice = input("Выберите действие (1-6): ").strip()

        match choice:
            case "1":
                card_id = input("Введите ID карточки: ").strip()

                if not card_id:
                    print("ID не может быть пустым")
                    continue

                try:
                    name = input("Наименование: ").strip()

                    if not name:
                        print("Наименование не может быть пустым")
                        continue

                    try:
                        quantity = int(input("Количество: ").strip())
                    except ValueError:
                        print("Количество должно быть числом")
                        continue

                    supplier = input("Поставщик: ").strip()

                    if not supplier:
                        print("Поставщик не может быть пустым")
                        continue

                    manufacturer = input("Производитель: ").strip()

                    if not manufacturer:
                        print("Производитель не может быть пустым")
                        continue

                    try:
                        cost = float(input("Стоимость: ").strip())
                    except ValueError:
                        print("Стоимость должна быть числом")
                        continue

                    location = input("Местоположение: ").strip()
                    if not location:
                        print("Местоположение не может быть пустым")
                        continue

                    articul = input("Артикул: ").strip()

                    guarantee_str = input("Гарантия (мес): ").strip()
                    guarantee = int(guarantee_str) if guarantee_str else 0

                    receipt_date = input("Дата поступления (ДД.ММ.ГГГГ): ").strip()

                    data = {
                        "name": name,
                        "quantity": quantity,
                        "supplier": supplier,
                        "manufacturer": manufacturer,
                        "cost": cost,
                        "location": location,
                        "articul": articul,
                        "guarantee": guarantee,
                        "receipt_date": receipt_date
                    }

                    system.create_card(card_id, data)

                except ValueError as e:
                    print(f"Ошибка ввода данных: {e}")
                except Exception as e:
                    print(f"Ошибка при создании карточки: {e}")

            case "2":
                card_id = input("Введите ID карточки: ").strip()

                if not card_id:
                    continue

                try:
                    card = system.get_card_object(card_id)
                except ValueError as e:
                    print(f"Ошибка: {e}")
                    continue

                if card.get_status() == ProductCard.STATUS_WRITTEN_OFF:
                    print("Невозможно изменить списанную карточку")
                    continue

                data = {}
                print("(Оставьте поле пустым, если не хотите менять)")

                name = input("Новое наименование: ").strip()

                if name:
                    data["name"] = name

                quantity = input("Новое количество: ").strip()

                if quantity:
                    try:
                        data["quantity"] = int(quantity)
                    except ValueError:
                        print("Количество должно быть числом")
                        continue

                supplier = input("Новый поставщик: ").strip()

                if supplier:
                    data["supplier"] = supplier

                manufacturer = input("Новый производитель: ").strip()

                if manufacturer:
                    data["manufacturer"] = manufacturer

                cost = input("Новая стоимость: ").strip()

                if cost:
                    try:
                        data["cost"] = float(cost)
                    except ValueError:
                        print("Стоимость должна быть числом")
                        continue

                location = input("Новое местоположение: ").strip()

                if location:
                    data["location"] = location

                articul = input("Новый артикул: ").strip()

                if articul:
                    data["articul"] = articul

                guarantee = input("Новая гарантия: ").strip()

                if guarantee:
                    try:
                        data["guarantee"] = int(guarantee)
                    except ValueError:
                        print("Гарантия должна быть числом")
                        continue

                receipt = input("Новая дата поступления: ").strip()

                if receipt:
                    data["receipt_date"] = receipt

                if data:
                    try:
                        system.update_card(card_id, data)
                    except ValueError as e:
                        print(f"Ошибка: {e}")
                    except Exception as e:
                        print(f"Ошибка при обновлении карточки: {e}")
                else:
                    print("Нет данных для обновления")

            case "3":
                card_id = input("Введите ID карточки: ").strip()

                if not card_id:
                    continue

                try:
                    data = system.get_card(card_id)
                    print("\n" + "-" * 40)

                    for key, value in data.items():
                        print(f"{key}: {value}")
                except ValueError as e:
                    print(f"Ошибка: {e}")

            case "4":
                card_id = input("Введите ID карточки: ").strip()

                if not card_id:
                    continue

                try:
                    system.write_off_card(card_id)
                except ValueError as e:
                    print(f"Ошибка: {e}")
                except Exception as e:
                    print(f"Ошибка при списании карточки: {e}")

            case "5":
                system.list_cards()

            case "6":
                print("До свидания!")
                break

            case _:
                print("Неверный выбор. Пожалуйста, выберите 1-6")


if __name__ == "__main__":
    main()