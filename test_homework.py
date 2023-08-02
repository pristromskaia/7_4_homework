from math import pi
import random


def test_greeting():
    """
    Программа, которая выводит на экран приветствие.
    """
    name = "Анна"
    age = 25

    # Сформируем нужную строку
    output = (f"Привет, {name}! Тебе {age} лет.")

    # Проверяем результат
    assert output == "Привет, Анна! Тебе 25 лет."

    # Выводим на экран результат
    print(output)


def test_rectangle():
    """
    Программа, которая берет длину и ширину прямоугольника
    и считает его периметр и площадь.
    """
    a = 10
    b = 20

    # Считаем  периметр
    perimeter = 2 * a + 2 * b

    # Проверяем результат
    assert perimeter == 60

    # Считаем площадь
    area = a * b

    # Проверяем результат
    assert area == 200


def test_circle():
    """
    Программа, которая берет радиус круга и выводит на экран его длину и площадь.
    Используйте константу PI
    """
    r = 23

    # Считаем площадь
    area = pi * r ** 2

    # Проверяем результат
    assert area == 1661.9025137490005

    # Выводим на экран результат
    print(area)

    # Считаем длину окружности
    length = pi * r * 2

    # Проверяем результат
    assert length == 144.51326206513048

    # Выводим на экран результат
    print(length)


def test_random_list():
    """
    Создаем список из 10 случайных чисел от 1 до 100 и отсортируем его по возрастанию.
    """

    # Cоздаем список
    l = sorted([random.randint(1, 100) for _ in range(10)])

    # Проверяем результат
    assert len(l) == 10
    assert l[0] < l[-1]


def test_unique_elements():
    """
    Удалите из списка все повторяющиеся элементы
    """
    l = [1, 2, 3, 4, 5, 5, 5, 6, 7, 8, 8, 9, 10, 10]

    # Преобразуем в множество и обратно в список
    l = list(set(l))

    # Проверяем результат
    assert isinstance(l, list)
    assert len(l) == 10
    assert l == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def test_dicts():
    """
    Создаем словарь из двух списков - первый список как ключи, а второй - как значения.
    Выводим на экран все значения словаря.
    """

    first = ["a", "b", "c", "d", "e"]
    second = [1, 2, 3, 4, 5]

    # Создаем словарь
    d = dict(zip(first, second))

    # Проверяем результат
    assert isinstance(d, dict)
    assert len(d) == 5

    # Выводим на экран результат
    print(d)