import time, externalModules

# Main menu
while True:
    choice = input("""
Enter 'details' to enter a customer's details
Enter 'quote' to add a new quote
Enter 'display' to display stored customer details
Enter 'exit' to quit

>>> """)
    if choice == "details":
        # Entering user details
        first_name = input("Enter the customer's first name: ").title()
        last_name = input("Enter the customer's last name: ").title()
        telephone = input("Enter the customer's telephone number: ")
        try:
            int(telephone)
        except (TypeError or ValueError):
            print("Incorrect phone number, try again")
            exit(0)
        town = input("Enter the user's town: ").title()

        data_to_add = first_name + ", " + last_name + ", " + telephone + ", " + town
        print(data_to_add)
        externalModules.addingCustomer(data_to_add)
    elif choice == "quote":
        length = float(input("Enter the length of the carpet: "))
        width = float(input("Enter the width of the carpet: "))
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
        
        print(temp_total_price)
        break
    elif choice == "display":
        customers = []
        firstNames = []
        lastNames = []
        phones = []
        towns = []
        try:
            # Temporarily store the contents of customers file into a variable for easier use later
            tempCustomers = open("customers.txt", encoding="utf-8").readlines()
        except FileNotFoundError:
            print("Customer file not found! Please add a customer (1st choice on the main menu).")
        for element in tempCustomers:
            customers.append(element.strip())
        # Separate each field in the customer text file into separate variables and append them to individual lists
        for iteration, allDetails in enumerate(customers):
            try:
                firstName, lastName, phone, town = allDetails.split(", ")
                firstNames.append(firstName)
                lastNames.append(lastName)
                phones.append(phone)
                towns.append(town)            
            except ValueError:
                print(f"\033[1mERROR:\033[0m Invalid customer file syntax detected at line: \033[1m{int(iteration) + 1}\033[0m of customers.txt file")
        # print(f"first names = {firstNames}")
        # print(f"last names = {lastNames}")
        # print(f"phones = {phones}")
        # print(f"towns = {towns}")
        while True:
            for iteration_over_people, person in enumerate(range(len(lastNames))):
                print(f"{iteration_over_people + 1}: {lastNames[person]}, {firstNames[person]}")
            choose_person = int(input("Choose the number of the person you would like to look-up details on\n>>> ")) - 1
            time.sleep(0.15)
            print(f"Details on: \033[1m{firstNames[choose_person]} {lastNames[choose_person]}\033[0m\n\033[1mPhone\033[0m: {phones[choose_person]}\n\033[1mTown\033[0m: {towns[choose_person]}\n")
    elif choice  == "exit":
        print("Exiting...")
        exit(0)

exit(0)