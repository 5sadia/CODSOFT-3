import random
import string

def gen_password(length):
    character = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(character) for i in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
        if length <= 0:
            print("Length must be a positive integer.")
            return
        password = gen_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid integer for the length.")

if __name__ == "__main__":
    main()
