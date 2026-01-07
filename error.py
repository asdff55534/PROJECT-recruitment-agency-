def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value_str = input(prompt)
            value = int(value_str)
            if min_val is not None and value < min_val:
                print(f'Ошибка: значение должно быть не меньше {min_val}')
                continue
            if max_val is not None and value > max_val:
                print(f'Ошибка: значение должно быть не больше {max_val}')
                continue
            return value
        except ValueError:
            print('Ошибка: введите целое число')

def get_float_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            value_str = input(prompt)
            value = float(value_str)
            if min_val is not None and value < min_val:
                print(f'Ошибка: значение должно быть не меньше {min_val}')
                continue
            if max_val is not None and value > max_val:
                print(f'Ошибка: значение должно быть не больше {max_val}')
                continue
            return value
        except ValueError:
            print('Ошибка: введите число')