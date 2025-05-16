"""
File: utils_branton_advanced.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Advanced: This version requires a working .venv with loguru and pyttsx3 installed.
It includes a function to read the byline aloud using pyttsx3.

Author: Branton Dawson

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# Learn more: https://docs.python.org/3/library/

import statistics 

# Import packages from requirements.txt
# Learn more: https://pypi.org/project/loguru/ 
# Learn more:  https://pypi.org/project/pyttsx3/
import loguru   # Easy logging
import pyttsx3  # Text-to-speech engine

#####################################
# Configure Logger and Verify
#####################################

logger = loguru.logger
logger.add("project.log", level="INFO", rotation="100 KB") 
logger.info("Logger loaded.")

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
# Add another or replace this with your own boolean variable
has_international_clients: bool = True
located_in_usa: bool = False

# declare an integer variable 
# Add or replace this with your own integer variable
years_in_operation: int = 10
number_of_students: int = 425

# declare a floating point variable
# Add or replace this with your own floating point variable
average_client_satisfaction: float = 4.7
average_grade_point: float = 3.8

# declare a list of strings
# Add or replace this with your own list  
skills_offered: list = ["Data Analysis", "Machine Learning", "Business Intelligence"]
choice_in_analytics: list = ["Data Science", "Data Engineering", "Business Analytics"]

# declare a list of numbers so we can illustrate statistics skills
# Add or replace this with your own numeric list  
client_satisfaction_scores: list = [4.8, 4.6, 4.9, 5.0, 4.7]
student_grades: list = [3.9, 4.0, 3.7, 3.8, 4.0]

# Calculate basic statistics using built-in Python functions and the statistics module
# Replace these variable names with the variable name of your own numeric list
min_grade: float = min(student_grades)
max_grade: float = max(student_grades)
mean_grade: float = statistics.mean(student_grades)
stdev_grade: float = statistics.stdev(student_grades)
min_score: float = min(client_satisfaction_scores)  
max_score: float = max(client_satisfaction_scores)  
mean_score: float = statistics.mean(client_satisfaction_scores)  
stdev_score: float = statistics.stdev(client_satisfaction_scores)

# Use a Python formatted string (f-string) to show information
# Modify the text in the byline to fit your information
# Modify the variables in the byline to use your variable names
byline: str = f"""
---------------------------------------------------------
Stellar Analytics: Delivering Professional Insights
---------------------------------------------------------
Has International Clients:  {has_international_clients}
Located in USA:            {located_in_usa}
Choice in Analytics:     {choice_in_analytics}
Average Client Satisfaction: {average_client_satisfaction}
Average Grade Point:      {average_grade_point}
Number of Students:       {number_of_students}
Average Student Grade:   {mean_grade:.2f}
Minimum Student Grade:   {min_grade}
Maximum Student Grade:   {max_grade}
Standard Deviation of Student Grades: {stdev_grade:.2f}
Years in Operation:         {years_in_operation}
Skills Offered:             {skills_offered}
Client Satisfaction Scores: {client_satisfaction_scores}
Minimum Satisfaction Score: {min_score}
Maximum Satisfaction Score: {max_score}
Mean Satisfaction Score: {mean_score:.2f}
Standard Deviation of Satisfaction Scores: {stdev_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline


# Read the byline aloud (requires pyttsx3)

def read_byline_aloud():
    engine = pyttsx3.init()
    engine.say(get_byline())
    engine.runAndWait()


#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_branton_advanced.py")
    loguru.logger.info("START main() in utils_branton_advanced.py")

    print(get_byline())
    loguru.logger.info("Byline:\n" + get_byline())

    # Uncomment to hear it read aloud:
    read_byline_aloud()

    print("END main() in utils_branton_advanced.py")
    loguru.logger.info("END main() in utils_branton_advanced.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()
