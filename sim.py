#! /usr/bin/python3

from random import randrange

n_pl = 4 # How many players do we have
# Init and name the players
names = ["Hans","Dieter","Peter","Olaf"] 
players = []
p = 1 # Do you want printing? 

class player:
    def __init__(self,st1,st2, name="test_bot",marks=0,eyes=0):
        self.st1 = st1
        self.st2 = st2
        self.name = name
        self.marks = marks
        self.eyes = eyes
        
# Strat which randomly continues or not (btw all strat need the same arguments)
def rand_strat(eyes,low):
    return randrange(0,2)

# Simple test strategy which stops above 8
def test_strat(eyes,low ):
    if (eyes > 8 and eyes < low): 
        return 1
    else: 
        return 0

# Simple strategy which continues w/o risk and returns final eye count
def cont_stat(num):
    count = num
    while(count<11):
        count+= throw_dice()
    return count

def max_marks():
    high = 0
    for pl in players:
        if pl.marks > high: high = pl.marks
    return high     

def find_max():
    high = 0
    for pl in players:
        if pl.eyes > high: high= pl.eyes
    return high     

def find_low():
    low = 32
    for pl in players:
        if pl.eyes < low: low = pl.eyes
    return low

def mark_loser():
    i = 0
    low = find_low()
    for pl in players:
        if pl.eyes == low: 
            pl.marks += 1
            if p: print(pl.name + " bekommt nen Strich. ")


def punish_loser():
    for pl in players:
        if pl.eyes >= 16 or pl.marks >= 3: 
            print(pl.name +" lost the game!")        

def throw_dice():
    return randrange(1,6)



players.append(player(test_strat,cont_stat,"Ulf")) # The chosen one
for i in range(n_pl-1):
    players.append(player(rand_strat,cont_stat,names[i]))


# Main loop for one Round of playing 

cur_eyes = 0
c1 = 1
while(True):                                      # Play until somebody lost
    if p: print("Starting Round "+ str(c1) )
    for  pl in players:   
        low = find_low()                          # Play one round
        pl.eyes = throw_dice()+throw_dice()       # Every player start ny throwing 2 times
        
        if pl.st1(pl.eyes,low):                   # Will the player choose to continue 
           pl.eyes += throw_dice() + throw_dice() # If so throw two more times 
        if pl.eyes > 16:                          # Stop if he has over-thrown
            if p: print(pl.name + " hat "+ str(pl.eyes) + " geworfen" )            
            break
        else: pl.eyes = pl.st2(pl.eyes)           # Otherwise continue with sec strat
    	
        if p: print(pl.name + " hat "+ str(pl.eyes) + " geworfen" )

    if find_max() > 16:  
        if p: print("Überworfen!")                # After the round: Did someone over-throw
        punish_loser()
        break
    else: mark_loser()                            # If not, mark losers

    if p: print(" \n")

    if max_marks() >= 3: 
        punish_loser()                     # Does anyone reach three marks
        break

    c1 += 1 



