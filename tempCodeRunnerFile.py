import random 
password = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890abcdefghijklmnopqrstuvwxyz!@#$%^&*():?{}"
length_password = int(input("enter the length of the password : "))
a = "".join(random.sample(password,length_password))
print(f"Your password is {a}")