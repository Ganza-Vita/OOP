import unittest

from src.homework_16_1 import Category, Product, Smartphone, LawnGrass

class TestProduct(unittest.TestCase):
    def test_product_initialization(self):
        product = Product("Товар 1", "Описание товара", 100.0, 10)
        self.assertEqual(product.name, "Товар 1")
        self.assertEqual(product.description, "Описание товара")
        self.assertEqual(product.price, 100.0)
        self.assertEqual(product.quantity, 10)

    def test_price_setter(self):
        product = Product("Товар 1", "Описание товара", 100.0, 10)
        product.price = 150.0
        self.assertEqual(product.price, 150.0)

    def test_price_setter_invalid(self):
        product = Product("Товар 1", "Описание товара", 100.0, 10)
        with self.assertRaises(Exception):  # Проверяем, что при установке отрицательной цены происходит ошибка
            product.price = -50.0

    def test_str(self):
        product = Product("Товар 1", "Описание товара", 100.0, 10)
        self.assertEqual(str(product), "Товар 1, 100.0 руб. Остаток: 10 шт.")


class TestCategory(unittest.TestCase):
    def test_category_initialization(self):
        product1 = Product("Товар 1", "Описание товара", 100.0, 10)
        category = Category("Категория 1", "Описание категории 1", [product1])
        self.assertEqual(category.name, "Категория 1")
        self.assertEqual(category.description, "Описание категории 1")
        self.assertEqual(len(category.products), 1)

    def test_add_product(self):
        product1 = Product("Товар 1", "Описание товара", 100.0, 10)
        product2 = Smartphone("Смартфон 1", "Описание смартфона", 50000.0, 5, "10 часов", "Model X", "64GB", "Black")
        category = Category("Категория 1", "Описание категории 1", [])
        category.add_product(product1)
        category.add_product(product2)
        self.assertEqual(len(category.products), 2)

    def test_add_invalid_product(self):
        category = Category("Категория 1", "Описание категории 1", [])
        with self.assertRaises(TypeError):
            category.add_product("Некорректный тип")  # Передаем строку вместо продукта

    def test_total_products(self):
        product1 = Product("Товар 1", "Описание товара", 100.0, 10)
        product2 = LawnGrass("Трава", "Газонная трава", 1500.0, 20, "Россия", "14-28 дней", "Зеленый")
        category = Category("Категория 1", "Описание категории 1", [product1, product2])
        self.assertEqual(category.total_products(), 30)


class TestSmartphone(unittest.TestCase):
    def test_smartphone_initialization(self):
        smartphone = Smartphone("Смартфон 1", "Описание смартфона", 50000.0, 5, "10 часов", "Model X", "64GB", "Black")
        self.assertEqual(smartphone.name, "Смартфон 1")
        self.assertEqual(smartphone.efficiency, "10 часов")


class TestLawnGrass(unittest.TestCase):
    def test_lawn_grass_initialization(self):
        lawn_grass = LawnGrass("Трава", "Газонная трава", 1500.0, 20, "Россия", "14-28 дней", "Зеленый")
        self.assertEqual(lawn_grass.name, "Трава")
        self.assertEqual(lawn_grass.country, "Россия")


if __name__ == '__main__':
    unittest.main()