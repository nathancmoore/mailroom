from setuptools import setup

setup(
    name="mailroom",
    description="Command-line script used to track donations and \
    write thank you notes.",
    license="MIT",
    py_modules=['function_names'],
    package_dir={'mailroom'},
    install_requires=[],
    extras_requires={'test': ['pytest, pytest-watch', 'tox']},
    )