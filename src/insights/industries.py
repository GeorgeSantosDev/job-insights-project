from typing import List, Dict
from src.insights.jobs import read


def get_unique_industries(path: str) -> List[str]:
    jobs_data = read(path)
    industries_types = set()

    for industrie in jobs_data:
        if industrie['industry'] != '':
            industries_types.add(industrie['industry'])

    return [type for type in industries_types]


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    filtered_industry_list = [job for job in jobs if
                              job['industry'] == industry]
    return filtered_industry_list

