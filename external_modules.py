import csv
from os.path import exists

def validate_phone(phone):
    if len(phone) == 11 and phone.isdigit():
        return True
    else:
        return False

def validate_town(town):
    if (len(town) > 0) and town.isalpha():
        return True
    else:
        return False

def validate_first_name(name):
    if (len(name) > 0) and name.isalpha():
        return True
    else:
        return False

def validate_last_name(name):
    if (len(name) > 0) and name.isalpha():
        return True
    else:
        return False


def append_to_file(filename, data_to_write):
    """
    Appending a line to the end of a file
    Parameters: filename (string) - the name of the file to be read
                data_to_write (string) - the line to be appended to the file
    """
    with open(filename, "a+", encoding='utf-8') as file_object:
        file_object.seek(0)
        reading_data = file_object.read(100)
        if len(reading_data) > 0 :
            file_object.write("\n")
        file_object.write(data_to_write)
        file_object.close()

def writing_data_csv(filename, data_to_write):
    """
    Function to write data to csv file
    Parameters: filename (string) - the name of the file to be read
                data_to_write (string) - the data to be written (or appended) to the file
    """
    file_exists = exists(filename)
    if file_exists is False:
        header = ['first_name', 'last_name', 'telephone', 'town']
        with open(filename, 'w+', newline="", encoding='utf-8') as writing_file:
            csvwriter1 = csv.writer(writing_file) # 1. create a csvwriter object
            csvwriter1.writerow(header) # 2. write the header
            csvwriter1.writerow(data_to_write) # 3. write the rest of the data
            writing_file.close() # 4. close the file
    else:
        with open(filename, 'a', newline="", encoding='utf-8') as appending_file:
            csvwriter2 = csv.writer(appending_file) # 1. create a csvwriter object
            csvwriter2.writerow(data_to_write) # 2. write the row, without the header
            appending_file.close() # 3. close the file

def reading_data_csv(filename):
    """
    Reads the data from the csv file and returns a header and a list of rows (both as lists)
    Parameters: filename (string) - the name of the file to be read
    """
    with open(filename, 'r', encoding='utf-8') as read_file:
        content = read_file.readlines()
    read_header = content[:1]
    read_rows = content[1:]
    read_file.close()
    read_header[-1] = read_header[-1].strip()
    for i in range(len(read_rows)):
        read_rows[i] = read_rows[i].strip()
    return read_header, read_rows

def validate_choice(choice_to_validate, number_of_choices):
    """
    Function to validate a choice by trying to convert it to an integer to see if its a number
    Parameters: choice_to_validate (string) - the choice to be validated
                number_of_choices (int) - the number of choices available
    """
    try:
        int(choice_to_validate)
        if (int(choice_to_validate) > number_of_choices) or (int(choice_to_validate) < 1):
            return False
        else:
            return True
    except ValueError:
        return False
        
def validate_length_or_width(length_or_width):
    """
    Function to validate a length or width by trying to convert it to an integer to see if its a number
    Parameters: length_or_width (string) - the length or width to be validated
    """
    try:
        int(length_or_width)
        if int(length_or_width) < 0:
            print("\n\033[1mERROR:\033[0m The length or width cannot be negative")
            return False
        if int(length_or_width) > 10000:
            print("\n\033[1mERROR:\033[0m The length or width cannot be greater than 10000")
            return False
        if int(length_or_width) < 0.1:
            print("\n\033[1mERROR:\033[0m The length or width cannot be less than 0.1")
            return False
    except ValueError:
        print("\n\033[1mERROR:\033[0m The length and width must be numbers")
        return False
    return True
    