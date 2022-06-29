from signal import signal, SIGINT
from rich.console import Console
import time, external_modules, platform

console = Console()

def handler(signal_received, frame):
    # Handling any cleanup here
    print('\nCTRL-C or SIGINT detected. Exiting gracefully...')
    exit(0)

customers = []
firstNames = []
lastNames = []
phones = []
towns = []
quotes = []

### Main menu ###
while True:
    signal(SIGINT, handler)
    # os.system("cls") if 'Windows' in platform.system() else os.system("clear")
    console.print("Main Menu:", style="bold underline green") 
    choice = input("""
Enter '\033[1mnew\033[0m' to enter a new customer's details, and subsequently generate a quote
Enter '\033[1mdisplay\033[0m' to display stored customer details
Enter '\033[1mdelete\033[0m' to remove details
Enter '\033[1mexit\033[0m' to quit
>>> """)
    print(choice)
    if choice == "new":
        # Entering user details
        temp_details = []
        # os.system("cls") if 'Windows' in platform.system() else os.system("clear")
        first_name = input("Enter the customer's first name: ").title()
        if external_modules.validate_first_name(first_name) is False:
            print("\n\033[1mERROR:\033[0m Invalid first name")
            time.sleep(1)
            continue
        else:
            temp_details.append(first_name)
        last_name = input("Enter the customer's last name: ").title()
        if external_modules.validate_last_name(last_name) is False:
            print("\n\033[1mERROR:\033[0m Invalid last name")
            time.sleep(1)
            continue
        if last_name.isalpha() is False:
            print("\n\033[1mERROR:\033[0m Last name must be alphabetical")
            time.sleep(1)
            continue
        temp_details.append(last_name)
        telephone = input("Enter the customer's telephone number: ")
        if external_modules.validate_phone(telephone) is False:
            print("\n\033[1mERROR:\033[0m Invalid phone number entered. Please try again.")
            time.sleep(1)
            continue
        else:
            temp_details.append(telephone)
        town = input("Enter the user's town: ").title()
        if external_modules.validate_town(town) is False:
            print("\n\033[1mERROR:\033[0m Invalid town name entered. Please try again.")
            time.sleep(1)
            continue
        else:
            temp_details.append(town)
        print(f"Saving to file: {temp_details}")
        print(f"\nNow you should create a quote for: {first_name} {last_name}")
        length = float(input("Enter the length of the carpet: "))
        try :
            int(length)
        except ValueError:
            print("Incorrect length, try again")
            continue
        except TypeError:
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
        TOTAL_PRICE = str(round(temp_total_price, 2))
        temp_details.append(TOTAL_PRICE)
        data_to_add_with_quote = temp_details
        # Saving this amount to the text file
        print(temp_details)
        print(data_to_add_with_quote)
        print(type(data_to_add_with_quote))
        external_modules.writing_data_csv('customers.csv', data_to_add_with_quote)
        print(f"Save{first_name} {last_name} with a quote of £{TOTAL_PRICE}")
        break
    elif choice == "display":
        print('WORKING')
        file_headers, file_rows = external_modules.reading_data_csv('data.csv')
        print(file_headers)
        print(type(file_headers))
        print('')
        print(file_rows)
        print(type(file_rows))
    elif choice  == "exit":
        print("Exiting...")
        exit(0)
    elif choice == "delete":
        print("\nNot yet implemented")
exit(0)
