#todo: Создайте функцию compute_bill, считающаю итоговую сумму товаров в чеке.
#Функция должна принимать 1 параметр - словарь, в котором указано количество едениц товара.
#Цены хранятся в словаре:
#prices = {
#  "banana": 4,
# "apple": 2,
#  "orange": 1.5,
# "pear": 3
#}

food_list = ["apple", "banana", "orange", "pear"]

stock = {"banana": 9,
    "apple": 5,
    "orange": 27,
    "pear": 8
    }

prices = {"banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3
    }

def computeBill(food_list):
    total = 0
    for item in food_list:
        tot = prices[item] * stock[item]
        print(item, tot)
        total += tot
    return total

computeBill(food_list)
print("Итого:")