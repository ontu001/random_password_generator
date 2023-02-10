import random
import string

def generate_password(length):
    password = ''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for i in range(length))
    return password

password_length = int(input("Enter the password length: "))
password = generate_password(password_length)
print("Generated password: ", password)