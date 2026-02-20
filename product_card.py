import datetime


class ProductCard:
    """
    Класс, который позволяет создавать, изменять, просматривать и списывать карточки товаров.
    """

    STATUS_DRAFT = "почти доработал"
    STATUS_IN_STOCK = "состоит на учёте"
    STATUS_WRITTEN_OFF = "списано"

    def __init__(
            self,
            card_id: str,
            name: str,
            quantity: int,
            supplier: str,
            manufacturer: str,
            cost: float,
            location: str,
            articul: str,
            guarantee: int,
            receipt_date: str
    ) -> None:
        """
        Инициализация карточки товара с указанными параметрами.

        Args:
            card_id: Айди карточки
            name: Наименование товара
            quantity: Количество единиц товара
            supplier: Наименование поставщика
            manufacturer: Наименование производителя
            cost: Стоимость единицы товара в рублях
            location: Место хранения на складе
            articul: Артикул товара
            guarantee: Гарантийный срок в месяцах
            receipt_date: Дата поступления на склад в формате ДД.ММ.ГГГГ
        """

        self._card_id = card_id
        self._name = name
        self._quantity = quantity
        self._status = self.STATUS_DRAFT
        self._supplier = supplier
        self._manufacturer = manufacturer
        self._cost = cost
        self._location = location
        self._articul = articul
        self._guarantee = guarantee
        self._receipt_date = receipt_date

    def get_card_id(self) -> str:
        """Айди карточки."""

        return self._card_id

    def get_name(self) -> str:
        """Наименование товара."""

        return self._name

    def get_quantity(self) -> int:
        """Количество единиц товара на складе."""

        return self._quantity

    def get_status(self) -> str:
        """Текущий статус карточки."""

        return self._status

    def get_supplier(self) -> str:
        """Наименование поставщика товара."""

        return self._supplier

    def get_manufacturer(self) -> str:
        """Наименование производителя товара."""

        return self._manufacturer

    def get_cost(self) -> float:
        """Стоимость единицы товара в рублях."""

        return self._cost

    def get_location(self) -> str:
        """Место хранения товара на складе."""

        return self._location

    def get_articul(self) -> str:
        """Артикул товара."""

        return self._articul

    def get_guarantee(self) -> int:
        """Гарантийный срок в месяцах."""

        return self._guarantee

    def get_receipt_date(self) -> str:
        """Дата поступления товара на склад."""

        return self._receipt_date

    def set_name(self, value: str) -> None:
        """
        Изменение наименования товара.

        Args:
            value: Новое наименование товара

        Raises:
            ValueError: При попытке установить пустое наименование
        """

        if not value or not value.strip():
            raise ValueError("Название не может быть пустым")

        self._name = value.strip()

    def set_quantity(self, value: int) -> None:
        """
        Изменение количества товара.

        Args:
            value: Новое количество единиц товара

        Raises:
            ValueError: При попытке установить отрицательное количество
        """

        if value < 0:
            raise ValueError("Количество не может быть отрицательным")

        self._quantity = value

    def set_status(self, value: str) -> None:
        """
        Изменение статуса карточки.

        Args:
            value: Новый статус карточки

        Raises:
            ValueError: При попытке установить недопустимый статус
        """

        valid_statuses = [
            self.STATUS_DRAFT,
            self.STATUS_IN_STOCK,
            self.STATUS_WRITTEN_OFF
        ]

        if value not in valid_statuses:
            raise ValueError(
                f"Некорректный статус. Допустимые значения: "
                f"{', '.join(valid_statuses)}"
            )

        self._status = value

    def set_supplier(self, value: str) -> None:
        """
        Изменение поставщика товара.

        Args:
            value: Новое наименование поставщика

        Raises:
            ValueError: При попытке установить пустого поставщика
        """

        if not value or not value.strip():
            raise ValueError("Поставщик не может быть пустым")

        self._supplier = value.strip()

    def set_manufacturer(self, value: str) -> None:
        """
        Изменение производителя товара.

        Args:
            value: Новое наименование производителя

        Raises:
            ValueError: При попытке установить пустого производителя
        """

        if not value or not value.strip():
            raise ValueError("Производитель не может быть пустым")

        self._manufacturer = value.strip()

    def set_cost(self, value: float) -> None:
        """
        Изменение стоимости товара.

        Args:
            value: Новая стоимость в рублях

        Raises:
            ValueError: При попытке установить отрицательную стоимость
        """

        if value < 0:
            raise ValueError("Стоимость не может быть отрицательной")

        self._cost = value

    def set_location(self, value: str) -> None:
        """
        Изменение местоположения товара.

        Args:
            value: Новое место хранения

        Raises:
            ValueError: При попытке установить пустое местоположение
        """

        if not value or not value.strip():
            raise ValueError("Местоположение не может быть пустым")

        self._location = value.strip()

    def set_articul(self, value: str) -> None:
        """
        Изменение артикула товара.

        Args:
            value: Новый артикул товара
        """

        self._articul = value.strip() if value else ""

    def set_guarantee(self, value: int) -> None:
        """
        Изменение гарантийного срока.

        Args:
            value: Новый гарантийный срок в месяцах

        Raises:
            ValueError: При попытке установить отрицательный срок
        """

        if value < 0:
            raise ValueError("Гарантия не может быть отрицательной")

        self._guarantee = value

    def set_receipt_date(self, value: str) -> None:
        """
        Изменение даты поступления товара.

        Args:
            value: Новая дата в формате ДД.ММ.ГГГГ

        Raises:
            ValueError: При неверном формате даты
        """

        if value:
            try:
                self._receipt_date = datetime.datetime.strptime(
                    value, "%d.%m.%Y"
                )
            except ValueError as e:
                raise ValueError(
                    "Дата должна быть в формате ДД.ММ.ГГГГ"
                ) from e
        else:
            self._receipt_date = None

    def create(self, data: dict) -> 'ProductCard':
        """
        Заполнение карточки данными с последующей сменой статуса на "на учете"

        Args:
            data: Словарь с данными карточки, содержащий ключи:
                name, quantity, supplier, manufacturer, cost,
                location, articul, guarantee, receipt_date

        Returns:
            ProductCard: Заполненная карточка в статусе "на учёте"

        Raises:
            Exception: При ошибке валидации или заполнения данных
        """

        self.set_name(data["name"])
        self.set_quantity(data["quantity"])
        self.set_supplier(data["supplier"])
        self.set_manufacturer(data["manufacturer"])
        self.set_cost(data["cost"])
        self.set_location(data["location"])
        self.set_articul(data.get("articul", ""))
        self.set_guarantee(data.get("guarantee", 0))
        self.set_receipt_date(data.get("receipt_date", ""))
        self.set_status(self.STATUS_IN_STOCK)

        print(f"Карточка {self._card_id} создана")

        return self

    def update(self, data: dict) -> 'ProductCard':
        """
        Обновление указанных полей карточки.

        Args:
            data: Словарь с обновляемыми данными.
                  Может содержать ключи: name, quantity, supplier,
                  manufacturer, cost, location, articul, guarantee,
                  receipt_date

        Returns:
            ProductCard: Обновленная карточка

        Raises:
            ValueError: При попытке обновить списанную карточку
            Exception: При ошибке валидации новых данных
        """

        if self._status == self.STATUS_WRITTEN_OFF:
            raise ValueError(
                "Нельзя изменять списанную карточку"
            )

        if "name" in data:
            self.set_name(data["name"])

        if "quantity" in data:
            self.set_quantity(data["quantity"])

        if "supplier" in data:
            self.set_supplier(data["supplier"])

        if "manufacturer" in data:
            self.set_manufacturer(data["manufacturer"])

        if "cost" in data:
            self.set_cost(data["cost"])

        if "location" in data:
            self.set_location(data["location"])

        if "articul" in data:
            self.set_articul(data["articul"])

        if "guarantee" in data:
            self.set_guarantee(data["guarantee"])

        if "receipt_date" in data:
            self.set_receipt_date(data["receipt_date"])

        print(f"Карточка {self._card_id} обновлена")

        return self

    def get_data(self) -> dict:
        """
        Полные данные карточки в формате словаря.

        Returns:
            dict: Словарь со всеми полями карточки и их значениями
        """

        receipt = "не указана"

        if self._receipt_date:
            receipt = self._receipt_date.strftime("%d.%m.%Y")

        guarantee = "нет"

        if self._guarantee:
            guarantee = f"{self._guarantee} мес."

        return {
            "ID": self._card_id,
            "Наименование": self._name,
            "Количество": self._quantity,
            "Состояние": self._status,
            "Поставщик": self._supplier,
            "Производитель": self._manufacturer,
            "Стоимость": f"{self._cost:.2f} руб.",
            "Местоположение": self._location,
            "Артикул": self._articul or "не указан",
            "Гарантия": guarantee,
            "Дата поступления": receipt
        }

    def write_off(self) -> 'ProductCard':
        """
        Списание карточки со статусом "на учёте".

        При наличии остатков запрашивает подтверждение списания.

        Returns:
            ProductCard: Списанная карточка со статусом "списано"

        Raises:
            ValueError: При неверном статусе или отмене списания пользователем
        """

        if self._status != self.STATUS_IN_STOCK:
            raise ValueError(
                f"Списание возможно только для статуса "
                f"'{self.STATUS_IN_STOCK}'"
            )

        if self._quantity > 0:
            print(f"Остаток на складе: {self._quantity} шт.")

            answer = input("Подтвердить списание? (да/нет): ").lower()

            if answer != "да":
                raise ValueError("Списание отменено пользователем")

        self.set_status(self.STATUS_WRITTEN_OFF)

        print(f"Карточка {self._card_id} списана")

        return self