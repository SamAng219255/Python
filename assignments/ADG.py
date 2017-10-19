import random
import time

d1=0
d2=0
game=True
cash=0
round=0
playing=True
pool=0
minBet=0
pointIds=[1,4,5,6,8,9,10]
points=[0]*len(pointIds)
playerPoints=[]
trying=True

def otPlDiceroll():
 global pool
 global players
 global points
 global minBet
 random.seed()
 D1=0
 D2=0
 SUM=0
 for i in range(len(players)):
  D1=random.randint(1,6)
  D2=random.randint(1,6)
  SUM=D1+D2
  if(minBet<players[i]):
   bett=int(random.random()**2)*(players[i]-minBet)+minBet
   players[i]-=bett
   pool+=bett
   if(SUM==playerPoints[i]):
    players[i]+=pool
    print("Player",(i+1),"won the POOL! Gaining",pool,"dollars!")
    pool=0
   elif(SUM==7 or (SUM==11 and playerPoints[i]==0)):
    if(playerPoints[i]==0):
     players[i]+=pool
     print("Player",(i+1),"won the POOL! Gaining",pool,"dollars!")
     pool=0
   elif(SUM==2 or SUM==3 or SUM==12):
    print("Player",(i+1),"has lost. Ending the game with",players[i],"dollars.")
    minBet=int(minBet/2)
    minBet=max(minBet,10)
    players[i]=0
   elif(round==1):
    playerPoints[i]=SUM
  time.sleep(0.1)

def diceroll():
 global pool
 global game
 global players
 random.seed()
 global d1, d2, sum
 d1=random.randint(1,6)
 d2=random.randint(1,6)
 sum=(d1+d2)
 global cash, bet
 print ('You have',cash,'dollars')
 while True:
  print('The minimum bet is',minBet,'dollars.')
  if(minBet>cash):
   print("You can't afford this game anymore.")
   game=False
   playing=False
   cash=1000
   return False
   break
  if game:
   bett=input("How much to bet: $")
   if(bett=='hold'):
    if cash>0:
     print('You have ended the game with',cash,'dollars.')
    elif cash==0:
     print("Don't have many other options when broke...")
    else:
     print('You are now',(cash*-1),'dollars in debt.')
    return False
    game=False
    playing=False
    break
   elif int(bett)>cash:
    print("You can't bet more than you have.")
   elif int(bett)<minBet:
    print("You can't bet less than the minimum bet.")
   else:
    cash-=int(bett)
    pool+=int(bett)
    bet=bett
    print('The other players roll the dice...')
    time.sleep(0.5)
    otPlDiceroll()
    time.sleep(0.5)
    print('The POOL now contains',pool,'dollars.')
    return True
    break

bet=0
players=[]
point=0

if __name__ == '__main__':
 try:
  f=open("cash.txt","r")
  f.close()
 except FileNotFoundError:
  cash=1000
 else:
  f=open("cash.txt","r")
  cash=int(f.read())
  f.close()
 while trying:
  startCash=cash
  round=0
  players=[1000]*int(input('How many other players do you want to play with? '))
  playerPoints=[0]*len(players)
  minBet=10
  pool=0
  while playing:
   game=True
   points=[0]*len(pointIds)
   round=0
   while game:
    if diceroll():
     round+=1
     print('dice d1=',d1,'dice d2=',d2,'sum is',sum)
     if sum == point:
      cash+=pool
      print('You WIN and now have',cash,'dollars.')
      game=False
     elif(sum==7 or (sum==11 and point==0)):
      if(point==0):
       cash+=pool
       print('You WIN and now have',cash,'dollars.')
       game=False
      else:
       print('You LOSE and now have',cash,'dollars.')
       game=False
       playing=False
     elif(sum==2 or sum==3 or sum==12):
      print('You LOSE and now have',cash,'dollars.')
      game=False
      playing=False
     elif(round==1):
      point=sum
      print('Your POINT is',sum,'You must now roll',sum,'before you roll a 7\n inorder to add to your $',cash,'cash')
    minBet+=10
   playQuery="no"
   if(playing):
    playQuery=input("Do You want to keep playing?\n")
   yesses=["y","Y","yes","Yes","YES","si","Si","SI","ja","Ja","JA"]
   if playQuery in yesses:
    game=True
   else:
    playing=False
    if(cash>startCash):
     print('You gained',(cash-startCash),'dollars. Congratulations.')
    else:
     print('You lost',(startCash-cash),'dollars. Too Bad.')
  playQuery=input("Do You want to play again?\n")
  yesses=["y","Y","yes","Yes","YES","si","Si","SI","ja","Ja","JA"]
  if playQuery in yesses:
   playing=True
  else:
   trying=False
 f=open("cash.txt","w")
 f.write(str(cash))
 f.close()
