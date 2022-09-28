#выбор действия
print("Выберите арифметическое действие")
print("1=сложение")
print("2=вычитание")
print("3=умножение")
print("4=деление")
print("5=квадратное удравнение")
action=int(input())#выбор действия


#сложение
if action==1:
    print("выберите количество чисел")
    quantity=int(input())#ввод количества чисел
    if quantity <= 1:#условие: должно быть 2 или более числа
        print("недостаточно слагаемых")
    elif quantity==2:#если у нас 2 числа цикл продолжается
        print("Введите 2 числа")
        x=int(input())+int(input())#Ввод двух чисел
    elif quantity>2:#решение если выбрано более 2 чисел
        n=int(1)#счётчик
        print("Введите первое число")
        x=int(input())#ввод первого числа
        while n<quantity:#Стандарт: 2 числа , ввод доп чисел
          print("ведите следющее число")
          x=x+int(input())
          n=n+1
    print("Ответ" + str(x))#вывод ответа


#вычитание
elif action==2:
        print("выберите количество чисел")
        quantity = int(input())  # ввод количества чисел
        if quantity <= 1:  # условие: должно быть 2 или более числа
            print("недостаточно слагаемых")
        elif quantity == 2:  # если у нас 2 числа цикл продолжается
            print("Введите 2 числа")
            x = int(input()) - int(input())#ввод двух чисел
        elif quantity > 2:#решение если более 2 чисел
            n = int(1)  # счётчик
            print("Введите первое число")
            x = int(input())  # ввод первого числа
            while n < quantity:#Стандарт: 2 числа , ввод доп чисел
                print("ведите следющее число")
                x = x - int(input())
                n = n + 1
        print("Ответ" + str(x))

#умножение
elif action==3:
    print("выберите количество чисел")
    quantity = int(input())  # ввод количества чисел
    if quantity <= 1:  # условие: должно быть 2 или более числа
        print("недостаточно чисел")
    elif quantity == 2:  # если у нас 2 числа цикл продолжается
        print("Введите 2 числа")
        x = int(input()) * int(input())
    elif quantity > 2:
        n = int(1)  # счётчик
        print("Введите первое число")
        x = int(input())  # ввод первого числа
        while n < quantity:
            print("ведите следющее число")
            x = x * int(input())
            n = n + 1
    print("Ответ" + str(x))


#Деление
elif action==4:
    print("выберите количество чисел")
    quantity = int(input())  # ввод количества чисел
    if quantity <= 1:  # условие: должно быть 2 или более числа
        print("недостаточно слагаемых")
    elif quantity == 2:  # если у нас 2 числа цикл продолжается
        print("Введите 2 числа")
        x = int(input()) / int(input())
    elif quantity > 2:
        n = int(1)  # счётчик
        print("Введите первое число")
        x = int(input())  # ввод первого числа
        while n < quantity:
            print("ведите следющее число")
            x = x/int(input())
            n = n + 1
    print("Ответ" + str(x))


#квадратное уравнение
elif action==5:
    print("Введите a")#введение трёх переменных
    a=int(input())
    print("Введите b")
    b=int(input())
    print("Введите c")
    c=int(input())

    D=float(b**2-4*a*c)#вычисление дискриминанта
    print("D="+str(D))#вывод дискриминанта
    if D<0:# дискриминант<0
        print("Нет решения")#вывод ответа
    elif D==0:#дискриминант=0
        x1 = float((-1*b)/ (2 * a))#нахождение x

        print("x1="+str(x1))
    elif D>0:#дискриминант > 0
        x1=float((-b-D**0.5)/2*a)#вычисление x1
        x2 =float( ((-1*b) + D**0.5) / 2 * a)#вычисление x2
        print("ответ=")#вывод ответа
        print(str(x1))
        print(str(x2))







