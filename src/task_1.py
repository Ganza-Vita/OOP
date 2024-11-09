class Product():
    """ Описывает название, цену, количество и описание отдельного продукта """

    name: str
    description: str
    price: int
    quantity: int

    def __init__(self, name, description, price, quantity):
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity


class Category():
    """ Описывает название, описание и список товаров категории продуктов """

    name: str
    description: str
    products: list

    sum_products = 0

    def __init__(self, name, description, products):
        self.name = name
        self.description = description
        self.products = products
        Category.sum_products += len(products)
