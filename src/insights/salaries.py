from typing import Union, List, Dict
import csv


def read(path: str) -> List[Dict]:
    """Reads a file from a given path and returns its contents

    Parameters
    ----------
    path : str
        Full path to file

    Returns
    -------
    list
        List of rows as dicts
    """
    with open(path) as data_file:
        data_list = csv.DictReader(data_file)
        data = []
        for d in data_list:
            data.append(d)

    return data


def get_max_salary(path: str) -> int:
    """Get the maximum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The maximum salary paid out of all job opportunities
    """
    data = read(path)
    max_salary = set()
    for d in data:
        if d["max_salary"] != 'invalid' and d["max_salary"] != '':
            max_salary.add(int(d["max_salary"]))
    list_max_salary = list(max_salary)
    list_max_salary.sort()
    return list_max_salary[-1]


def get_min_salary(path: str) -> int:
    """Get the minimum salary of all jobs

    Must call `read`

    Parameters
    ----------
    path : str
        Must be passed to `read`

    Returns
    -------
    int
        The minimum salary paid out of all job opportunities
    """
    data = read(path)
    min_salary = set()
    for d in data:
        if d["min_salary"] != 'invalid' and d["min_salary"] != '':
            min_salary.add(int(d["min_salary"]))
    list_min_salary = list(min_salary)
    list_min_salary.sort()
    return list_min_salary[0]


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    try:
        int(job["min_salary"])
        int(job["max_salary"])
        int(salary)
    except (KeyError, ValueError, TypeError):
        raise ValueError
    
    if int(job["min_salary"]) > int(job["max_salary"]):
        raise ValueError
    
    if int(job["min_salary"]) <= int(salary) <= int(job["max_salary"]):
        return True
    return False


def filter_by_salary_range(
    jobs: List[dict],
    salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

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
    """

    answer_jobs = []
    for job in jobs:
        try:
            match = matches_salary_range(job, salary)
        except ValueError:
            # print("min or max salaries invalid")
            pass
        else:
            if match:
                answer_jobs.append(job)
    
    return answer_jobs
