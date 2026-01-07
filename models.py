class Vacancy:
    def __init__(self, position, experience, gender, education, min_age,
                 max_age, languages, min_salary, social_package, probation):
        self.position = position
        self.experience = experience
        self.gender = gender
        self.education = education
        self.min_age = min_age
        self.max_age = max_age
        self.languages = languages
        self.min_salary = min_salary
        self.social_package = social_package
        self.probation = probation

    def to_string(self):
        social_package_str = 'да' if self.social_package else 'нет'
        return (f'{self.position};{self.experience};{self.gender};{self.education};'
                f'{self.min_age};{self.max_age};{self.languages};{self.min_salary};'
                f'{social_package_str};{self.probation}')

    def display(self):
        social_package_str = 'да' if self.social_package else 'нет'
        return (f'Должность: {self.position}\n'
                f'Стаж: {self.experience} лет\n'
                f'Пол: {self.gender}\n'
                f'Образование: {self.education}\n'
                f'Возраст: {self.min_age}-{self.max_age} лет\n'
                f'Языки: {self.languages}\n'
                f'Оклад: {self.min_salary} руб.\n'
                f'Соцпакет: {social_package_str}\n'
                f'Испытательный срок: {self.probation} мес.\n')


def vacancy_from_string(data_string):
    parts = data_string.strip().split(';')
    if len(parts) != 10:
        return None

    social_package = parts[8] == 'да'

    return Vacancy(
        position=parts[0],
        experience=int(parts[1]),
        gender=parts[2],
        education=parts[3],
        min_age=int(parts[4]),
        max_age=int(parts[5]),
        languages=parts[6],
        min_salary=float(parts[7]),
        social_package=social_package,
        probation=int(parts[9])
    )