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
            print("Цена не должна быть нулевая или отрицательная")
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


class Category:
    """ Описывает название, описание и список товаров категории продуктов """

    category_count = 0
    product_count = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.__products = products  # Инициализируем приватный список товаров
        Category.category_count += 1
        Category.product_count += len(products)

    def add_product(self, product: Product):
        """ Добавляет продукт в категорию. """
        self.__products.append(product)
        Category.product_count += 1

    @property
    def products(self):
        """ Геттер для получения продуктов. """
        return self.__products

    def get_products(self):
        """ Возвращает строковое представление всех товаров в категории. """
        return '\n'.join(str(product) for product in self.__products)

