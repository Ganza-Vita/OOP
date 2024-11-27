import unittest
from io import StringIO
import sys
from src.task_14_2 import Product, Category


class TestProduct(unittest.TestCase):

    def setUp(self):
        self.product = Product("Тестовый продукт", "Тестовое описание", 100, 10)

    def test_initial_price(self):
        self.assertEqual(self.product.price, 100)

    def test_price_setter_success(self):
        self.product.price = 150
        self.assertEqual(self.product.price, 150)

    def test_price_setter_negative(self):
        captured_output = StringIO()  # Создаем временный вывод
        sys.stdout = captured_output  # Перенаправляем stdout
        self.product.price = -50  # Устанавливаем отрицательную цену
        sys.stdout = sys.__stdout__  # Возвращаем stdout
        self.assertIn("Цена не должна быть нулевая или отрицательная", captured_output.getvalue())

    def test_price_setter_zero(self):
        captured_output = StringIO()  # Создаем временный вывод
        sys.stdout = captured_output  # Перенаправляем stdout
        self.product.price = 0  # Устанавливаем цену в 0
        sys.stdout = sys.__stdout__  # Возвращаем stdout
        self.assertIn("Цена не должна быть нулевая или отрицательная", captured_output.getvalue())

    def test_new_product_creation(self):
        new_product_info = {
            "name": "Продукт C",
            "description": "Описание C",
            "price": 200,
            "quantity": 5
        }
        new_product = Product.new_product(new_product_info)
        self.assertEqual(new_product.name, "Продукт C")
        self.assertEqual(new_product.description, "Описание C")
        self.assertEqual(new_product.price, 200)
        self.assertEqual(new_product.quantity, 5)


class TestCategory(unittest.TestCase):

    def setUp(self):
        self.product1 = Product("Продукт 1", "Описание 1", 100, 10)
        self.product2 = Product("Продукт 2", "Описание 2", 150, 5)
        self.category = Category("Категория 1", "Описание категории 1", [self.product1, self.product2])

    def test_initial_products(self):
        self.assertEqual(len(self.category.products), 2)

    def test_add_product(self):
        product3 = Product("Продукт 3", "Описание 3", 200, 15)
        self.category.add_product(product3)
        self.assertEqual(len(self.category.products), 3)

    def test_product_count(self):
        self.assertEqual(Category.product_count, 2)  # Количество при инициализации
        product3 = Product("Продукт 3", "Описание 3", 200, 15)
        self.category.add_product(product3)
        self.assertEqual(Category.product_count, 3)  # После добавления

    def test_get_products(self):
        expected_output = f"{self.product1}, {self.product1.price} руб. Остаток: {self.product1.quantity} шт.\n{self.product2}, {self.product2.price} руб. Остаток: {self.product2.quantity} шт."
        self.assertEqual(self.category.get_products(), expected_output)
