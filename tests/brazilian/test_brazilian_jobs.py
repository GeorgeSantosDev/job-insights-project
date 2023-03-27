from src.pre_built.brazilian_jobs import read_brazilian_file


def test_brazilian_jobs():
    data = read_brazilian_file('tests/mocks/brazilians_jobs.csv')
    for job in data:
        assert 'titulo' not in job
        assert 'salario' not in job
        assert 'tipo' not in job
