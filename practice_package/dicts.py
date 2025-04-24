def count_char_occurrences(text):
    result = {}
    for char in text.lower():
        if char.isalpha():  # учитываем только буквы
            result[char] = result.get(char, 0) + 1
    return result

def merge_dicts(dict1, dict2, conflict_resolver):
    merged_dict = dict1.copy()  # копируем первый словарь
    for key, value in dict2.items():
        if key in merged_dict:
            merged_dict[key] = conflict_resolver(key, merged_dict[key], value)
        else:
            merged_dict[key] = value
    return merged_dict

def invert_dictionary(original_dict):
    inverted_dict = {}
    for key, value in original_dict.items():
        if value in inverted_dict:
            inverted_dict[value].append(key)
        else:
            inverted_dict[value] = [key]
    return inverted_dict

def dict_to_table(data_dict, columns):
    # Заголовки столбцов в верхнем регистре
    headers = [col.upper() for col in columns]
    
    # Заполнение таблицы
    table_rows = []
    for row_id, row_data in data_dict.items():
        row = []
        for column in columns:
            # Если атрибута нет, то выводим N/A
            row.append(str(row_data.get(column, 'N/A')))
        table_rows.append(row)

    # Выравнивание колонок по ширине самого длинного значения
    column_widths = [max(len(str(item)) for item in col) for col in zip(*table_rows, headers)]
    
    # Форматирование таблицы
    formatted_table = []
    formatted_table.append('| ' + ' | '.join([headers[i].ljust(column_widths[i]) for i in range(len(headers))]) + ' |')
    formatted_table.append('|' + '|'.join(['-' * column_widths[i] for i in range(len(headers))]) + '|')
    
    for row in table_rows:
        formatted_table.append('| ' + ' | '.join([row[i].ljust(column_widths[i]) for i in range(len(row))]) + ' |')

    return '\n'.join(formatted_table)

def deep_update(base_dict, update_dict):
    result = base_dict.copy()  # копируем исходный словарь
    for key, value in update_dict.items():
        if isinstance(value, dict) and key in result and isinstance(result[key], dict):
            result[key] = deep_update(result[key], value)  # рекурсивно обновляем
        else:
            result[key] = value
    return result
