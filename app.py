# ask user if they want to generate password
def main():
    option = char(input("Do you want to generate password?\ny/n: ")).lower()

    # if yes, get password length
    if option == 'y':
        password_len = input("Enter length of password: ")

# grenerate password

# print password

# if initial response is no, then exit program