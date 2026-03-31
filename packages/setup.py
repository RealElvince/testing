from setuptools import setup,find_packages

setup(
    name='packages',
    version='0.1',
    packages=find_packages(exclude['test']),
    license='MIT',
    description='python packages',
    long_description=open('README.md').read(),
    install_requires=['numpy'],
    url='https://github.com/RealElvince/testing',
    author='Elvince',
    author_email="elvinceoduor76@gmail.com"


)