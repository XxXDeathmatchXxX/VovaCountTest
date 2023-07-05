import random
import fractions
from Settings import bag, name1, name2, number1, number2
import math

import cmath


def main():
    boy = name1()
    girl = name2()
    apples = number1()
    pineapples = number2()

    print("Наши школьники ", boy,  "и ", girl,  "имеют ", apples, "и ", pineapples,
      "яблок и груш, соответственно,\nим необходимо отнести их домой, при том, что в сумку вмещается" f' {bag} ' 
      "яблок, либо груш \n"
      "Сколько сумок необъходимо каждому из школьников"
      "  \n\n")



    print('Ответ: ', math.ceil(apples/bag), "для первого и ", math.ceil(pineapples/bag), " для второго школьника.")


import random
import fractions
from Settings import bag, name1, name2, number1, number2
import math
import re
import cmath




# Задача № 10991
def random_logarythm():

    base_of_loogarythm = random.randint(2, 15)
    answer = random.randint(0, 4)
    degree_of_logarythm = base_of_loogarythm**answer
    a = math.log(degree_of_logarythm, base_of_loogarythm)
    task = f'Вычислите: \(log_'"{" + str(base_of_loogarythm)+'}{'+str(degree_of_logarythm)+'}\)'
    return task, answer





#Задача 14526
def random_logarythm_stepen():

    base_of_loogarythm = random.randint(2, 15)
    answer = random.randint(0, 4)
    degree_of_logarythm = base_of_loogarythm**answer
    n = random.randint(1, 5)
    if n < 2:
        a = int(n**math.log(degree_of_logarythm, base_of_loogarythm))
        task = f'Вычислите: \(log_'"{" + str(base_of_loogarythm)+'}{'+str(degree_of_logarythm)+'}\)'
    else:
        a = int(n ** math.log(degree_of_logarythm, base_of_loogarythm))
        task = f'Вычислите: \({n}^'"{"'log_'"{" + str(base_of_loogarythm) + '}{' + str(degree_of_logarythm) + '}}\)'
    return task, a



#Задачи 14526, 14567, 10991
def random_logarythm_stepen_umnojenie():
    base_of_loogarythm = random.randint(2, 6)
    answer = random.randint(0, 4)
    degree_of_logarythm = base_of_loogarythm ** answer
    n = random.randint(1, 3)
    m = random.randint(1, 3)
    if n < 2 and m < 2:
        a = int(n ** (m * math.log(degree_of_logarythm, base_of_loogarythm)))
        task = f'Вычислите: \(log_'"{" + str(base_of_loogarythm) + '}{' + str(degree_of_logarythm) + '}\)'
    elif n >= 2 and m >= 2:
        a = int(n ** (m * math.log(degree_of_logarythm, base_of_loogarythm)))
        task = f'Вычислите:' f'\({n}^'"{"f'{m}*log_'"{" + str(base_of_loogarythm) + '}{' \
               + str(degree_of_logarythm) + '}}\)'
    elif n < 2 and m >= 2:
        a = int(n ** (m * math.log(degree_of_logarythm, base_of_loogarythm)))
        task = f'Вычислите:' f'\({n}^'"{"f'{m}*log_'"{" + str(base_of_loogarythm) + '}{' \
               + str(degree_of_logarythm) + '}}\)'
    elif n >= 2 and m < 2:
        a = int(n ** (m * math.log(degree_of_logarythm, base_of_loogarythm)))
        task = f'Вычислите:' f'\({n}^'"{"f'log_'"{" + str(base_of_loogarythm) + '}{' \
               + str(degree_of_logarythm) + '}}\)'

    return task, a



#Задача № 12242

def random_logarythm_with_fractions():
    list = [2, 3, 4, 8, 9, 16, 27, 81]
    even_or_odd = random.choice(list)
    if even_or_odd % 2 == 0:
        fraction = fractions.Fraction(1, even_or_odd)
        a = int(math.log(fraction, 2))
        task = f'Вычислите: \(log_' r"{\frac" + '{' + str(1) + '}' + '{' + str(even_or_odd) + '}}{' + str(2) + '}\)'
    else:
        fraction = fractions.Fraction(1, even_or_odd)
        a = int(math.log(fraction, 3))
        task = f'Вычислите: \(log_' r"{\frac" + '{' + str(1) + '}' + '{' + str(even_or_odd) + '}}{' + str(3) + '}\)'
    return a, task





# № Задача 14069

def sum_logarytms():
    base_of_loogarythm1 = random.randint(2, 10)
    answer_of_loogarythm1 = random.randint(0, 4)
    degree_of_logarythm1 = base_of_loogarythm1**answer_of_loogarythm1
    n = random.randint(1, 3)
    base_of_loogarythm2 = random.randint(2, 10)
    answer_of_loogarythm2 = random.randint(0, 4)
    degree_of_logarythm2 = base_of_loogarythm2**answer_of_loogarythm2
    a = int(math.log(degree_of_logarythm2, base_of_loogarythm2) + n*math.log(degree_of_logarythm1, base_of_loogarythm1))
    if n > 1:
        task = f'Вычислите сумму логарифмов:\(log_'"{" + str(base_of_loogarythm1) + '}{' + str(degree_of_logarythm1) +\
           '}\)' "+" f'{n}*\(log_'"{" + str(base_of_loogarythm2) + '}{' + str(degree_of_logarythm2) + '}\)'
    else:
        task = f'Вычислите сумму логарифмов:\(log_'"{" + str(base_of_loogarythm1) + '}{' + str(
        degree_of_logarythm1) + '}\)' "+" f'\(log_'"{" + str(base_of_loogarythm2) + '}{' + str(degree_of_logarythm2) + '}\)'

    return a, task


# Задачи 14510, 14515
def decrement_logarytms():
    base_of_loogarythm1 = random.randint(2, 10)
    answer_of_loogarythm1 = random.randint(0, 4)
    degree_of_logarythm1 = base_of_loogarythm1**answer_of_loogarythm1
    n = random.randint(1, 3)

    base_of_loogarythm2 = random.randint(2, 10)
    answer_of_loogarythm2 = random.randint(0, 4)
    degree_of_logarythm2 = base_of_loogarythm2**answer_of_loogarythm2
    minus = int(math.log(degree_of_logarythm2, base_of_loogarythm2) - n*math.log(degree_of_logarythm1, base_of_loogarythm1))
    if n > 1:
        task_decrement = f'Вычислите разницу логарифмов:\(log_'"{" + str(base_of_loogarythm2) +\
                         '}{' + str(degree_of_logarythm2) + '}\)' "-" f'{n}*\(log_'"{" + str(base_of_loogarythm1) + \
                         '}{' + str(degree_of_logarythm1) + '}\)'
    else:
        task_decrement = f'Вычислите разницу логарифмов:\(log_'"{" + str(base_of_loogarythm2) + '}{' + str(
            degree_of_logarythm2) + '}\)' "-" f'\(log_'"{" + str(base_of_loogarythm1) + '}{' + str(
            degree_of_logarythm1) + '}\)'

    return minus, task_decrement












# l = 3**math.log(8, 2)
# print(l)
#
#
# k = 8**(4*math.log(3, 16))
# print(k)


