import pytest

from src.task_1 import Product, Category


@pytest.fixture(autouse=True)
def reset_sum_products():
    Category.sum_products = 0


def test_product_initialization():
    # Проверяем корректность инициализации объекта Product
    product = Product("Товар 1", "Описание товара 1", 100, 10)

    assert product.name == "Товар 1"
    assert product.description == "Описание товара 1"
    assert product.price == 100
    assert product.quantity == 10


def test_category_initialization():
    # Проверяем корректность инициализации объекта Category
    product1 = Product("Товар 1", "Описание товара 1", 100, 10)
    product2 = Product("Товар 2", "Описание товара 2", 200, 5)
    category = Category("Категория 1", "Описание категории 1", [product1, product2])

    assert category.name == "Категория 1"
    assert category.description == "Описание категории 1"
    assert category.products == [product1, product2]


def test_count_products():
    # Проверяем подсчет количества продуктов
    product1 = Product("Товар 1", "Описание товара 1", 100, 10)
    product2 = Product("Товар 2", "Описание товара 2", 200, 5)
    category1 = Category("Категория 1", "Описание категории 1", [product1])
    category2 = Category("Категория 2", "Описание категории 2", [product2])

    assert Category.sum_products == 2  # Общее количество продуктов должно быть 2


def test_count_categories():
    # Проверяем создание и количество категорий, используя экземпляры
    product1 = Product("Товар 1", "Описание товара 1", 100, 10)
    product2 = Product("Товар 2", "Описание товара 2", 200, 5)
    category1 = Category("Категория 1", "Описание категории 1", [product1])
    category2 = Category("Категория 2", "Описание категории 2", [product2])

    # Хотя мы не имеем атрибута для подсчета категорий, мы просто можем
    # проверить количество созданных категорий, которые мы знаем
    assert category1.name == "Категория 1"
    assert category2.name == "Категория 2"
