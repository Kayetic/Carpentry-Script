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
