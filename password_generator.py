import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 for a good mix of characters.")
        return None

    letters = string.ascii_letters   # a-z, A-Z
    digits = string.digits           # 0-9
    symbols = string.punctuation     # !@#$%^&* etc.

    all_characters = letters + digits + symbols

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    try:
        length = int(input("Enter desired password length: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    password = generate_password(length)

    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
