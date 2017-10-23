from setuptools import setup

setup(
    name="mailroom",
    description="Command-line script used to track donations and \
    write thank you notes.",
    py_modules=['mailroom'],
    install_requires=[
        'future==0.16.0',
        'terminaltables==3.1.0',
        'Faker==0.8.6'
        ],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    )
