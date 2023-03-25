from typing import Union, List, Dict
from src.insights.jobs import read


def get_max_salary(path: str) -> int:
    jobs_data = read(path)
    salaries = [
        job['max_salary'] for job in jobs_data if job['max_salary'].isdigit()
    ]
    int_salaries = list(map(int, salaries))

    return max(int_salaries)


def get_min_salary(path: str) -> int:
    jobs_data = read(path)
    salaries = [
        int(job['min_salary'])
        for job in jobs_data
        if job['min_salary'].isdigit()
    ]
    int_salaries = list(map(int, salaries))

    return min(int_salaries)


def check_salary(salary: Union[int, str]) -> bool:
    try:
        int(salary)
        return False
    except ValueError:
        return True
    except TypeError:
        return True


def check_min_max(min: Union[int, str], max: Union[int, str]) -> bool:
    try:
        return int(min) > int(max)
    except TypeError:
        return True


def check_fields_are_digits(
    min: Union[int, str], max: Union[int, str]
) -> bool:
    try:
        return not str(min).isnumeric() or not str(max).isnumeric()
    except KeyError:
        return True


def check_if_fields_exist(job: Dict) -> bool:
    return 'min_salary' not in job or 'max_salary' not in job


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    validate1 = check_if_fields_exist(job)

    validate2 = check_fields_are_digits(
        job.get('min_salary'), job.get('max_salary')
    )

    validate3 = check_min_max(job.get('min_salary'), job.get('max_salary'))

    validate4 = check_salary(salary)

    if validate1 or validate2 or validate3 or validate4:
        raise ValueError

    return int(job['min_salary']) <= int(salary) <= int(job['max_salary'])


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    '''Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    '''
    raise NotImplementedError
