from product_card import ProductCard


class Menu:
    """
    Система управления карточками, которая обеспечивает создание, хранение и операции с карточками товаров.
    """

    def __init__(self) -> None:
        """Инициализация пустой системы хранения карточек."""

        self.cards = {}

    def create_card(self, card_id: str, data: dict) -> ProductCard:
        """
        Добавление новой карточки в систему.

        Args:
            card_id: Айди карточки
            data: Словарь с данными для создания карточки

        Returns:
            ProductCard: Созданная и сохранённая карточка

        Raises:
            ValueError: При попытке создать карточку с существующим ID
            Exception: При ошибке создания карточки
        """

        if card_id in self.cards:
            raise ValueError(f"Карточка с ID {card_id} уже существует")

        card = ProductCard(
            card_id, "", 0, "", "", 0.0, "", "", 0, ""
        ).create(data)

        self.cards[card_id] = card

        return card

    def update_card(self, card_id: str, data: dict) -> ProductCard:
        """
        Обновление существующей карточки в системе.

        Args:
            card_id: Идентификатор обновляемой карточки
            data: Словарь с обновляемыми данными

        Returns:
            ProductCard: Обновленная карточка

        Raises:
            ValueError: Если карточка с указанным ID не найдена
        """

        if card_id not in self.cards:
            raise ValueError(f"Карточка {card_id} не найдена")

        return self.cards[card_id].update(data)

    def get_card(self, card_id: str) -> dict:
        """
        Получение данных карточки по ID.

        Args:
            card_id: Идентификатор карточки

        Returns:
            dict: Словарь с данными карточки

        Raises:
            ValueError: Если карточка с указанным ID не найдена
        """

        if card_id not in self.cards:
            raise ValueError(f"Карточка {card_id} не найдена")

        return self.cards[card_id].get_data()

    def write_off_card(self, card_id: str) -> ProductCard:
        """
        Списание карточки по ID.

        Args:
            card_id: Идентификатор списываемой карточки

        Returns:
            ProductCard: Списанная карточка

        Raises:
            ValueError: Если карточка с указанным ID не найдена
        """

        if card_id not in self.cards:
            raise ValueError(f"Карточка {card_id} не найдена")

        return self.cards[card_id].write_off()

    def list_cards(self) -> None:
        """
        Вывод краткой информации обо всех карточках в системе.

        Для каждой карточки отображается: ID, наименование, статус, количество.
        """

        if not self.cards:
            print("\nНет созданных карточек")

        else:
            print("\n" + "=" * 60)

            for card in self.cards.values():
                data = card.get_data()

                print(
                    f"{data['ID']}: {data['Наименование']} | "
                    f"{data['Состояние']} | {data['Количество']} шт."
                )

            print(f"\nВсего карточек: {len(self.cards)}")