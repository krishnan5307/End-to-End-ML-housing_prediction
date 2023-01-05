import os
import sys

class HousingException(Exception):

    def __init__(self, error_message:Exception, error_detail:sys):   ## creating object of exception as error messgage and sys module as error detail
        super().__init__(error_message)   ### or Exception(error_message)     
                                          ## super() means to parent class we are passing informaion error message
        self.error_message = error_message           

    @staticmethod          ## no object of class is needed , we can call funtion belw using class name.funct name
    def get_detailed_error_message(error_message:Exception, error_detail:sys)-> str:   ## this function is going to return a string

        """
        error message : Exception object
        error detail : object of sys module 
             
        """
        _,_, exec_tb = error_detail.exc_info()  ##  exc_info return excption info about error details in 3 tuples params --> (type,value,traceback)
                  ## we are skipping the frst two info typ and value, that s why we left blank but we want trace back in varivble exec_tb
                   ## from tackeback we extract line number and file name
        file_name = exec_tb.tb_frame.f_code.co_filename
        line_number = exec_tb.tb_frame.f_lineno

        error_message = f"Error occured in script :[{file_name}] at line number [{line_number}] error message :[{error_message}]"
        return error_message


    def __str__(self):          ## this str() returns the string when we give print statment for the class() 
        return self.error_message

    def __repr__(self) -> str:  ## this repr() will return something if obhject of calss is called
        return HousingException.__name__.__str()





