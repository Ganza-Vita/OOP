class Product:
    """ Описывает название, цену, количество и описание отдельного продукта """

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.__price = price  # Приватный атрибут для цены
        self.quantity = quantity

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


class LawnGrass(Product):
    def __init__(self, name, description, price, quantity, country, germination_period, color):
        super().__init__(name, description, price, quantity)
        self.country = country
        self.germination_period = germination_period
        self.color = color
