# 1 задание:
def get_count_char(str_):
    char_dict = {}
    low_str_list = str_.lower()
    join_ = ''.join(low_str_list.split())
    list_ = list(join_)
    for key in list_:
        if key in char_dict and key.isalpha() is True:
            char_dict[key] += 1
        elif key not in char_dict and key.isalpha() is True:
            char_dict[key] = 1
    return char_dict

main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""

print(get_count_char(main_str))

# задание 2:

def percent_str(char_dict):
    sum_ = sum(char_dict.values())
    for key, value in char_dict.items():
        char_dict[key] = round((value / sum_ * 100), 1)
    return char_dict

print(percent_str(get_count_char(main_str)))
