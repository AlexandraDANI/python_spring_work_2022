#todo: Дан массив размера N. Найти индексы двух ближайших чисел из этого массива.

#Пример:
#масса  = [ 1 , 2 , 17 , 16 , 30 , 51 , 2 , 70 , 3 , 2 ]

#Для чисел 2 индексы двух ближайших чисел: 6 и 9

#Пример:
#масса  = [ 1 , 2 , 17 , 54 , 30 , 89 , 2 , 1 , 6 , 2 ]
#Для чисел 1 индексы двух ближайших чисел: 0 и 7
#Для чисел 2 индексы двух ближайших чисел: 6 и 9



print("Mасса = [2, 5, 8, 6, 7, 64, 55, 2, 8, 63]")
M = [2, 5, 8, 6, 7, 64, 55, 2, 8, 63]
a = (int(input()))
x = [i for i, ltr in enumerate(M) if ltr == a]
print("Для чисел", a, "индексы двух ближайших чисел: ", x)





