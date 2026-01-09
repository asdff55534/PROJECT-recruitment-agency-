def create_sample_database(filename):
    from models import Vacancy
    from file import save_vacancies

    vacancies = [
        Vacancy('Менеджер', 2, 'любой', 'среднее', 25, 45, 'английский', 50000, True, 3),
        Vacancy('Бухгалтер', 5, 'женский', 'среднее специальное', 30, 50, 'нет', 45000, True, 1),
        Vacancy('Программист', 3, 'любой', 'высшее', 22, 40, 'английский', 80000, True, 2),
        Vacancy('Аналитик', 4, 'любой', 'магистратура', 26, 45, 'английский', 90000, True, 2),
        Vacancy('Администратор', 2, 'женский', 'высшее', 22, 40, 'английский', 40000, False, 2),
        Vacancy('Инженер', 4, 'мужской', 'высшее', 25, 50, 'английский', 85000, True, 2),
        Vacancy('Дизайнер', 2, 'любой', 'высшее', 23, 40, 'английский', 60000, True, 3),
        Vacancy('Маркетолог', 3, 'любой', 'высшее', 25, 45, 'английский', 65000, True, 2),
        Vacancy('Тестировщик', 2, 'любой', 'высшее', 22, 40, 'английский', 55000, True, 3),
        Vacancy('Специалист', 4, 'любой', 'высшее', 26, 48, 'нет', 52000, True, 2),
        Vacancy('Консультант', 1, 'любой', 'высшее', 22, 45, 'английский', 42000, False, 2),
        Vacancy('Руководитель', 7, 'любой', 'высшее', 30, 55, 'английский', 120000, True, 3),
        Vacancy('Разработчик', 3, 'любой', 'высшее', 23, 42, 'английский', 95000, True, 2),
        Vacancy('Водитель', 3, 'мужской', 'среднее', 25, 55, 'нет', 40000, False, 2),
        Vacancy('Курьер', 0, 'любой', 'среднее', 18, 40, 'нет', 30000, False, 1),
        Vacancy('Юрист', 5, 'любой', 'высшее', 28, 50, 'английский', 70000, True, 1),
        Vacancy('Секретарь', 1, 'женский', 'среднее', 20, 35, 'английский', 35000, False, 3),
        Vacancy('Оператор', 1, 'любой', 'среднее', 20, 40, 'нет', 32000, False, 1),
        Vacancy('Экономист', 5, 'любой', 'высшее', 27, 52, 'английский', 72000, True, 1),
        Vacancy('Продавец', 1, 'любой', 'среднее', 20, 45, 'нет', 35000, False, 1),
        Vacancy('Переводчик', 3, 'любой', 'высшее', 24, 45, 'английский', 60000, False, 3),
        Vacancy('Логист', 3, 'любой', 'среднее', 25, 50, 'нет', 48000, True, 2),
        Vacancy('Ассистент', 1, 'любой', 'среднее', 20, 35, 'английский', 38000, False, 3),
        Vacancy('Слесарь', 4, 'мужской', 'среднее специальное', 25, 55, 'нет', 50000, True, 2),
        Vacancy('Воспитатель', 3, 'женский', 'высшее', 22, 45, 'нет', 40000, True, 2),
        Vacancy('Повар', 3, 'любой', 'среднее специальное', 22, 50, 'нет', 45000, True, 2),
    ]
    save_vacancies(filename, vacancies)
    return vacancies


def display_vacancies_simple(vacancies, title):
    print(f'{title}: {len(vacancies)} вакансий')

    if not vacancies:
        print('Нет вакансий')
        return

    for i, vacancy in enumerate(vacancies, 1):
        print(f'\n{i}. {vacancy.position}')
        print(f'   Образование: {vacancy.education}')
        print(f'   Стаж: {vacancy.experience} лет')
        print(f'   Испытательный: {vacancy.probation} мес.')
        print(f'   Соцпакет: {"да" if vacancy.social_package else "нет"}')
        print(f'   Оклад: {vacancy.min_salary} руб.')


def main_menu():
    filename = 'vacancies.txt'
    vacancies = []

    try:
        file_test = open(filename, 'r')
        file_test.close()
        file_exists = True
    except:
        file_exists = False

    if file_exists:
        from file import load_vacancies
        vacancies = load_vacancies(filename)
        print(f'Загружено {len(vacancies)} вакансий')
    else:
        print('Создаем новую базу.')
        vacancies = create_sample_database(filename)

    while True:
        print('КАДРОВОЕ АГЕНТСТВО')
        print('1. Все вакансии')
        print('2. Отчет 1: по образованию и должности')
        print('3. Отчет 2: испытательный не менее 2 месяцев')
        print('4. Отчет 3: по окладу')
        print('5. Выход')

        choice = input('Выберите (1-5): ').strip()

        if choice == '1':
            display_vacancies_simple(vacancies, 'ВСЕ ВАКАНСИИ')

        elif choice == '2':
            from report1 import sort_report1
            sorted_vac = sort_report1(vacancies)
            display_vacancies_simple(sorted_vac, 'Полный список всех вакансий, который будет отсортирован следующему ключу: образование (по возрастанию) + должность (по возрастанию).')

        elif choice == '3':
            from report2 import sort_report2
            sorted_vac = sort_report2(vacancies)
            display_vacancies_simple(sorted_vac, 'Список всех вакансий с испытательным сроком не менее 2 месяцев, отсортированный по следующему ключу: испытательный срок (по убыванию) + необходимый стаж работы (по убыванию) + максимальный возраст (по возрастанию).')

        elif choice == '4':
            while True:
                try:
                    n1 = float(input('Минимальный оклад: '))
                    n2 = float(input('Максимальный оклад: '))
                    if n1 > n2:
                        print('Ошибка: минимум больше максимума. Попробуйте снова')
                        continue
                except:
                    print('Ошибка ввода')
                    break

            from report3 import sort_report3
            sorted_vac = sort_report3(vacancies, n1, n2)
            display_vacancies_simple(sorted_vac, f'ОТЧЕТ 3: Оклад {n1}-{n2} руб.')

        elif choice == '5':
            print('Выход')
            break

        else:
            print('Нет такого варианта ответа')

if __name__ == '__main__':
    main_menu()