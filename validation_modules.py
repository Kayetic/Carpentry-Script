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