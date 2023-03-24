from functools import lru_cache
from typing import List, Dict
import csv


@lru_cache
def read(path: str) -> List[Dict]:
    try:
        with open(path, encoding='utf-8') as file:
            data = csv.DictReader(file, delimiter=",", quotechar='"')
            jobs = [job for job in data]
    except FileNotFoundError:
        print('Arquivo não encontrado')
    return jobs


def get_unique_job_types(path: str) -> List[str]:
    data_list = read(path)
    types = set()

    for data in data_list:
        types.add(data['job_type'])

    return [type for type in types]


def filter_by_job_type(jobs: List[Dict], job_type: str) -> List[Dict]:
    """Filters a list of jobs by job_type

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    job_type : str
        Job type for the list filter

    Returns
    -------
    list
        List of jobs with provided job_type
    """
    raise NotImplementedError
