from setuptools import setup
from typing import List




## DECLARING VARIABLES FOR SETUP FUNCTION
PROJECT_NAME= "housing-prediction"
VERSION = "0.0.1"
AUTHOR = "Krishnanunni"
DESCRIPTION = "This is first FSDS ML project"
PACKAGES = ["housing"]     ## specify folder name in packages
REQUIREMENTS_FILE_NAME= "requirements.txt"

def get_requirements_list()->List[str]:

    """
    Description: this function is going to return list of requirement
    mention in requirements.txt file

    return this function is going to return a list which contain name of
    libraries mentioned in requirements.txt file

    """

    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines()



setup(

name= PROJECT_NAME,
version= VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages= PACKAGES,
install_requires= get_requirements_list()

)




if __name__=="__main__":
    print(get_requirements_list())