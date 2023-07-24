from menu_item import MenuItem

class Drink(MenuItem):
    def __init__(self, name, price, amount):
        super().__init__(name, price)
        self.amount = amount

    def info(self):
        return self.name + ': ¥' + str(self.price) + ' (' + str(self.amount) + 'mL)'

    def print_menu(drinks):
        print('==飲み物メニュー==')
        index = 0
        for index, drink in enumerate(drinks.values()):
            print(str(index) + '. ' + drink.info())
            index += 1
        print('=================')

    def set_drink(drinks):
        name = str(input('名前：'))
        price = int(input('値段：'))
        amount = int(input('量：'))
        n = len(drinks)
        drinks['drink' + str(n + 1)] = Drink(name, price, amount)
        return drinks
    
    def delete_menu(drinks):
        Drink.print_menu(drinks)
        i = int(input('削除するメニュー番号を選択して下さい：'))
        del drinks[i]
        Drink.print_menu(drinks)

    def set_menu():
        n = int(input('drinkメニューを何個登録しますか？:'))
        i = 1
        drinks = {}
        while i <= n:
            print(str(i) + '品目のメニュー')
            name = str(input('名前:'))
            price = int(input('値段：'))
            amount = int(input('量：'))
            print('---------------------')
            drinks['drink' + str(i)] = Drink(name, price, amount)
            i += 1
        return drinks