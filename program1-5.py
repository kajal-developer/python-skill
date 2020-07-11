player1_run=int(input("enter the run of player1:"))
player2_run=int(input("enter the run of player2:"))
player3_run=int(input("enter the run of player3:"))
strikerate1=player1_run*100/60
strikerate2=player2_run*100/60
strikerate3=player3_run*100/60
print("the strikerate of player1",strikerate1)
print("the strikerate of player2",strikerate2)
print("the strikerate of player3",strikerate3)
print("if player1 gets 60 more balls then run will be",player1_run*2)
print("if player2 gets 60 more balls then run will be",player2_run*2)
print("if player3 gets 60 more balls then run will be",player3_run*2)
print("max six hit by player1",player1_run//6)
print("max six hit by player2",player2_run//6)
print("max six hit by player3",player3_run//6)

