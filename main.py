# Main menu
while True:
    choice = input("""
Enter 'details' to enter a user's details
Enter 'quote' to make a new quote
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
    elif choice  == "exit":
        print("Exiting...")
        exit(0)

exit(0)
