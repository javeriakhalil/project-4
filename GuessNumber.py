import random
 
def guess (x):
     random_number=random.randint(1, x)
     guess=0
     
     while guess != random_number:
         guess=int(input(f'Enter a number between 1 and {x}:'))
 
         if guess < random_number:
             print("Sorry,The Random Number is too low.")
 
         elif guess > random_number:
             print("Sorry,The Random Number is too high.")
         
     print(f"Yay,Congrats you have guessed the number {random_number} ") 
     guess(10)  
def computer_guess(x):
   low=1
   high=x
   feedback=""
 
   while feedback != 'c':
         if low != high:
          guess=random.randint(low,high)
         else:
           guess=low # could also be high b/c low = high
           feedback=input(f"Is {guess} too high(H),too low(L), or Correct (C)!!".lower())
         if feedback == 'h':
            high = guess - 1
         elif feedback == 'l':
            low = guess + 1
               
   print(f"yay! The Computer guessed the number ,{guess} ,correctly!!")           
             
 
 
 
computer_guess(100) 




















































