from sorting import quick_sort


def sort_report2(vacancies):

    filtered = []
    for v in vacancies:
        if v.probation >= 2:
            filtered.append(v)

    def compare_vacancies(v1, v2):

        if v1.probation > v2.probation:
            return -1
        elif v1.probation < v2.probation:
            return 1
        else:
            if v1.experience > v2.experience:
                return -1
            elif v1.experience < v2.experience:
                return 1
            else:
                if v1.max_age < v2.max_age:
                    return -1
                elif v1.max_age > v2.max_age:
                    return 1
                else:
                    return 0

    if filtered:
        quick_sort(filtered, 0, len(filtered) - 1, compare_vacancies)
    return filtered