import unittest

from src.homework_17_1 import Category, Product


class TestCategory(unittest.TestCase):

    def setUp(self):
        """ Метод, который будет выполнен перед каждым тестом. """
        # Создаем тестовые продукты
        self.product1 = Product('Product 1', 'Description 1', 100, 10)
        self.product2 = Product('Product 2', 'Description 2', 200, 5)
        self.product3 = Product('Product 3', 'Description 3', 300, 3)

    def test_middle_price_with_products(self):
        """ Проверка средней цены с продуктами в категории. """
        category = Category('Test Category', 'Test Description', [self.product1, self.product2, self.product3])
        self.assertEqual(category.middle_price(), (self.product1.price + self.product2.price + self.product3.price) / 3)

    def test_middle_price_with_no_products(self):
        """ Проверка средней цены без продуктов в категории. """
        category = Category('Empty Category', 'No products', [])
        self.assertEqual(category.middle_price(), 0)  # Ожидаем результат 0 при отсутствии продуктов

    def test_middle_price_with_one_product(self):
        """ Проверка средней цены с одним продуктом в категории. """
        category = Category('Single Product', 'Only one product', [self.product1])
        self.assertEqual(category.middle_price(),
                         self.product1.price)  # Средняя цена должна быть равна цене единственного продукта


