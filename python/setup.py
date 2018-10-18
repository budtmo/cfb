from setuptools import setup

with open('requirements.txt', 'r') as f:
    reqs = f.read().splitlines()

setup(
    name='cfb-p',
    url='https://github.com/butomo1989/cfb',
    description='Sample CLI written in Python',
    author='Budi Utomo',
    author_email='budi.ut.1989@gmail.com',
    install_requires=reqs,
    py_modules=['cli', 'utils'],
    entry_points={'console_scripts': 'cfb-p=cfb.cli:cli'}
)
