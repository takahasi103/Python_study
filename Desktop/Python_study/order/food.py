from menu_item import MenuItem

class Food(MenuItem):
    def __init__(self, name, price, calorie):
        super().__init__(name, price)
        self.calorie = calorie
    
    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.calorie) + 'kcal)'
    
    def calorie_info(self):
        print(str(self.calorie) + 'kcalです')

    def print_menu(foods):
        print('==食べ物メニュー==')
        for index, food in enumerate(foods.values()):
            print(str(index) + '.' + food.info())
        print('=================')

    def set_food(foods):
        name = str(input('名前：'))
        price = int(input('値段：'))
        calorie = int(input('カロリー：'))
        n = len(foods)
        foods['food' + str(n + 1)] = Food(name, price, calorie)
        return foods
    
    def delete_menu_food(foods):
        Food.print_menu(foods)
        i = int(input('削除するメニュー番号を選択して下さい：'))
        del foods['food' + str(i + 1)]

    def set_menu():
        n = int(input('foodメニューを何個登録しますか？:'))
        i = 1
        foods = {}
        while i <= n:
            print(str(i) + '品目のメニュー')
            name = str(input('名前:'))
            price = int(input('値段：'))
            calorie = int(input('カロリー：'))
            print('---------------------')
            foods['food' + str(i)] = Food(name, price, calorie)
            i += 1
        return foods
