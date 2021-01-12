from drivers import *


class ProducerManager(JSONDriver):
    def __init__(self, path: str = 'producers.json'):
        super().__init__(path)

    def add_producer(self, producer: dict):
        producers_dict = self.load_data()
        names = [i['name'] for i in producers_dict['producers']]
        if producer['name'] not in names:
            producers_dict['producers'].append(producer)
        else:
            print('Already exist!')
        self.save_data(producers_dict)


    def delete_producer(self, name):
        producers_dict = self.load_data()
        for i, producer in enumerate(producers_dict["producers"]):
            if producer['name'] == name:
                removed = producers_dict["producers"].pop(i)
                print(f'Removed->  {removed}')
                break
        self.save_data(producers_dict)


    def get_producer(self, name) -> dict:
        producers_dict = self.load_data()
        for i, producer in enumerate(producers_dict['producers']):
            if producer['name'] == name:
                return producer


class CategoriesManager(JSONDriver):
    def __init__(self, path: str = 'categories.json'):
        super().__init__(path)

    def add_category(self, categories: dict):
        categories_dict = self.load_data()
        names = [i['name'] for i in categories_dict['categories']]
        if categories['name'] not in names:
            categories_dict['categories'].append(categories)
        else:
            print('Already exist!')
        self.save_data(categories_dict)

    def delete_category(self, name):
        categories_dict = self.load_data()
        for i, categories in enumerate(categories_dict["categories"]):
            if categories['name'] == name:
                removed = categories_dict["categories"].pop(i)
                print(f'Category removed ->  {removed}')
                break
        self.save_data(categories_dict)

    def get_category(self, name) -> dict:
        categories_dict = self.load_data()
        for i, categories in enumerate(categories_dict['categories']):
            if categories['name'] == name:
                return categories


class SuperManager(ProducerManager, CategoriesManager):
    """
Клас Супер менеджера может работать одновременно
и с производителями и продуктами)
    """
    def __init__(self):
        ProducerManager.__init__(self, path='producers.json')
        CategoriesManager.__init__(self, path='categories.json')
