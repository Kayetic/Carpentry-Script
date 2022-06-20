import csv
from os.path import exists

data_to_write = []

while True:
    temp_array = []
    first_name = input("Enter the customer's first name: ").title()
    last_name = input("Enter the customer's last name: ").title()
    telephone = input("Enter the customer's phone number: ")
    town = input("Enter the customer's town: ").title()
    temp_array.append(first_name)
    temp_array.append(last_name)
    temp_array.append(telephone)
    temp_array.append(town)
    print(temp_array)
    data_to_write.append(temp_array)
    print(f"Data to write: {data_to_write}")
    to_continue = input("\nDo you want to continue? (y/n): ").title()
    if to_continue == "N":
        break


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
            csvwriter1.writerows(data_to_write) # 3. write the rest of the data
            writing_file.close() # 4. close the file
    else:
        with open(filename, 'a', newline="", encoding='utf-8') as appending_file:
            csvwriter2 = csv.writer(appending_file) # 1. create a csvwriter object
            csvwriter2.writerows(data_to_write) # 2. write the rows, without the header
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
    return read_header, read_rows
