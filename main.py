from models import Vacancy, vacancy_from_string
from report1 import sort_report1
from report2 import sort_report2
from report3 import sort_report3


class VacancyDatabase:
    def __init__(self, filename='vacancies.txt'):
        self.filename = filename
        self.vacancies = []
        self.load_from_file()

    def load_from_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                next(file)
                for line in file:
                    vacancy = vacancy_from_string(line)
                    if vacancy:
                        self.vacancies.append(vacancy)
            print(f'Загружено {len(self.vacancies)} вакансий')
            return True
        except FileNotFoundError:
            print(f'Файл {self.filename} не найден.')
            return False
        except Exception as e:
            print(f'Ошибка: {e}')
            return False

    def save_to_file(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as file:
                file.write(
                    'должность;стаж;пол;образование;мин_возраст;макс_возраст;языки;оклад;соцпакет;испытательный\n')
                for vacancy in self.vacancies:
                    file.write(vacancy.to_string() + '\n')
            print(f'Сохранено {len(self.vacancies)} вакансий')
            return True
        except Exception as e:
            print(f'Ошибка: {e}')
            return False

    def add_vacancy(self, vacancy):
        self.vacancies.append(vacancy)
        return True

    def remove_vacancy(self, index):
        if 0 <= index < len(self.vacancies):
            removed = self.vacancies.pop(index)
            print(f'Вакансия "{removed.position}" удалена.')
            return True
        else:
            print('Неверный индекс.')
            return False

    def get_all_vacancies(self):
        return self.vacancies.copy()

    def count_vacancies(self):
        return len(self.vacancies)


def create_sample_database(db):
    sample_vacancies = [
        Vacancy('Менеджер', 3, 'любой', 'среднее', 37, 68, 'английский', 50000, True, 3),
        Vacancy('Бухгалтер', 5, 'женский', 'среднее специальное', 38, 69, 'нет', 45000, True, 1),
        Vacancy('Программист', 2, 'любой', 'высшее', 56, 70, 'английский', 80000, True, 1),
        Vacancy('Аналитик', 4, 'любой', 'магистратура', 56, 71, 'английский', 90000, True, 2),
        Vacancy('Администратор', 1, 'любой', 'среднее', 65, 72, 'нет', 30000, False, 1),
        Vacancy('Инженер', 4, 'мужской', 'высшее', 56, 73, 'английский', 85000, True, 2),
        Vacancy('Дизайнер', 2, 'любой', 'высшее', 43, 74, 'английский', 60000, True, 3),
        Vacancy('Маркетолог', 3, 'любой', 'высшее', 44, 75, 'английский', 65000, True, 2),
        Vacancy('Тестировщик', 1, 'любой', 'высшее', 45, 76, 'английский', 55000, True, 3),
        Vacancy('Специалист', 4, 'любой', 'высшее', 46, 77, 'нет', 52000, True, 2),
        Vacancy('Консультант', 1, 'любой', 'высшее', 39, 78, 'английский', 42000, False, 2),
        Vacancy('Руководитель', 7, 'любой', 'высшее', 56, 79, 'английский', 120000, True, 3),
        Vacancy('Разработчик', 3, 'любой', 'высшее', 16, 80, 'английский', 95000, True, 2),
        Vacancy('Водитель', 3, 'мужской', 'среднее', 17, 81, 'нет', 40000, False, 2),
        Vacancy('Курьер', 0, 'любой', 'среднее', 51, 82, 'нет', 30000, False, 1),
        Vacancy('Юрист', 5, 'любой', 'высшее', 52, 83, 'английский', 70000, True, 1),
        Vacancy('Секретарь', 1, 'женский', 'среднее', 53, 84, 'английский', 35000, False, 3),
        Vacancy('Оператор', 1, 'любой', 'среднее', 54, 85, 'нет', 32000, False, 1),
        Vacancy('Экономист', 5, 'любой', 'высшее', 55, 86, 'английский', 72000, True, 1),
        Vacancy('Продавец', 1, 'любой', 'среднее', 56, 87, 'нет', 35000, False, 1),
        Vacancy('Переводчик', 3, 'любой', 'высшее', 34, 89, 'английский', 60000, False, 3),
        Vacancy('Логист', 3, 'любой', 'среднее', 58, 90, 'нет', 48000, True, 2),
        Vacancy('Ассистент', 1, 'любой', 'среднее', 43, 91, 'английский', 38000, False, 3),
        Vacancy('Слесарь', 4, 'мужской', 'среднее специальное', 60, 92, 'нет', 50000, True, 2),
        Vacancy('Воспитатель', 3, 'женский', 'высшее', 45, 93, 'нет', 40000, True, 2),
        Vacancy('Повар', 3, 'любой', 'среднее специальное', 62, 94, 'нет', 45000, True, 2),
        Vacancy('Охранник', 2, 'мужской', 'среднее', 63, 95, 'нет', 35000, True, 1),
        Vacancy('Уборщик', 0, 'любой', 'среднее', 64, 96, 'нет', 25000, False, 1),
        Vacancy('Бармен', 1, 'любой', 'среднее', 22, 97, 'нет', 30000, False, 2),
        Vacancy('Парикмахер', 2, 'любой', 'среднее специальное', 66, 98, 'нет', 40000, True, 2),
        Vacancy('Фармацевт', 3, 'любой', 'высшее', 45, 99, 'нет', 50000, True, 1),
        Vacancy('Архитектор', 5, 'любой', 'высшее', 16, 100, 'английский', 85000, True, 3),
    ]

    for vacancy in sample_vacancies:
        db.add_vacancy(vacancy)

    db.save_to_file()
    print(f'Создана база из {len(sample_vacancies)} вакансий')
    return True


def contains_only_letters(text):
    if not text:
        return False
    for char in text:
        if not char.isalpha():
            return False
    return True


def input_vacancy():
    print("\nВвод новой вакансии")

    while True:
        position = input("Должность: ").strip()
        if not position:
            print("Должность не может быть пустой.")
            continue
        if not contains_only_letters(position):
            print("Должность должна содержать только буквы.")
            continue
        break

    while True:
        try:
            experience = int(input("Необходимый стаж (лет): "))
            if experience < 0:
                print("Стаж не может быть отрицательным.")
                continue
            break
        except ValueError:
            print("Введите целое число.")

    valid_genders = ['мужской', 'женский', 'любой']
    while True:
        gender = input("Пол (мужской/женский/любой): ").strip().lower()
        if gender not in valid_genders:
            print("Некорректный пол. Используйте: мужской, женский, любой.")
            continue
        break

    valid_educations = ['среднее', 'среднее специальное', 'высшее', 'магистратура']
    while True:
        education = input("Образование (среднее/среднее специальное/высшее/магистратура): ").strip().lower()
        if education not in valid_educations:
            print("Некорректное образование.")
            continue
        break

    while True:
        try:
            min_age = int(input("Минимальный возраст: "))
            if min_age < 0:
                print("Возраст не может быть отрицательным.")
                continue
            break
        except ValueError:
            print("Введите целое число.")

    while True:
        try:
            max_age = int(input("Максимальный возраст: "))
            if max_age < 0:
                print("Возраст не может быть отрицательным.")
                continue
            if max_age < min_age:
                print("Максимальный возраст не может быть меньше минимального.")
                continue
            break
        except ValueError:
            print("Введите целое число.")

    while True:
        languages = input("Знание иностранных языков: ").strip()
        if not languages:
            languages = 'нет'
        if not contains_only_letters(languages):
            print("Языки должны содержать только буквы.")
            continue
        break

    while True:
        try:
            min_salary = float(input("Минимальный оклад (руб.): "))
            if min_salary < 0:
                print("Оклад не может быть отрицательным.")
                continue
            break
        except ValueError:
            print("Введите число.")

    while True:
        social_package_input = input("Наличие соцпакета (да/нет): ").strip().lower()
        if social_package_input not in ['да', 'нет']:
            print("Введите 'да' или 'нет'.")
            continue
        social_package = social_package_input == 'да'
        break

    while True:
        try:
            probation = int(input("Испытательный срок (месяцев): "))
            if probation < 0:
                print("Испытательный срок не может быть отрицательным.")
                continue
            break
        except ValueError:
            print("Введите целое число.")

    return Vacancy(position, experience, gender, education, min_age,
                   max_age, languages, min_salary, social_package, probation)


def display_vacancies(vacancies, title="Список вакансий"):
    print(f'\n{title}: {len(vacancies)} вакансий')

    if not vacancies:
        print('Нет вакансий')
        return

    for i, vacancy in enumerate(vacancies, 1):
        print(f'\n{i}. {vacancy.position}')
        print(f'   Образование: {vacancy.education}')
        print(f'   Стаж: {vacancy.experience} лет')
        print(f'   Минимальный возраст: {vacancy.min_age} лет')
        print(f'   Максимальный возраст: {vacancy.max_age} лет')
        print(f'   Оклад: {vacancy.min_salary} руб.')
        print(f'   Соцпакет: {"да" if vacancy.social_package else "нет"}')
        print(f'   Испытательный: {vacancy.probation} мес.')


def display_vacancies_report2(vacancies, title="Список вакансий"):
    print(f'\n{title}: {len(vacancies)} вакансий')

    if not vacancies:
        print('Нет вакансий')
        return

    for i, vacancy in enumerate(vacancies, 1):
        print(f'\n{i}. {vacancy.position}')
        print(f'   Образование: {vacancy.education}')
        print(f'   Стаж: {vacancy.experience} лет')
        print(f'   Минимальный возраст: {vacancy.min_age} лет')
        print(f'   Максимальный возраст: {vacancy.max_age} лет')
        print(f'   Оклад: {vacancy.min_salary} руб.')
        print(f'   Соцпакет: {"да" if vacancy.social_package else "нет"}')
        print(f'   Испытательный: {vacancy.probation} мес.')


def main():
    print("КАДРОВОЕ АГЕНТСТВО")

    db = VacancyDatabase()

    if db.count_vacancies() == 0:
        print("\nБаза данных пуста.")
        create_test = input("Создать тестовую базу данных? (да/нет): ").lower()
        if create_test == 'да':
            create_sample_database(db)

    while True:
        print("\nГЛАВНОЕ МЕНЮ")
        print("1. Показать все вакансии")
        print("2. Добавить вакансию")
        print("3. Удалить вакансию")
        print("4. Отчет 1: Сортировка по образованию и должности")
        print("5. Отчет 2: Испытательный срок ≥2 мес.")
        print("6. Отчет 3: Вакансии по окладу")
        print("7. Выход")

        choice = input("Выберите действие (1-7): ").strip()

        if choice == '1':
            vacancies = db.get_all_vacancies()
            display_vacancies(vacancies, "ВСЕ ВАКАНСИИ")

        elif choice == '2':
            new_vacancy = input_vacancy()
            db.add_vacancy(new_vacancy)
            db.save_to_file()
            print(f'Вакансия "{new_vacancy.position}" добавлена.')

        elif choice == '3':
            vacancies = db.get_all_vacancies()
            if not vacancies:
                print("База данных пуста.")
                continue

            display_vacancies(vacancies, "ТЕКУЩИЕ ВАКАНСИИ")

            while True:
                try:
                    index_input = input("Введите номер вакансии для удаления (или 'отмена' для возврата): ").strip()
                    if index_input.lower() == 'отмена':
                        print("Отмена удаления.")
                        break

                    index = int(index_input) - 1

                    if 0 <= index < len(vacancies):
                        db.remove_vacancy(index)
                        db.save_to_file()
                        break
                    else:
                        print(f"Неверный номер. Введите число от 1 до {len(vacancies)} или 'отмена'.")

                except ValueError:
                    print("Введите число или 'отмена'.")

        elif choice == '4':
            vacancies = db.get_all_vacancies()
            sorted_vac = sort_report1(vacancies)
            display_vacancies(sorted_vac, 'ОТЧЕТ 1: Образование + должность')

        elif choice == '5':
            vacancies = db.get_all_vacancies()
            sorted_vac = sort_report2(vacancies)
            display_vacancies_report2(sorted_vac, 'ОТЧЕТ 2: Испытательный срок ≥2 мес.')

        elif choice == '6':
            while True:
                try:
                    n1 = float(input("Минимальный оклад (руб.): "))
                    if n1 < 0:
                        print("Оклад не может быть отрицательным.")
                        continue
                    break
                except ValueError:
                    print("Введите число.")

            while True:
                try:
                    n2 = float(input("Максимальный оклад (руб.): "))
                    if n2 < 0:
                        print("Оклад не может быть отрицательным.")
                        continue
                    if n1 > n2:
                        print("Минимальный оклад не может быть больше максимального.")
                        continue
                    break
                except ValueError:
                    print("Введите число.")

            vacancies = db.get_all_vacancies()
            sorted_vac = sort_report3(vacancies, n1, n2)
            display_vacancies(sorted_vac, f'ОТЧЕТ 3: Оклад {n1}-{n2} руб.')

        elif choice == '7':
            save = input("Сохранить изменения перед выходом? (да/нет): ").lower()
            if save == 'да':
                db.save_to_file()
            print("Выход")
            break

        else:
            print("Неверный выбор.")


if __name__ == '__main__':
    main()