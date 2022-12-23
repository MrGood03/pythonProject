while True:
    import random
    import math

    print("выбирите номер задания")
    print("1-11")
    print("Exit = 12")

    Ex = int(input())
    if Ex == 12:
        break
    if Ex == 1:
        print("выбирите часть задания")
        print("1-6")
        Ex = int(input())
        # задание 1а
        if Ex == 1:
            print("f = (101 - 0) / 3")
            f = (101 - 0) / 3
            print("Ответ: " + str(f))
            # задание 1b
        elif Ex == 2:
            print("f = 3.0 * math.e - 6 * 10000000.1")
            f = 3.0 * math.e - 6 * 10000000.1
            print("Ответ: " + str(f))
            # задание 1c
        elif Ex == 3:
            true = 1
            false = 0
            print("f = true * false")
            f = true * false
            print("true&false= " + str(f))
            # задание 1d
        elif Ex == 4:
            true = 1
            false = 0
            print("f=true and false")
            f = true and false
            print("true&false= " + str(f))
            # задание 1e
        elif Ex == 5:
            true = 1
            false = 0
            print("f=false and false")
            f = false and false
            print("false&false= " + str(f))
            # задание 1f
        elif Ex == 6:
            true = 1
            false = 0
            print("f = (false or false) and (true and true)")
            f = (false or false) and (true and true)
            print("(false||false)&(true&true)= " + str(f))
    # Задание 2
    elif Ex == 2:
        print("1=ввести самому")
        print("2=рандом")
        z = int(input())
        if z == 1:
            x1 = int(input())
            x2 = int(input())
            x3 = int(input())
            x4 = int(input())
        elif z == 2:
            x1 = random.randint(1, 10)
            print("число 1 =" + str(x1))
            x2 = random.randint(1, 10)
            print("число 2 =" + str(x2))
            x3 = random.randint(1, 10)
            print("число 3 =" + str(x3))
            x4 = random.randint(1, 10)
            print("число 4 =" + str(x4))
        if x1 == x2 == x3 == x4:
            print("равно")
        elif x1 != x2 != x3 != x4:
            print("не равно")
        # Задание 3
        # Задание 3
    elif Ex == 3:
        list = [random.randint(1, 100) for i in range(20)]
        listmax = max(list)
        print("максимальное число списка =" + str(listmax))
        print(list)
        # Задание 4
    elif Ex == 4:
        list = [random.randint(1, 100) for i in range(20)]
        listmin = min(list)
        print("минимальное число списка =" + str(listmin))
        print(list)
        # Задание 5
    elif Ex == 5:
        list = [random.randint(1, 100) for i in range(10, 30)]
        total = []
        print(list)
        meanvalue = sum(list) / len(list)
        print("Среднее значение= " + str(meanvalue))
        for i in range(len(list)):
            tr = list[i]
            if meanvalue < tr:
                total.append((tr))
        print("числа большие среднего значения списка= " + str(total))
        # Задание 6
    elif Ex == 6:

        print("введите первое число ")
        number1 = int(input())
        print("введите второе число")
        total = 0
        for i in range(int(input())):
            total = total + number1
        print("ответ: " + str(total))
        # Задание 7
    elif Ex == 7:
        even = []
        noteven = []
        list = [random.randint(1, 10) for i in range(10)]
        print(list)
        for i in range(len(list)):
            z = list.pop()
            y = z % 2
            if y == 0:
                even.append(z)
            elif y != 0:
                noteven.append(z)
        print("чётные" + str(even))
        print("не чётные " + str(noteven))
        # Задание 8
    elif Ex == 8:
        print("ведите температуру в фарингейтах ")
        temp = int(input())
        gradus = (temp - 32) / 1.8
        print("gradus= " + str(gradus))
        # Задание 9
    elif Ex == 9:
        print("введите вес")
        weight = int(input())
        print("введите рост ")
        height = int(input())
        IMT = weight / height
        print("IMT= " + str(IMT))
        # Задание 10
    elif Ex == 10:
        print("Enter the number")
        number = int(input())
        SecondDegree = number ** 2
        ThirdDegree = number ** 3
        FourthDegree = number ** 4
        print("Second degree= " + str(SecondDegree))
        print("Third degree= " + str(ThirdDegree))
        print("Fourth degree= " + str(FourthDegree))
        # Задание 11
    elif Ex == 11:
        print("Enter side A")
        A = int(input())
        print("Enter side B")
        B = int(input())
        print("Enter side С")
        C = int(input())
        if not A < B + C:
            print("Треугольника с данными сторонами не сущесвтует")
        elif not B < A + C:
            print("Треугольника с данными сторонами не сущесвтует")
        elif C < A + B:
            print("треугольник со сторонама " + str(A) + ", " + str(B) + ", " + str(C) + " существует")
    input('Press ENTER to exit')
