from food import Food
from drink import Drink

# food1 = Food('サンドイッチ', 500, 330)
# food2 = Food('チョコケーキ', 400, 450)
# food3 = Food('シュークリーム', 200, 180)

# foods = [food1, food2, food3]

# drink1 = Drink('コーヒー', 300, 180)
# drink2 = Drink('オレンジジュース', 200, 350)
# drink3 = Drink('エスプレッソ', 300, 30)

# drinks = [drink1, drink2, drink3]

# Food.print_menu(foods)
# Drink.print_menu(drinks)

print('--------------------')

# food_order = int(input('食べ物の番号を選択してください: '))
# selected_food = foods[food_order]

# drink_order = int(input('飲み物の番号を選択してください: '))
# selected_drink = drinks[drink_order]

# count = int(input('何セット買いますか？(3つ以上で1割引): '))

# result = selected_food.get_total_price(count) + selected_drink.get_total_price(count)

# print('合計は' + str(result) + '円です')

print('--------------------')

# food4 = Food.set_food()
# foods.append(food4)
# Food.print_menu(foods)

# drink4 = Drink.set_drink()
# drinks.append(drink4)
# Drink.print_menu(drinks)

# Food.delete_menu_item(foods)

# Drink.delete_menu(drinks)

foods = Food.set_menu()
# Food.print_menu(foods)
# Food.set_food(foods)
Food.delete_menu_food(foods)
Food.print_menu(foods)

# drinks = Drink.set_menu()
# Drink.print_menu(drinks)
# Drink.set_drink(drinks)
# Drink.delete_drink_item(drinks)
# Drink.print_menu(drinks)