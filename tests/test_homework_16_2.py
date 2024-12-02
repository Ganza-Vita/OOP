import unittest

from src.homework_16_2 import BaseProduct, Product, Smartphone, LawnGrass, LoggerMixin


class TestLoggerMixinAndBaseProduct(unittest.TestCase):
    class TestProduct(LoggerMixin, BaseProduct):
        def __init__(self, name, description, price, quantity):
            super().__init__(name, description, price, quantity)
            self.__price = price

        def get_info(self):
            return f"{self.name}, {self.price} руб. Остаток: {self.quantity} шт."

    def test_base_product_initialization(self):
        product = self.TestProduct("Test Product", "This is a test product", 100, 10)
        self.assertEqual(product.name, "Test Product")
        self.assertEqual(product.description, "This is a test product")
        self.assertEqual(product.price, 100)
        self.assertEqual(product.quantity, 10)

    def test_base_product_get_info(self):
        product = self.TestProduct("Test Product", "This is a test product", 100, 10)
        expected_info = "Test Product, 100 руб. Остаток: 10 шт."
        self.assertEqual(product.get_info(), expected_info)


class TestLoggerMixin(unittest.TestCase):
    # Вспомогательный класс для тестирования LoggerMixin
    class TestProduct(LoggerMixin):
        def __init__(self, name, description, price, quantity):
            super().__init__(name, description, price, quantity)
            self.name = name
            self.description = description
            self.price = price
            self.quantity = quantity

    def test_logger_mixin_repr(self):
        product = self.TestProduct("Test Product", "This is a test product", 100, 10)
        expected_repr = "TestProduct('Test Product', 'This is a test product', 100, 10) создан."
        self.assertEqual(repr(product), expected_repr)

    def test_logger_mixin_init(self):
        product = self.TestProduct("Another Product", "Another test product", 150, 20)
        expected_repr = "TestProduct('Another Product', 'Another test product', 150, 20) создан."
        self.assertEqual(repr(product), expected_repr)