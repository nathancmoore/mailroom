from setuptools import setup

setup(
    name="mailroom",
    description="Command-line script used to track donations and \
    write thank you notes.",
    py_modules=['mailroom'],
    package_dir={'mailroom'},
    install_requires=[],
    extras_require={'test': ['pytest', 'pytest-watch', 'tox']},
    )