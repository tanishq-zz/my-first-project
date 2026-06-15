import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    letters = string.ascii_letters
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""

    all_characters = letters + digits + special

    if not all_characters:
        return "Error: No character types selected!"

    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password

def main():
    print("=== Password Generator ===")

    while True:
        try:
            length = int(input("\nEnter password length (default 12): ") or 12)
        except ValueError:
            print("Please enter a valid number.")
            continue

        use_digits = input("Include digits? (y/n, default y): ").lower() != 'n'
        use_special = input("Include special characters? (y/n, default y): ").lower() != 'n'

        password = generate_password(length, use_digits, use_special)
        print(f"\nGenerated Password: {password}")

        again = input("\nGenerate another? (y/n): ").lower()
        if again != 'y':
            break

    print("\nThanks for using Password Generator!")

if __name__ == "__main__":
    main()
