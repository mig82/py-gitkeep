from setuptools import setup

setup(
    name='gitkeep',
    version='0.1',
    py_modules=['gitkeep'],
    install_requires=[
        'Click',
    ],
    entry_points='''
        [console_scripts]
        gitkeep=gitkeep:gitkeep
    ''',
)
