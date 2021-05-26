# ------------------------------------------------- #
# Title: Assignment07
# Description: Example of storing data in a binary file with Error Handling
# ChangeLog: (Who, When, What)
#  CTUNG,<5.25.2021>,Created Scripted to read in pickle file AppData.dat
#  CTUNG,<5.25.2021>,Created function save_data_to_file() to save data to AppData.dat
#  CTUNG,<5.25.2021>,Created function read_data_from_file() read data tp AppData.dat
#  CTUNG,<5.25.2021>,Added Error Handling to read_data_from_file()
#  CTUNG,<5.25.2021>,Added user input for lstCustomer and intID with error handling
#  CTUNG,<5.25.2021>,Added data to be appended to list lstCustomer[]
# ------------------------------------------------- #
import pickle  # This imports code from another code file!
import os.path # This imports code used to check if file exists

# Data -------------------------------------------- #
strFileName = 'AppData.dat'
lstCustomer = []

# Processing -------------------------------------- #
def save_data_to_file(file_name, list_of_data):
    """ saves pickle file
    :param file_name: (string) file name of pickle file
    :param list_of_data: (list) list of data
    :return: none
    """
    file = open(file_name, "wb")
    pickle.dump(list_of_data, file)
    file.close()

def read_data_from_file(file_name):
    """Reopen and unpickle the pickled content and read to obj
    :param file_name: (string) with name of the pikcle file
    :return: list of data
    """
    try:
        with open(file_name, "rb") as f:
            list_of_data = pickle.load(f)
            print(list_of_data)
        f.close()
        return list_of_data
    except FileNotFoundError as e:
        print("The pickle file must exist before running this script!")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
        quit()
    except Exception as e:
        print("There was a non-specific error!")
        print("Built-In Python error info: ")
        print(e, e.__doc__, type(e), sep='\n')
        quit()

# Presentation ------------------------------------ #
if os.path.exists(strFileName):
    print("Pickle Data File Exists!")
    # Checks if file exists and reads in data
    lstCustomer = read_data_from_file(strFileName)
else:
    print("Pickle File Does Not Exists!")
    print("Pickle File Will be Created!")

try:
    intID = int(input("Enter an Id: "))
except ValueError as e:
    print("The input must be a number!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
    quit()

try:
    strName = str(input("Enter a Name: "))
except Exception as e:
    print("There was a non-specific error!")
    print("Built-In Python error info: ")
    print(e, e.__doc__, type(e), sep='\n')
    quit()

# Appends New Data to Existing List
lstCustomer.append(intID)
lstCustomer.append(strName)

# Store the list object into a binary file
save_data_to_file(strFileName, lstCustomer)

# Read the data from the file into a new list object and display the contents
read_data_from_file(strFileName)