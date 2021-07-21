print("created by hussainatphysics@gmail.com(hussainsha syed")
print("welcome to pizza bill calculator")

"""
we are creating pizza bill calculator....i am adding but variable as i am creating exe file noting morethan this

"""



size = input("What size pizza do you want? S, M, or L ")
but1=input("press enter")
add_pepperoni = input("Do you want pepperoni? Y or N ")
but2=input("press enter")
extra_cheese = input("Do you want extra cheese? Y or N ")





cost=0

if size=="S":
  cost+=15
elif size=="M":
  cost+=20
elif size=="L":
  cost+=25

else:
  print('choose proper pizza letter')

if add_pepperoni=="Y":
  if size=="S":
    cost+=2
  else:
    cost+=3
if extra_cheese=="Y":
  cost+=1

print(f"your final bill is:${cost}")
print()
but3=input("press enter for byeeeeeeeee")