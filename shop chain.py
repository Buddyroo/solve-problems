# *Дополнительное задание:
# Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет
# свои особенности, но также существуют общие характеристики,
# такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно
# будет использовать для создания различных магазинов.
# Шаги:
# 1. Создай класс Store:
# -Атрибуты класса:
# name: название магазина.
# address: адрес магазина.
# items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
# Методы класса:
# __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь дляitems`.
# -  метод для добавления товара в ассортимент.
# метод для удаления товара из ассортимента.
# метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
# метод для обновления цены товара.
# 2. Создай несколько объектов класса Store:
# Создай не менее трех различных магазинов с разными названиями, адресами и добавь
# в каждый из них несколько товаров.
# 3. Протестировать методы:
# Выбери один из созданных магазинов и протестируй все его методы:
# добавь товар, обнови цену, убери товар и запрашивай цену.
# В поле для ответа загрузи ссылку на GitHub-реп
# озиторий, содержащий код проекта с реализацией задания.

class Store:

    def __init__(self, name, address, items={}):
        self.name = name
        self.address = address
        self.items = items

    def add_items(self,list={}):
        if list!=None:
            updated_list= { key.lower(): value for key , value in list.items()}
            self.items.update(updated_list)

        while True:
            try:
                a = input(f"Чтобы добавить товарные позиции в магазин '{self.name}' по адресу {self.address},\n"
                          f"введите название продукта и цену, через пробел. Когда закончите, введите 'Стоп'.\n")
                if a == "Стоп":
                    break
                else:
                    a = a.split()
                    print(a)
                    self.items[a[0].lower()]=float(a[1])
                    print (self.items)
                    print()
            except ValueError:
                    print("---ОШИБКА: В поле 'Цена' должно быть введено число---")
            except Exception as e:
                print(f"---ОШИБКА: {e}---")

    def delete_items(self,product):
        deleted = self.items.pop(product.lower(),None)
        if deleted != None:
            print(f"Товар {product} был удален из ассортимента магазина {self.name}")
        else:
            print("Такого товара в магазине нет")

    def show_price(self, product):
        price = self.items.get(product.lower(),None)
        if price != None:
            print(f"В магазине {self.name} цена товара {product}: {price}")
        else:
            print(f"Такого товара в магазине {self.name} нет")

    def price_update(self, product, price):
        if product.lower not in self.items.keys():
            print(f"Товара {product} нет в магазине {self.name}")
        else:
            self.items[product.lower()]=price
            print (f"В магазине {self.name} новая цена товара {product}: {price}")

    def list_products(self ):
        print(f"В ассортименте магазина {self.name} находятся следующие товары")
        i=1
        for product,price in self.items.items():
            print(f"{i}. Товар - {product}, цена - {price}")
            i+=1


        

store1 = Store("Цветочный", "Юбилейный проспект, 10")
store1.add_items({"Пион":20,"Тюльпан":30})
store1.list_products()
store2 = Store("Продукты", "Улица Ленина, 10")
store2.add_items()
store3 = Store("Игрушки", "Улица Маяковского, 15")
store3.add_items()
store1.delete_items("пион")
store1.list_products()
store1.delete_items("яблоко")
store1.show_price("тюльпан")
store1.delete_items("яблоко")
store1.show_price("тюльпан")
store1.show_price("яблоко")
store1.update_price("тюльпан")
store1.update_price("яблоко")






