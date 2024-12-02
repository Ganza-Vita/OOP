from abc import ABC, abstractmethod

class BaseProduct(ABC):

    @abstractmethod
    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity

    @abstractmethod
    def get_info(self):
        """ Возвращает информацию о продукте в строковом виде. """
        pass


class LoggerMixin:
    """ Миксин для логирования информации о создании объектов. """

    def __init__(self, *args, **kwargs):
        # Получаем имя класса и параметры
        class_name = self.__class__.__name__
        self._class_name = class_name
        self._params = args, kwargs
        super().__init__(*args, **kwargs)

    def __repr__(self):
        """ Возвращает строковое представление объекта с информацией о создании. """
        args_repr = ", ".join(repr(arg) for arg in self._params[0])
        kwargs_repr = ", ".join(f"{key}={value!r}" for key, value in self._params[1].items())
        params_repr = ", ".join(filter(None, [args_repr, kwargs_repr]))

        return f"{self._class_name}({params_repr}) создан."


class Product(LoggerMixin, BaseProduct):
    """ Описывает название, цену, количество и описание отдельного продукта """

    def __init__(self, name, description, price, quantity):
        super().__init__(name, description, price, quantity)
        self.__price = price  # Приватный атрибут для цены

    @property
    def price(self):
        """ Геттер для атрибута цена """
        return self.__price

    @price.setter
    def price(self, value):
        """ Сеттер для атрибута цена с проверкой """
        if value <= 0:
            raise ValueError("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = value

    def get_info(self):
        """ Возвращает строковое представление продукта. """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    @classmethod
    def new_product(cls, product_info):
        """ Создает экземпляр Product из словаря """
        return cls(
            name=product_info['name'],
            description=product_info['description'],
            price=product_info['price'],
            quantity=product_info['quantity']
        )

    def __str__(self):
        """ Возвращает строковое представление продукта. """
        return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        if type(self) == type(other):
            return (self.price * self.quantity) + (other.price * other.quantity)
        raise TypeError


class Category:
    """ Описывает название, описание и список товаров категории продуктов """

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products=None):
        self.name = name
        self.description = description
        self.__products = products if products is not None else []  # Инициализация списка продуктов, если не передан None
        Category.category_count += 1
        Category.product_count += len(self.__products)

    def add_product(self, product: Product):
        """ Добавляет продукт в категорию. """
        if isinstance(product, (Smartphone, LawnGrass, Product)):
            self.__products.append(product)  # Добавление продукта в список
            Category.product_count += 1  # Увеличение общего счётчика только на 1
        else:
            raise TypeError("Неверный тип продукта.")

    @property
    def products(self):
        """ Геттер для получения продуктов. """
        return self.__products  # Возвращаем приватный список продуктов

    def get_products(self):
        """ Возвращает строковое представление всех товаров в категории. """
        return '\n'.join(str(product) for product in self.__products)

    def total_products(self):
        """ Возвращает общее количество всех товаров в категории. """
        return sum(product.quantity for product in self.__products)

    def __str__(self):
        return f"{self.name}, количество продуктов: {self.total_products()} шт."


class Smartphone(Product):
    def __init__(self, name, description, price, quantity, efficiency, model, memory, color):
        super().__init__(name, description, price, quantity)
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

    def get_info(self):
        """ Возвращает информацию о смартфоне. """
        return (f"{super().get_info()}, Эффективность: {self.efficiency}, Модель: {self.model}, "
                f"Память: {self.memory}, Цвет: {self.color}")


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color

    def get_info(self):
        """ Возвращает информацию о газонной траве. """
        return (f"{super().get_info()}, Страна: {self.country}, "
                f"Период всходов: {self.germination_period}, Цвет: {self.color}")




