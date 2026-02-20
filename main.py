from menu import Menu


def main() -> None:
    """
    Запуск консольного интерфейса для работы с карточками товаров.

    Предоставляет меню с возможностью создания, просмотра, изменения,
    списания карточек и вывода списка всех карточек.
    """

    system = Menu()

    while True:
        print("\n" + "=" * 40)
        print("1. Создать карточку")
        print("2. Изменить карточку")
        print("3. Просмотреть карточку")
        print("4. Списать карточку")
        print("5. Список всех карточек")
        print("6. Выход")

        choice = input("Выберите действие (1-6): ").strip()

        match choice:
            case "1":
                card_id = input("Введите ID карточки: ").strip()
                
                if not card_id:
                    print("ID не может быть пустым")
                    continue

                try:
                    data = {
                        "name": input("Наименование: ").strip(),
                        "quantity": int(input("Количество: ").strip()),
                        "supplier": input("Поставщик: ").strip(),
                        "manufacturer": input("Производитель: ").strip(),
                        "cost": float(input("Стоимость: ").strip()),
                        "location": input("Местоположение: ").strip(),
                        "articul": input("Артикул: ").strip(),
                        "guarantee": int(
                            input("Гарантия (мес): ").strip() or "0"
                        ),
                        "receipt_date": input(
                            "Дата поступления (ДД.ММ.ГГГГ): "
                        ).strip()
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

                # Проверка существования карточки
                try:
                    system.get_card(card_id)  # Просто проверяем существование
                except ValueError:
                    print(f"Карточка с ID {card_id} не найдена")

                    continue

                data = {}

                print("(Оставьте поле пустым, если не хотите менять)")

                name = input("Новое наименование: ").strip()

                if name:
                    data["name"] = name

                quantity = input("Новое количество: ").strip()

                if quantity:
                    data["quantity"] = int(quantity)

                supplier = input("Новый поставщик: ").strip()

                if supplier:
                    data["supplier"] = supplier

                manufacturer = input("Новый производитель: ").strip()

                if manufacturer:
                    data["manufacturer"] = manufacturer

                cost = input("Новая стоимость: ").strip()

                if cost:
                    data["cost"] = float(cost)

                location = input("Новое местоположение: ").strip()

                if location:
                    data["location"] = location

                articul = input("Новый артикул: ").strip()

                if articul:
                    data["articul"] = articul

                guarantee = input("Новая гарантия: ").strip()

                if guarantee:
                    data["guarantee"] = int(guarantee)

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