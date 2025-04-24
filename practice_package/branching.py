def is_weekend(day):
    return day in (6, 7)

def get_discount(amount):
    if amount >= 5000:
        return amount * 0.10
    elif amount >= 1000:
        return amount * 0.05
    return 0

def describe_number(n):
    if n % 2 == 0:
        parity = 'четное'
    else:
        parity = 'нечетное'

    if n < 10:
        digits = 'однозначное'
    elif n < 100:
        digits = 'двузначное'
    else:
        digits = 'трехзначное'

    return f"{parity} {digits} число"

def convert_to_meters(unitNumber, lengthInUnits):
    conversions = {
        1: 0.1,     # дециметр
        2: 1000,    # километр
        3: 1,       # метр
        4: 0.001,   # миллиметр
        5: 0.01     # сантиметр
    }
    return lengthInUnits * conversions.get(unitNumber, 0)

def describe_age(age):
    num_words = {
        20: 'двадцать', 30: 'тридцать', 40: 'сорок', 50: 'пятьдесят',
        60: 'шестьдесят', 70: 'семьдесят', 80: 'восемьдесят',
        90: 'девяносто', 100: 'сто'
    }
    unit_words = {
        1: 'один', 2: 'два', 3: 'три', 4: 'четыре', 5: 'пять',
        6: 'шесть', 7: 'семь', 8: 'восемь', 9: 'девять'
    }

    if age in num_words:
        text = num_words[age]
    else:
        tens = age // 10 * 10
        units = age % 10
        text = num_words[tens] + ' ' + unit_words.get(units, '')

    last_digit = age % 10
    last_two = age % 100

    if 11 <= last_two <= 14:
        suffix = 'лет'
    elif last_digit == 1:
        suffix = 'год'
    elif 2 <= last_digit <= 4:
        suffix = 'года'
    else:
        suffix = 'лет'

    return f"{text.strip()} {suffix}"
