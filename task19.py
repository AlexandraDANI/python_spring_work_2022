#todo: Требуется создать csv-файл «algoritm.csv» со следующими столбцами:
#– id - номер по порядку (от 1 до 10);
#– текст из списка algoritm

#algoritm = [ "C4.5" , "k - means" , "Метод опорных векторов" , "Apriori" ,
#"EM" , "PageRank" , "AdaBoost", "kNN" , "Наивный байесовский классификатор" , "CART" ]

#Каждое значение из списка должно находится на отдельной строке.

algoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori",
"EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]

f = open("algoritm.csv", "w", encoding="utf-8")

id = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
lgoritm = ["C4.5", "k - means", "Метод опорных векторов", "Apriori",
"EM", "PageRank", "AdaBoost", "kNN", "Наивный байесовский классификатор", "CART"]

new = []
for i in range(len(id)):
    f.write(str(id[i])+"_" + str(algoritm[i]) + "\n")

f.close()


