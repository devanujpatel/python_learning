import random,sys

print("ROCK, PAPER, SCISSOR ")
wins=0
losses=0
ties=0

while True:
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True:    
        print("enter your move : (r)ock,(s)cissor,(p)aper or (q)uit")
        playermove=input()
        if playermove=='q':
             sys.exit()
        if playermove=='p' or playermove=='s' or playermove=='r':
          break
    if playermove=='s':
        print("SCISSOR versus")
    elif playermove=='r':
        print("ROCK versus")
    elif playermove=='p':
        print("PAPER versus")
    randomnumber=random.randint(1,3)
    if randomnumber==1:
        computermove='r'
        if computermove=='r':
         print("ROCK")
    if randomnumber==2:
        computermove='p'
        if computermove=='p':
         print("PAPER")
    if randomnumber==3:
        computermove='s'
        if  computermove=='s':
         print("SCISSOR")
    if playermove==computermove:
        print("TIE")
        ties=ties+1
    elif playermove=='p' and computermove=='s':
        print("loss")
        losses=losses+1
    elif playermove=='p 'and computermove=='r':
        print("win")
        wins=wins+1
    
    elif playermove=='s' and computermove=='p':
        print("win")
        wins=wins+1
    if playermove=='s' and computermove=='r':
        print("loss")
        losses=losses+1

    if playermove=='r' and computermove=='s':
        print("win")
        wins=wins+1

    if playermove=='r' and computermove=='p':
        print("loss")
        losses=losses+1
