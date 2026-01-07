from sorting import quick_sort

def sort_report3(vacancies, n1, n2):
    filtered = []
    for v in vacancies:
        if n1 <= v.min_salary <= n2:
            filtered.append(v)

    def compare_vacancies(v1, v2):
        if v1.social_package and not v2.social_package:
            return -1
        elif not v1.social_package and v2.social_package:
            return 1
        else:
            if v1.probation > v2.probation:
                return -1
            elif v1.probation < v2.probation:
                return 1
            else:
                return 0

    if filtered:
        quick_sort(filtered, 0, len(filtered) - 1, compare_vacancies)
    return filtered