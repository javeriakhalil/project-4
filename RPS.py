import random
 
def play():
     user=input(" What's your choice 'R' for Rock,'P' for Paper ,'S' For Scissor \n")
     computer=random.choice(['R','P','S'])
 
     if user == computer:
         return "It's Tie"
     if is_win(user,computer):
         return "You Won"
         
     return  "You Lost"
def is_win(player,opponent):
      return (player == 'R' and opponent == 'S') or \
            (player == 'S' and opponent == 'P') or \
            (player == 'P' and opponent == 'R')
print(play())