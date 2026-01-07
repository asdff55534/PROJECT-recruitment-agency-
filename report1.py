from sorting import quick_sort

def sort_report1(vacancies):
    def compare_vacancies(v1, v2):
        edu_order = {'среднее': 1, 'среднее специальное': 2, 'высшее': 3, 'магистратура': 4}
        edu1 = edu_order.get(v1.education, 5)
        edu2 = edu_order.get(v2.education, 5)

        if edu1 != edu2:
            return -1 if edu1 < edu2 else 1

        if v1.position < v2.position:
            return -1
        elif v1.position > v2.position:
            return 1
        else:
            return 0

    sorted_vacancies = vacancies[:]
    if sorted_vacancies:
        quick_sort(sorted_vacancies, 0, len(sorted_vacancies) - 1, compare_vacancies)
    return sorted_vacancies