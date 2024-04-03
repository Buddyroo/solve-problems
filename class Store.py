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

    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        if items == None:
            self.items = {}
        else:
            self.items = { key.lower() : float(value) for key, value in items.items()}

    def add_items(self,list=None):
        if list!=None:
            updated_list= { key.lower(): float(value) for key , value in list.items()}
            self.items.update(updated_list)
        else:
            list = {}
        print(f"\nЧтобы добавить товарные позиции в магазин '{self.name}' по адресу {self.address},\n"
                          f"введите название продукта и цену, через пробел. Когда закончите, введите 'Стоп'.\n")
        while True:
            try:
                a = input()
                if a.lower() == "стоп":
                    break
                else:
                    a = a.split()
                    self.items[a[0].lower()]=float(a[1])
            except ValueError:
                    print("---ОШИБКА: В поле 'Цена' должно быть введено число---")
            except Exception as e:
                print(f"---ОШИБКА: Введите название и цену через пробел---")
    def add_items_in_function(self, product, price):
        self.items[product.lower()] = float(price)
        print(f"\nТовар {product.lower()} с ценой {float(price)} был добавлен в ассортимент магазина {self.name}")

    def delete_items(self,product):
        deleted = self.items.pop(product.lower(),None)
        if deleted != None:
            print(f"\nТовар {product} был удален из ассортимента магазина {self.name}")
        else:
            print(f"\nТовара {product} нет в магазине {self.name}")

    def show_price(self, product):
        price = self.items.get(product.lower(),None)
        if price != None:
            print(f"\nВ магазине {self.name} цена товара {product}: {price}")
        else:
            print(f"\nТовара {product} в магазине {self.name} нет")
        return price

    def price_update(self, product, price):
        if product.lower() not in self.items.keys():
            print(f"\nТовара {product} нет в магазине {self.name}")
        else:
            self.items[product.lower()]= float(price)
            print (f"\nВ магазине {self.name} новая цена товара {product}: {float(price)}")

    def list_products(self ):
        print(f"\nВ ассортименте магазина {self.name} находятся следующие товары")
        print(self.items)
        i=1
        for product,price in self.items.items():
            print(f"{i}. Товар - {product}, цена - {price}")
            i+=1


        


store1 = Store("Цветочный", "Юбилейный проспект, 10")
store1.add_items({"Пион":20,"Тюльпан":30})
store1.add_items_in_function("гладиолус", 20)
store1.list_products()

store2 = Store("Продукты", "Улица Ленина, 10")
store2.add_items()
store2.list_products()

store3 = Store("Игрушки", "Улица Маяковского, 15")
store3.add_items()
store3.list_products()

store1.delete_items("пион")
store1.list_products()

store1.delete_items("яблоко")

store1.show_price("тюльпан")
store1.show_price("яблоко")

store1.price_update("тюльпан", 50)
store1.price_update("яблоко", 40)






