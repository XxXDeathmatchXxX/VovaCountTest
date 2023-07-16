import random


def name1():
    name_list = ['Иван', 'Петя', 'Коля', 'Дмитрий']
    random_name = random.choice(name_list)
    return random_name


def name2():
    name_list = ['Алина', 'Настя', 'Света', 'Лена']
    random_name = random.choice(name_list)
    return random_name


def number1():
    random_number = random.choice(range(1, 100))
    return random_number


def number2():
    random_number = random.choice(range(1, 100))
    return random_number


bag = random.choice(range(5, 20))














# name_list = ['Иван', 'Петя', 'Коля', 'Дмитрий']
# randomname1 = random.choice(name_list)
#
# name_list_women = ['Алина', 'Настя', 'Света', 'Лена']
# randomname2 = random.choice(name_list_women)
#
# # number_list = ['1', '2', '3', '4']
# #     random_number = random.choices(number_list, k=3)
# #     number = random_number
# randomnumber1 = random.choice(range(1, 100))
# randomnumber2 = random.choice(range(1, 100))




#print("Наши школьники " f'{result1} ' "и " f'{result2} ' "имеют " f' {randomnumber1} ' "и " f' {randomnumber2} ' "яблок и груш, каждый ")