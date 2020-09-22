from setuptools import setup, find_packages

setup(
    name="snapshoter",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "snapshot = moduls.main:main",
        ],
    },
    install_requires=[
        # put your requirements separated by comma here
    ],
    version="0.1",
    author="Captain Jack",
    author_email="captain_jack@gmail.com",
    description="Example of the test application",
    license="MIT",
)
