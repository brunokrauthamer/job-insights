from src.pre_built.brazilian_jobs import read_brazilian_file
from unittest.mock import patch


def function_mock(path):
    return [{"titulo": "Maquinista", "salario": "2000", "tipo": "trainee"}]

def test_brazilian_jobs():
    jobs_en = [{"title": "Maquinista", "salary": "2000", "type": "trainee"}]
    with patch("src.pre_built.brazilian_jobs.jobs.read", function_mock):
        result = read_brazilian_file("any path")
        assert result == jobs_en
