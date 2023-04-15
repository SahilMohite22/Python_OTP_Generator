import random
generator_otp = random.randint(000000, 999999)
username = input("Username: ")
print("Hello...."+username)
print("Here is your otp for login : ", generator_otp)
password = input("Enter the otp for login : ")
if password == str(generator_otp):
    print('Login Success')
else:
    print("Please enter a valid otp 😡")
