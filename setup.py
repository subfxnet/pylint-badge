from setuptools import setup

setup(
    name='pylint-badge',
    version='0.9.6',
    description="Runs pylint to generate badges",
    author="Pouncy Silverkitten",
    author_email="pouncy.sk@gmail.com",
    url="https://github.com/subfxnet/pylint-badge",
    install_requires=["pylint",],
    packages=["pylintbadge"],
    entry_points = {
        'console_scripts': ['pylint-badge=pylintbadge.pylintbadge:main'],
    },
)
