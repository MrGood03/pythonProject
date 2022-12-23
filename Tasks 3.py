import random

while True:
    print("выбирите номер задания")
    print("1-10")
    print("Exit = 11")
    tasks = int(input("Введите номер задания :"))
    if tasks == 11:
        break
    match tasks:
        case 1:
            list1 = [random.randint(1, 100) for i in range(10, 30)]
            list2 = [random.randint(1, 100) for i in range(10, 30)]
            total = []
            print("первый массив: " + str(list1))
            print("Второй массив:" + str(list2))
            for i in range(len(list1)):
                tr = list1[i]
                if tr % 2 == 0:
                    total.append(tr)
            for i in range(len(list2)):
                check = list2[i]
                if check % 2 > 0:
                    total.append(check)
            print("Отсортированный массив: " + str(total))
        case 2:
            list1 = [random.randint(1, 10) for i in range(10)]
            print("изначальный массив: " + str(list1))
            total = []
            n = len(list1) - 1
            for i in range(len(list1)):
                add = list1[n]
                total.insert(i, add)
                n = n - 1
            print("развёрнутый массив" + str(total))
        case 3:
            list1 = [random.randint(1, 100) for i in range(10)]
            print(list1)
            total = []
            for i in range(len(list1)):
                check = list1[i]
                k = 0
                for n in range(2, check):
                    if check % n == 0:
                        k = k + 1
                if k <= 0 and check != 1:
                    total.append(check)
            print(total)
        case 4:
            print("введите число ")
            number = int(input())
            print("2")
            print("3")
            print("8")
            print("16")
            print("Выбирите сисетму счисления для перевода  ")
            system = int(input())
            # 2
            if system == 2:
                cnumber = []
                while number != 0:
                    n = number % 2
                    if n >= 1:
                        cnumber.append(1)
                    elif n == 0:
                        cnumber.append(0)
                    number = number // 2
                cnumber.reverse()
                print("результат конвертации=" + str(cnumber))
            # 3
            if system == 3:
                cnumber = []
                while number != 0:
                    n = number % 3
                    if n >= 1:
                        cnumber.append(n)
                    elif n == 0:
                        cnumber.append(0)
                    number = number // 3
                cnumber.reverse()
                print("результат конвертации=" + str(cnumber))
            # 8
            if system == 8:
                cnumber = []
                while number != 0:
                    n = number % 8
                    if n >= 1:
                        cnumber.append(n)
                    elif n == 0:
                        cnumber.append(0)
                    number = number // 8
                cnumber.reverse()
                print("результат конвертации=" + str(cnumber))
            # 16
            if system == 16:
                cnumber = []
                while number != 0:
                    n = number % 16
                    if n >= 1:
                        cnumber.append(n)
                    elif n == 0:
                        cnumber.append(0)
                    number = number // 16
                cnumber.reverse()
                print("результат конвертации=" + str(cnumber))
        case 5:
            list1 = [1, 3, 5, 6, 7, 8, 10]
            list2 = [1, 2, 4, 6, 8, 9, 10]
            res = []
            for i in range(len(list1)):
                numbers1 = list1[i]
                for n in range(len(list2)):
                    numbers2 = list2[n]
                    if numbers2 == numbers1:
                        res.append(numbers1)
            print(res)
        case 6:
            print("напишите сколько чисел вы хотите ввести ")
            numof = int(input())
            list = []
            while numof != 0:
                print("Введите число")
                number = int(input())
                list.append(number)
                numof = numof - 1
            print("введённые числа=" + str(list))
        case 7:
            list = [4, 2, 3, 3, 4, 5, 6, 6, 7, 8, 9, 10, 4]

            same = []
            for i in range(len(list)):
                number1 = list[i]
                for n in range(i + 1, len(list)):
                    number2 = list[n]
                    if number1 == number2 and not list[i] in same:
                        same.append(number1)
            print(same)
        case 8:
            select = 1
            while select == 1:
                print("1=вести число")
                print("2=выход")
                select = int(input())

                if select == 1:
                    print("Ведите число")
                    number = int(input())
                    if number % 2 > 0:
                        print(str(number) + "нечётное")
                    elif number % 2 <= 0:
                        print(str(number) + "= чётное")
                elif select == 2:
                    quit()
        case 9:

            izmer = 0
            while izmer != 3:
                print("Выбериете меру измерения")
                print("feet=1\ninches=2\nвыход=3")

                izmer = int(input())
                if izmer == 1:
                    print("введите значение")
                    number = int(input())
                    number = number * 30.48
                    print(str(number) + "cm")
                elif izmer == 2:
                    print("введите значение")
                    number = int(input())
                    number = number * 2.54
                    print(str(number) + "cm")

        case 10:
            system1 = 0
            day = 86400
            hour = 3600
            minute = 60
            second = 1
            print("выберите систему времени")
            print("day=1\nhour=2\nminute=3\nseconds=4\nвыход=5")

            system1 = int(input())
            while system1 != 5:
                print("введите число  для конвертации")
                number = float(input())
                print("выберите систему времени для конвертации")
                print("day=1\nhour=2\nminute=3\nseconds=4")
                system2 = int(input())
                if system1 == 1:
                    if system2 == 1:
                        answer = number * day / day
                        print("Ответ= " + str(answer))
                    elif system2 == 2:
                        answer = (number * day) / hour
                        print("Ответ= " + str(answer))
                    elif system2 == 3:
                        answer = (number * day) / minute
                        print("Ответ= " + str(answer))
                    elif system2 == 4:
                        answer = (number * day) / second
                        print("Ответ= " + str(answer))
                # 2
                elif system1 == 2:
                    if system2 == 1:
                        answer = (number * hour) / day
                        print("Ответ= " + str(answer))
                    elif system2 == 2:
                        answer = (number * hour) / hour
                        print("Ответ= " + str(answer))
                    elif system2 == 3:
                        answer = (number * hour) / minute
                        print("Ответ= " + str(answer))
                    elif system2 == 4:
                        answer = (number * hour) / second
                        print("Ответ= " + str(answer))
                # 3
                elif system1 == 3:
                    if system2 == 1:
                        answer = (number * minute) / day
                        print("Ответ= " + str(answer))
                    elif system2 == 2:
                        answer = (number * minute) / hour
                        print("Ответ= " + str(answer))
                    elif system2 == 3:
                        answer = (number * minute) / minute
                        print("Ответ= " + str(answer))
                    elif system2 == 4:
                        answer = (number * minute) / second
                        print("Ответ= " + str(answer))
                # 4
                elif system1 == 4:
                    if system2 == 1:
                        answer = (number / day)
                        print("Ответ= " + str(answer))
                    elif system2 == 2:
                        answer = (number / hour)
                        print("Ответ= " + str(answer))
                    elif system2 == 3:
                        answer = (number / minute)
                        print("Ответ= " + str(answer))
                    elif system2 == 4:
                        answer = (number / second)
                        print("Ответ= " + str(answer))
