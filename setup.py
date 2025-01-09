from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = '-e .'

def get_requirements(file_path: str) -> List[str]:
    '''
    This function will return a list of requirements
    '''
    requirements = []
    try:
        with open(file_path, 'r') as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]  # Remove extra whitespace or line breaks
            
            if HYPEN_E_DOT in requirements:
                requirements.remove(HYPEN_E_DOT)
    except FileNotFoundError:
        print(f"Error: {file_path} not found. Please ensure the file exists.")
    
    return requirements

setup(
    name='mlprojects',
    version='0.0.1',
    author='Adeel Khan',
    author_email='reveliio123@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)

