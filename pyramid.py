#gfhdthev
#Программа вычисляет объем усеченной пирамиды


#импортируем библиотеку
from math import sqrt

#главная функция
def main():
    #просим у пользователя ввох значений
    H = int(input('Ввыедите высоту усеченной пирамиды: '))
    S1 = int(input('Ввыедите площадь верхнего основания усеченной пирамиды: '))
    S2 = int(input('Ввыедите площадь нижнего основания усеченной пирамиды: '))
    V = lambda h, s1, s2: (h*(s1+s2+sqrt(s1*s2)))/3 #лямбда функция для нахождения объема
    print(V(H, S1, S2))


#проверяем на прямой запуск
if __name__ == '__main__':
    main()