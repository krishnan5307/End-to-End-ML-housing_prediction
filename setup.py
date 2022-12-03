from setuptools import setup, find_packages
from typing import List




## DECLARING VARIABLES FOR SETUP FUNCTION
PROJECT_NAME= "housing-prediction"
VERSION = "0.0.1"            ## this version of package will get installed using "-e ." through requirements.txt file run 
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
        return requirement_file.readlines().remove("-e .")  ## -e . will install all libraries wherever  __init__ is preesent other than requiremets.txt 
                                                            ## we remove -e . in setup.py because we used find_packages() funtion below which will return -
                                                            #- all our packages names in list format
                                                            ## both find_packages() and -e . does the same thing

setup(

name= PROJECT_NAME,
version= VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages= find_packages,                  ## our own custom libraries or Returns all packages where there is __init__.py is present  
install_requires= get_requirements_list()   ## for external linraries

)




if __name__=="__main__":
    print(get_requirements_list())