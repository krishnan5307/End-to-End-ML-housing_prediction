from setuptools import setup,find_packages
from typing import List

#Declaring variables for setup functions
PROJECT_NAME="housing-predictor"
VERSION="0.0.2"                         ## this version of package will get installed using "-e ." through requirements.txt file run
AUTHOR="krishnanunni"
DESRCIPTION="This is a first FSDS Nov batch Machine Learning Project"
REQUIREMENT_FILE_NAME="requirements.txt"

HYPHEN_E_DOT = "-e ."


def get_requirements_list() -> List[str]:

    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file

    ## -e . will install all libraries wherever  __init__ is preesent other than requiremets.txt 
                                                            ## we remove -e . in setup.py because we used find_packages() funtion below which will return -
                                                            #- all our packages names in list format
                                                            ## both find_packages() and -e . does the same thing  
    """

    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list
    


setup(
name=PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESRCIPTION,
packages=find_packages(),                     ## our own custom libraries or Returns all packages where there is __init__.py is present  
install_requires=get_requirements_list()         ## for external linraries
)














"""



PROJECT_NAME= "housing-prediction"
VERSION = "0.0.2"             
AUTHOR = "Krishnanunni"
DESCRIPTION = "This is first FSDS ML project"
PACKAGES = ["housing"]    
REQUIREMENTS_FILE_NAME= "requirements.txt"




def get_requirements_list()->List[str]:

   
    Description: this function is going to return list of requirement
    mention in requirements.txt file

    return this function is going to return a list which contain name of
    libraries mentioned in requirements.txt file

     with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

   
    
    with open(REQUIREMENTS_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove('-e .') 
    

    
   

setup(

name= PROJECT_NAME,
version= VERSION,
author= AUTHOR,
description= DESCRIPTION,
packages= find_packages(),                 
install_requires= get_requirements_list(),  

)




if __name__=="__main__":
    print(get_requirements_list())

    
    
"""