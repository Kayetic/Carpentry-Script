import csv
from os.path import exists

header = ['first_name', 'last_name', 'telephone', 'town']
file_exists = exists('data.csv')
if file_exists is False:
    print("\n\033[1mCreating file\033[0m")
    with open('data.csv', 'w+') as file:
        csv.writer.writerow(header)
        file.close()


array = []
data_to_write = []

while True:
    first_name = input("Enter the customer's first name: ").title()
    last_name = input("Enter the customer's last name: ").title()
    telephone = input("Enter the customer's phone number: ")
    town = input("Enter the customer's town: ").title()
    
    data_to_write.append(first_name)
    data_to_write.append(last_name)
    data_to_write.append(telephone)
    data_to_write.append(town)
    array.append(data_to_write)
    to_continue = input("\nDo you want to continue? (y/n): ").title()
    if to_continue == "N":
        break


print(array)