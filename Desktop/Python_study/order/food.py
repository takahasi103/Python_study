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
        index = 0
        for food in foods:
            print(str(index) + '.' + food.info())
            index += 1
        print('=================')

    def set_food():
        name = str(input('名前：'))
        price = int(input('値段：'))
        calorie = int(input('カロリー：'))
        return Food(name, price, calorie)
    
