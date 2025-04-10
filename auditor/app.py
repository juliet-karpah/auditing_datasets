"""
Module that validates the flight school's records.

This is the primary module that does all of the work. It loads the files, loops through
the lessons, and searches for any takeoffs that violate insurance requirements.

Technically, we could have put many of these functions in __main__.py.  That is the
main module of this application anyway.  However, for testing purposes we want all
functions in modules and we only want script code in the file __main__.py

Author: Juliet George
Date: April 8th, 2025
"""
import utils
import tests
import os.path
import violations

# Uncomment for the extra credit
#import endorsements
#import inspections


def discover_violations(directory,output):
    """
    Searches the dataset directory for any flight lessons the violation regulations.
    
    This function will call list_weather_violations() to get the list of weather violations.
    If list_endorsment_violations (optional) is completed, it will call that too, as
    well as list_inspection_violations.  It will concatenate all of these 2d lists
    into a single 2d list of violations (so a flight may be listed more than once for
    each of the three types of violations).
    
    If the parameter output is not None, it will create the CSV file with name output
    and write the 2d list of violations to this file.  This CSV file should have the
    following header:
    
        STUDENT,AIRPLANE,INSTRUCTOR,TAKEOFF,LANDING,FILED,AREA,REASON
    
    Regardless of whether output is None, this function will print out the number of
    violations, as follows:
    
        '23 violations found.'
    
    If no violations are found, it will say
    
        'No violations found.'
    
    Parameter directory: The directory of files to audit
    Precondition: directory is the name of a directory containing the files 'daycycle.json',
    'weather.json', 'minimums.csv', 'students.csv', 'teachers.csv', 'lessons.csv',
    'fleet.csv', and 'repairs.csv'.
    
    Parameter output: The CSV file to store the results
    Precondition: output is None or a string that is a valid file name
    """
    current = [['STUDENT', 'AIRPLANE', 'INSTRUCTOR', 'TAKEOFF', 'LANDING', 'FILED', 'AREA', 'REASON']]
    current += violations.list_weather_violations(directory)
   
    if output:
        utils.write_csv(current, output)

    number_of_violations = len(current)-1
    if number_of_violations > 0:
        if number_of_violations == 1:
            print(f"{number_of_violations} violation found.")
        else:
            print(f"{number_of_violations} violations found.")
    else:
        print("No violations found.")



def execute(args):
    """
    Executes the application or prints an error message if executed incorrectly.
    
    The arguments to the application (EXCLUDING the application name) are provided to
    the list args. This list should contain either 1 or 2 elements.  If there is one
    element, it should be the name of the data set folder or the value '--test'.  If
    there are two elements, the first should be the data set folder and the second
    should be the name of a CSV file (for output of the results).
    
    If the user calls this script incorrectly (with the wrong number of arguments), this
    function prints:
    
        Usage: python auditor dataset [output.csv]
    
    This function does not do much error checking beyond counting the number of arguments.
    
    Parameter args: The command line arguments for the application (minus the application name)
    Precondition: args is a list of strings
    """

    #     # Quit if wrong number of arguments
    # if len(args) != 1:
    #     print('Usage: python to_celsius number')
    # elif args[0] == '--test':
    #     test.test_to_celsius()
    # else:
    #     try:
    #         # Prepare to crash if user gives a non-number
    #         value = float(args[0])
    #         result = temp.to_celsius(value)
    #         print(result)
    #     except:
    #         print('Usage: python to_celsius number')
    if len(args) < 1 or len(args) > 2:
        print('Usage: python auditor dataset [output.csv]')
    elif len(args) == 1:
        if args[0] == "--test":
            tests.test_all()
        elif os.path.isdir(args[0]):
            discover_violations(args[0])
    elif len(args) == 2:
        data_folder = args[0]
        csv_file = args[1]
        if os.path.isdir(data_folder) and (csv_file and csv_file.lower().endswith(".csv")):
            discover_violations(data_folder, csv_file)
        elif os.path.isdir(data_folder) and not csv_file:
            discover_violations(data_folder, None)
        else:
            print('Usage: python auditor dataset [output.csv]')



  

    

