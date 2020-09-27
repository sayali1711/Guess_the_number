str1="GUESS THE NUMBER!!"
print(str1.center(40,'#'))
import random
ran=random.randint(0,100)
def display():
   if(ip>=ran):
      error=ip-ran
      print("Your guess is greater by",error)
   elif(ran>=ip):
      error=ran-ip
      print("Your guess is less by",error)
   else:
      print("Your guess is correct!")
cmd="yes"      
while(cmd=="yes"):
    ip=input("Enter your guess!!")
    ip2=ip.isdigit()
    if(ip2==True):
        ip=float(ip)
        display()
        cmd=input("Do you want to give another try?\n1.yes\n2.no\n")   
    else:
        print("Invalid input\nEnter input in numeric form")
        exit()
