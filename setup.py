from setuptools import find_packages, setup
from typing import List


def get_requirements(file_path:str) ->List[str]:
    requirements = []
    with open(file_path) as file_obj:
        requirements= file_obj.readlines()
        requirements= [req.replace("\n","") for req in requirements]
        return requirements

setup(
    name = 'Fault Detection',
    version='0.0.1',
    author='vinay',
    author_email='vinayiet435@gmail.com',
    install_requirements=('requirements.txt'),
    packages=find_packages()
)