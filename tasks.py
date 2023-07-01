import math
import fractions
import random
import numpy as np


def task1():
    a = math.log(16, 2)
    print("Рассчитайте логарифм : В какую степень необходимо вовести 2, для получения числа 16")
    print("Правильный ответ: ", int(a))






def task2():
    a = math.log(64, 2)
    print("Рассчитайте логарифм : В какую степень необходимо вовести 2, для получения числа 64")
    print("Правильный ответ: ", int(a))





def task3():
    a = math.log(2, 2)
    print("Рассчитайте логарифм : В какую степень необходимо вовести 2, для получения числа 2")
    print("Правильный ответ: ", int(a))


def task4():
    a = math.log(1, 2)
    print("Рассчитайте логарифм : В какую степень необходимо вовести 2, для получения числа 1")
    print("Правильный ответ: ", int(a))





def task5():
    random_number1 = random.choice(range(1, 4))
    random_number2 = random.choice(range(3, 9))
    random_number3 = random.choice(range(1, 10))
    f_one = fractions.Fraction(random_number1, random_number2)
    print(f_one)
    a = math.log(f_one, 2)
    print("Рассчитайте логарифм : В какую степень необходимо вовести " f'{random_number3}', "для получения числа " f'{f_one}')
    print("Правильный ответ: ", int(a))


def task6():

    f_one = fractions.Fraction(1, 8)
    a = math.log(f_one, 2)
    print("Рассчитайте логарифм : В какую степень необходимо вовести 2, для получения числа 1/8")
    print("Правильный ответ: ", int(a))


def task7():
    a = math.log(27, 3)
    print("Рассчитайте логарифм : В какую степень необходимо вовести 3, для получения числа 27")
    print("Правильный ответ: ", int(a))
    return a


def random_log():
    random_number = random.choice(range(1, 5))
    return random_number




def random_log_fraction():
    random_number1 = random.choice(range(1, 10))
    random_number2 = random.choice(range(1, 10))

    random_fraction = fractions.Fraction(random_number1, random_number2)
    random_number3 = random.choice(range(1, 3))

    return math.log(random_fraction, random_number3)

# a = random_log_fraction()
# print(a)

def anti_log():
    original = 7
    log_original = np.log(original)
    log_original2 = np.log10(original)
    x = np.exp(log_original2)
    print(log_original)
    np.exp(log_original)
    print(log_original2)
    print(np.exp(log_original))
    print(x)








