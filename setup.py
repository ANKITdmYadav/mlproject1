from setuptools import find_packages,setup
from typing import List


HYPEN_E_DOT ='-e .'
def get_requirement(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        # readline also puts a /n at end so
        requirements=[req.replace("\n","") for req in requirements]

        # -e . also come from requirements.txt so remove this also
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    
    return requirements

# kind of metadata
setup(
name='mlproject',
version='0.0.1',
author='krish',
author_email='krishnaik06@gmail.com',
packages=find_packages(),
# install_requires=['pandas','numpy','seaborn'],
install_requires=get_requirement('requirements.txt')
)