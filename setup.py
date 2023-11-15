from setuptools import find_packages,setup
from typing import List
HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
        This function will return the lsit of requirements
    
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        for i in range(len(requirements)):
            requirements[i] = requirements[i].replace('\n', '')
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements
setup(

name='mental_health',
version='3.9.13',
author='Meher',
author_email='meher09@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')
)