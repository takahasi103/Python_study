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
    
    def edit_food(foods):
        Food.print_menu(foods)
        i = int(input('どのfoodメニューを編集しますか？'))
        food_key = 'food' + str(i)
        if food_key in foods:
            selected_food = foods[food_key]
            print("選択された食べ物メニューの情報：")
            print('1.名前：' + selected_food.name)
            print('2.値段：¥' + str(selected_food.price))
            print('3.カロリー：' + str(selected_food.calorie) + 'kcal')
            n = int(input('どの値を編集しますか？（1:名前 / 2:値段 / 3:カロリー）'))
            if n == 1:
                name = str(input('新しい名前：'))
                selected_food.name = name
            elif n == 2:
                price = int(input('新しい値段：'))
                selected_food.price = price
            elif n == 3:
                calorie = int(input('新しいカロリー：'))
                selected_food.calorie = calorie
            else:
                print("無効な選択です。")
            
            print("編集後の食べ物メニューの情報：")
            print('名前：' + selected_food.name)
            print('値段：¥' + str(selected_food.price))
            print('カロリー：' + str(selected_food.calorie) + 'kcal')
        else:
            print("指定された番号の食べ物メニューは存在しません。")