import random
 
print("Welcome to Your Password Generator")
 
chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()[]:;"<>,./?|'
 
number = int(input("Amount of Password To generate:"))
 
Length =int(input("Enter Length Of your Passsword:"))
  
print('Here are Your Passwords:')
 
for pwd in range(number):
     Passwords=''
     for c in range(Length):
         Passwords += random.choice(chars) 
     print(Passwords)  