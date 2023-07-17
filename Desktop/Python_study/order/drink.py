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
        for drink in drinks:
            print(str(index) + '. ' + drink.info())
            index += 1
        print('=================')

    def set_drink():
        name = str(input('名前：'))
        price = int(input('値段：'))
        amount = int(input('量：'))
        return Drink(name, price, amount)
    
    def delete_menu(drinks):
        Drink.print_menu(drinks)
        i = int(input('削除するメニュー番号を選択して下さい：'))
        del drinks[i]
        Drink.print_menu(drinks)