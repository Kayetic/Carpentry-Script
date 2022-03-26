# Function to add a user to the players file
def addingCustomer(data_to_add):
    with open("customers.txt", "a+") as file_object:
      # Move read cursor to the start of file.
      file_object.seek(0)
      # If file is not empty then append '\n'
      data = file_object.read(100)
      if len(data) > 0 :
          file_object.write("\n")
      # Append text at the end of file
      file_object.write(data_to_add)
      file_object.close()