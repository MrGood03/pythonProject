while True:
    print("выбирите номер задания")
    print("1-4")
    print("Exit = 5")
    tasks = int(input("Введите номер задания :"))
    if tasks == 5:
        break
    match tasks:
        case 1:
            print("Создайте функцию для поиска минимума среди трех чисел (три параметра функции).")
            import random

            numbers = []
            x1 = random.randint(-100, 100)
            numbers.append(x1)
            x2 = random.randint(-100, 100)
            numbers.append(x2)
            x3 = random.randint(-100, 100)
            numbers.append(x3)
            print(numbers)
            MinNumber = min(numbers)
            print("Минимальное число", MinNumber)
            print(" ")
            print(" ")
        case 2:
            print("Напишите функцию, которая вычисляет количество цифр числа.")
            print("введите число")
            x = int(input())
            i = 1
            while x != 1:
                x = x // 10
                i = i + 1
            print(i)
            print(" ")
            print(" ")
        case 3:
            print("Создайте функцию, которая вычисляет сумму всех чисел от 1 до N. N — параметр функции.")
            print("Введите число до которого будет идти сложение ")
            number = int(input())
            Count = 0
            sum = 0
            if number < 1:
                print("Некорректное число")
            else:
                for i in range(1, number + 1):
                    Count = Count + 1
                    sum = Count + sum

            print("sum=" + str(sum))
            print(" ")
            print(" ")

        case 4:
            print("функцию, которая вычисляет факториал натурального числа N.")
            factorial = 1
            print("введите число")
            n = int(input())
            x = 0
            x = n
            while n > 0:
                factorial = factorial * n
                n = n - 1
            print("факториал числа " + str(x) + " = " + str(factorial))
            print(" ")
            print(" ")
