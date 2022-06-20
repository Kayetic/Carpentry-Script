import csv
from os.path import exists

# data_to_write = []

# while True:
#     temp_array = []
#     first_name = input("Enter the customer's first name: ").title()
#     last_name = input("Enter the customer's last name: ").title()
#     telephone = input("Enter the customer's phone number: ")
#     town = input("Enter the customer's town: ").title()
#     temp_array.append(first_name)
#     temp_array.append(last_name)
#     temp_array.append(telephone)
#     temp_array.append(town)
#     print(temp_array)
#     data_to_write.append(temp_array)
#     print(f"Data to write: {data_to_write}")
#     to_continue = input("\nDo you want to continue? (y/n): ").title()
#     if to_continue == "N":
#         break



# file_exists = exists('data.csv')
# if file_exists is False:
#     header = ['first_name', 'last_name', 'telephone', 'town']
#     with open('data.csv', 'w+', newline="", encoding='utf-8') as writing_file:
#         csvwriter1 = csv.writer(writing_file) # 2. create a csvwriter object
#         csvwriter1.writerow(header) # 4. write the header
#         csvwriter1.writerows(data_to_write) # 5. write the rest of the data
#         writing_file.close()
# else:
#     with open('data.csv', 'a', newline="", encoding='utf-8') as appending_file:
#         csvwriter2 = csv.writer(appending_file)
#         csvwriter2.writerows(data_to_write)
#         appending_file.close()


def reading_data():
    """
    Reads the data from the csv file and returns it as a list of lists.
    """
    with open('data.csv', 'r', encoding='utf-8') as read_file:
        content = read_file.readlines()
    read_header = content[:1]
    read_rows = content[1:]
    read_file.close()
    return read_header, read_rows
