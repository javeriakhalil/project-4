import time
 
def countsdown(t):
     while t:
           mins,secs=divmod(t,60)
           timer='{:02d}:{:02d}'.format(mins,secs)
           print(timer,end="\r")
           time.sleep(1)
           t -= 1
 
     print("Timer Completed")  
 
t =input("Enter The Time In Second:")
countsdown(int(t))












