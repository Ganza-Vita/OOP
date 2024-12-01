import unittest
from src.homework_15_1 import Product, Category


class TestProduct(unittest.TestCase):
    def setUp(self):
        """ Создание объекта продукта для использования в тестах. """
        self.product = Product("Яблоко", "Сладкое яблоко", 80, 15)

    def test_initialization(self):
        """ Проверка правильной инициализации объекта Product. """
        self.assertEqual(self.product.name, "Яблоко")
        self.assertEqual(self.product.description, "Сладкое яблоко")
        self.assertEqual(self.product.price, 80)
        self.assertEqual(self.product.quantity, 15)

    def test_price_setter_and_getter(self):
        """ Проверка работы геттера и сеттера для цены. """
        self.product.price = 100
        self.assertEqual(self.product.price, 100)

        # Проверка на установку отрицательной цены
        self.product.price = -50  # Должно вывести сообщение
        self.assertEqual(self.product.price, 100)  # Цена не должна измениться

    def test_string_representation(self):
        """ Проверка строкового представления продукта. """
        self.assertEqual(str(self.product), "Яблоко, 80 руб. Остаток: 15 шт.")

    def test_product_addition(self):
        """ Проверка сложения двух продуктов. """
        product2 = Product("Банан", "Спелый банан", 60, 25)
        total_price = self.product + product2
        self.assertEqual(total_price, (80 * 15) + (60 * 25))


class TestCategory(unittest.TestCase):
    def setUp(self):
        """ Создание категории для использования в тестах. """
        product1 = Product("Яблоко", "Сладкое яблоко", 80, 15)
        product2 = Product("Банан", "Спелый банан", 60, 25)
        self.category = Category("Фрукты", "Свежие фрукты", [product1, product2])

    def test_category_initialization(self):
        """ Проверка правильной инициализации класса Category. """
        self.assertEqual(self.category.name, "Фрукты")
        self.assertEqual(self.category.description, "Свежие фрукты")
        self.assertEqual(len(self.category.products.split('\n')), 2)  # Должны быть два продукта

    def test_add_product(self):
        """ Проверка добавления нового продукта в категорию. """
        new_product = Product("Груша", "Сочная груша", 70, 20)
        self.category.add_product(new_product)
        self.assertEqual(self.category.total_products(), 15 + 25 + 20)  # Общее количество продуктов

    def test_total_products(self):
        """ Проверка правильности подсчета общего количества продуктов. """
        self.assertEqual(self.category.total_products(), 40)  # 15 + 25

    def test_string_representation(self):
        """ Проверка строкового представления категории. """
        self.assertEqual(str(self.category), "Фрукты, количество продуктов: 40 шт.")


if __name__ == '__main__':
    unittest.main()
