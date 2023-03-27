import {{cookiecutter.project_slug}}


def test_version():
    assert {{cookiecutter.project_slug}}.__version__ is not None


def test_program_name():
    assert {{cookiecutter.project_slug}}.PROGRAM_NAME is not None

