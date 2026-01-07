def load_vacancies(filename):
    vacancies = []
    try:
        file = open(filename, 'r', encoding='utf-8')
        next(file)
        for line in file:
            from models import vacancy_from_string
            vacancy = vacancy_from_string(line)
            if vacancy:
                vacancies.append(vacancy)
        file.close()
    except FileNotFoundError:
        print(f'Ошибка: файл {filename} не найден')
    except Exception as e:
        print(f'Ошибка при чтении файла: {e}')
    return vacancies

def save_vacancies(filename, vacancies):
    try:
        file = open(filename, 'w', encoding='utf-8')
        file.write('должность; стаж; пол; образование; мин_возраст; макс_возраст; языки; оклад; соцпакет; испытательный\n')
        for vacancy in vacancies:
            file.write(vacancy.to_string() + '\n')
        file.close()
        return True
    except Exception as e:
        print(f'Ошибка при сохранении файла: {e}')
        return False