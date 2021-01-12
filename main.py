from managers import ProducerManager, CategoriesManager, SuperManager

"""
Вам необходимо реализовать ĸласс CategoriesManager для
управления данными о ĸатегориях товаров. Далее создать
суперменеджера для доступа ĸаĸ ĸ товарам, таĸ и ĸ менеджерам и
протестировать его работу.
"""


if __name__ == '__main__':

    pm = ProducerManager()
    print(f"Load all producer*s info-> {pm.load_data()}")
    print('=' * 50)

    np = {
        'name': 'LaCosta',
        'price': 9000,
        'rating': 88,
        'design': 'very good'
    }

    np2 = {
        'name': 'Apple',
        'price': 40999,
        'rating': 94,
        'design': 'good'
    }
# Тестируем все методы ProducerManager
    print(pm.add_producer(np))
    print(pm.add_producer(np2))
    pm.delete_producer('Apple')
    print(pm.get_producer('Nike'))

# Тестируем все методы CategoriesManager
    print('=' * 50)
    category = CategoriesManager()
    print(category.load_data())

    new_category = {
        'name': 'shoes'
    }
    category.add_category(new_category)
    print(category.load_data())
    category.delete_category('shoes')
    print(category.get_category('software'))
    print('=' * 50)

# Тестируем SuperManager
    dm = SuperManager()
    print(pm.get_producer('Nike'))
