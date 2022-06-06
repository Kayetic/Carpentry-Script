import time
import requests

# Function to add a user to the customers file
def addingCustomer(data_to_add):
    with open("customers.txt", "a+") as file_object:
        file_object.seek(0)
        data = file_object.read(100)
        if len(data) > 0 :
            file_object.write("\n")
        file_object.write(data_to_add)
        file_object.close()

customers = []
firstNames = []
lastNames = []
phones = []
towns = []
quotes = []

try:
    # Temporarily store the contents of customers file into a variable for easier use later
    tempCustomers = open("customers.txt", "a+", encoding="utf-8").readlines()
except FileNotFoundError:
    print("Customer file not found! Please add a customer (1st choice on the main menu).")
for element in tempCustomers:
    customers.append(element.strip())
# Separate each field in the customer text file into separate variables and append them to individual lists
for iteration, allDetails in enumerate(customers):
    try:
        firstName, lastName, phone, town, quote = allDetails.split(", ")
        firstNames.append(firstName)
        lastNames.append(lastName)
        phones.append(phone)
        towns.append(town)
        quotes.append(quote)
    except ValueError:
        print(f"\033[1mERROR:\033[0m Invalid customer file syntax detected at line: \033[1m{int(iteration) + 1}\033[0m of customers.txt file")

### Main menu ###
while True:
    choice = input("Enter 'new' to enter a new customer's details, and subsequently generate a quote\nEnter 'display' to display stored customer details\nEnter 'delete' to remove details\nEnter 'exit' to quit\n>>> ")
    if choice == "new":
        # Entering user details
        first_name = input("Enter the customer's first name: ").title()
        last_name = input("Enter the customer's last name: ").title()
        telephone = input("Enter the customer's telephone number: ")
        if (len(telephone) > 13) or (len(telephone) < 11):
            print("\n\033[1mERROR:\033[0m Invalid telephone number")
            continue
        else:
            telephone = str(telephone)
        try:
            int(telephone)
        except ValueError or TypeError:
            print("Incorrect phone number, try again")
            continue
        town = input("Enter the user's town: ").title()

        data_to_add = first_name + ", " + last_name + ", " + telephone + ", " + town
        print(f"Saving to file: {data_to_add}")
        print(f"\nNow you should create a quote for: {first_name} {last_name}")
        length = float(input("Enter the length of the carpet: "))
        try :
            int(length)
        except ValueError or TypeError:
            print("Incorrect length, try again")
            continue
        if length == 0:
            print("\n\033[1mERROR:\033[0m Invalid length")
            continue
        if length > 10000:
            print("\n\033[1mERROR:\033[0m Length must be less than 10,000")
            continue
        if length < 0.1:
            print("\n\033[1mERROR:\033[0m Length must be greater than 0.1m")
            continue

        width = float(input("Enter the width of the carpet: "))
        if width == 0:
            print("\n\033[1mERROR:\033[0m Invalid width")
            continue
        if width > 10000:
            print("\n\033[1mERROR:\033[0m Width must be less than 10,000")
            continue
        if width < 0.1:
            print("\n\033[1mERROR:\033[0m Width must be greater than 0.1m")
            continue
        carpet_area = length * width
        underlay_area = carpet_area
        gripper_length = (2*length + 2*width)

        price_carpet = carpet_area * 22.5
        price_gripper = gripper_length * 1.1
        underlay_choice = input("Choose which underlay you want:\nEnter 1 for First Step\nEnter 2 for Monarch\nEnter 3 for Royal\n>>> ")
        if underlay_choice == "1":
            underlay_price = carpet_area * 5.99
        elif underlay_choice == "2":
            underlay_price = carpet_area * 7.99
        elif underlay_choice == "3":
            underlay_price = carpet_area * 60
        else:
            print("Incorrect choice")
            continue
        temp_total_price = price_carpet + price_gripper + underlay_price
        total_price = round(temp_total_price, 2)
        data_to_add_with_quote = first_name + ", " + last_name + ", " + telephone + ", " + town + ", " + str(total_price)
        addingCustomer(data_to_add_with_quote)
        # Save this amount to the customers file
        quotes = []
        print(f"Saved: {first_name} {last_name} with a quote of £{total_price}")
        break
    elif choice == "display":
        while True:
            print("Stored customers:")
            for iteration_over_people, person in enumerate(range(len(lastNames))):
                print(f"{iteration_over_people + 1}: {lastNames[person]}, {firstNames[person]}")
            choose_person = input("Choose the number of the person you would like to look-up details on (or do 'exit' to quit)\n>>> ")
            if choose_person == "exit":
                break
            time.sleep(0.15)
            choose_person = int(choose_person) - 1
            try:
                print(f"Details on: \033[1m{firstNames[choose_person]} {lastNames[choose_person]}\033[0m\n\033[1mPhone\033[0m: {phones[choose_person]}\n\033[1mTown\033[0m: {towns[choose_person]}\n\033[1mQuote\033[0m: £{quotes[choose_person]}\n")
            except IndexError:
                print(f"The number: {choose_person} is not an option, try again.\n")
    elif choice  == "exit":
        print("Exiting...")
        exit(0)
    elif choice == "delete":
        for i in range(len(firstNames)):
            print(f"{i}: {firstNames[i]} {lastNames[i]}")
exit(0)
