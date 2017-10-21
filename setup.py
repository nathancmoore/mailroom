from setuptools import setup

setup(
    name="mailroom",
    description="Command-line script used to track donations and \
    write thank you notes.",
    py_modules=['mailroom'],
    install_requires=['builtins', 'terminaltables', 'faker'],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    )