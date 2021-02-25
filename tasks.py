import math


# 1
def fizz_buzz(number: int) -> str:
    if not number % 15:
        return 'FizzBuzz'
    elif not number % 5:
        return 'Buzz'
    elif not number % 3:
        return 'Fizz'
    else:
        return str(number)


# 2
def profit(sale: dict) -> float:
    inv = sale.get('inventory')
    return sale.get('sell_price') * inv - sale.get('cost_price') * inv


# 3
def quadratic_solutions(a: int, b: int, c: int) -> int:
    d = b ** 2 - (4 * a * c)
    if d < 0:
        return 0
    elif not d:
        return 1
    else:
        return 2


# 4
def square_areas_difference(radius: int) -> int:
    return (radius * 2) ** 2 / 2


# 5
def list_of_multiples(number: int, length: int) -> list:
    return [i * number for i in range(1, length + 1)]


# 6
def format_date(slash_date: str) -> str:
    date_arr = slash_date.split('/')
    date_arr.reverse()
    return ''.join(date_arr)


# 7
def lines_are_parallel(line1_params, line2_params):
    a1_coefficient = line1_params[1]
    a2_coefficient = line2_params[1]
    try:
        a1_coefficient /= line1_params[0]
        a2_coefficient /= line2_params[0]
    except:
        pass

    return a1_coefficient == a2_coefficient


# 8
def vol_shell(r1, r2):
    def vol(r):
        return (4 / 3) * math.pi * r ** 3

    return round(math.fabs(vol(r1) - vol(r2)), 3)


# 9
def greeting(name):
    GUEST_LIST = {
        "Randy": "Germany",
        "Karla": "France",
        "Wendy": "Japan",
        "Norman": "England",
        "Sam": "Argentina"
    }
    if name in GUEST_LIST:
        return f"Hi! I'm {name}, and I'm from {GUEST_LIST.get(name)}."
    else:
        return "Hi! I'm a guest."


# 10
def stupid_addition(par1, par2):
    if type(par1).__name__ == type(par2).__name__:
        if type(par1).__name__ == 'str':
            return int(par1) + int(par2)
        else:
            return str(par1) + str(par2)
    else:
        return None


# 11
def is_repdigit(number):
    return number >= 0


# 12
def concat(*lists):
    res = []
    for lst in lists:
        res += lst
    return res


# 13
def emptying_values(lst: list) -> list:
    return [type(element)() for element in lst]


# 14
def sum_fractions(lst: list) -> int:
    return round(sum([sub_lst[0] / sub_lst[1] for sub_lst in lst]))


# 15
def get_indices(lst: list, item) -> list:
    res = []
    for indx, element in enumerate(lst):
        if element == item:
            res.append(indx)
    return res


# 16
def count_overlapping(lst: list, number: int) -> int:
    for sub_lst in lst:
        sub_lst.append(sub_lst[0] + 1)
        sub_lst.append(sub_lst[1] - 1)
    return len([True for i in lst if number in i])


# 17
def progress_days(miles_list: list) -> int:
    progress_days_number = 0
    for i in range(len(miles_list) - 1):
        progress_days_number += 1 if miles_list[i + 1] > miles_list[i] else 0
    return progress_days_number


# 18
def square_patch(number: int) -> list:
    res = []
    for i in range(number):
        res.append([number] * number)

    return res


# 19
def oddish_or_evenish(number: int) -> str:
    number_sum = sum(map(int, str(number)))
    return 'Oddish' if number_sum % 2 else 'Evenish'


# 20
def dice_game(lst: list) -> int:
    res = 0
    for tpl in lst:
        if tpl[0] == tpl[1]:
            return 0
        res += sum(tpl)
    return res


# 21
def is_sastry(number: int) -> bool:
    numb_and_successor = int(str(number) * 2) + 1
    return not numb_and_successor ** 0.5 % 1


# 22
def num_of_sublists(lst: list) -> int:
    res = 0
    for element in lst:
        if type(element).__name__ == 'list':
            res += 1
    return res


# 23
def last_dig(a: int, b: int, c: int) -> bool:
    last_a = int(str(a)[-1])
    last_b = int(str(b)[-1])
    last_c = int(str(c)[-1])
    return (last_a * last_b) == last_c


# 24
def count_uppercase(lst: list) -> int:
    res = 0
    for string in lst:
        for letter in string:
            if letter.isupper():
                res += 1
    return res


# 25
def is_pandigital(number: int) -> bool:
    list_number = list(map(int, str(number)))
    for digit in range(10):
        if digit not in list_number:
            return False
    return True

