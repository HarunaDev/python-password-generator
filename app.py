import random
import string

# ask user if they want to generate password
def main():
    option = str(input("Do you want to generate password?\ny/n: ")).lower()

    # if yes, get password length
    if option == str('y'):
        password_len = input("Enter length of password: ")

        # define character set to use
        chars = string.ascii_letters + string.digits + string.punctuation
        
        # grenerate password
        password = ''.join(random.choice(chars) for i in range(int(password_len)))


        # print password
        print(f"Your random password is {password}")

    # if initial response is no, then exit program
    elif option == str('y'):
        quit()

main()