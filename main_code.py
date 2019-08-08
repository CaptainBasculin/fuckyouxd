# collabvm-user:0w0whatsThis
import os
import random as rng

if 1 == 2:
    print("LOOK AT THIS DUDE, our code broke the possibility chamber")

print("this is a test")
for i in reversed(range(0, 50)):
    print(i, "seconds until forking")
    print(rng.randint(1,80))

print("it's Raping time")


print('We will be making a simple 1v1 rng combat game')

hp_1 = 100
hp_2 = 100

# We need to determine their damage range and their accuracy

def attack (str weapon):
    #Sword: Deals moderate damage, has high accuracy
    if weapon == sword:
        #Determine if hit. if missed return damage 0
        if rng.nextint(0,100)>70:
            return 0
        #Attack: 15-30
        else:
            dmg = rng.nextint(15,30)
            return dmg
    
    if weapon == axe:
        #Determine if hit. if missed return damage 0
        #Accuracy: 50
        if rng.nextint(0,100)>50:
            return 0
        #Attack: 25-40
        else:
            dmg = rng.nextint(25,40)
            return dmg
    
    if weapon == spell:
        #Determine if hit. if missed return damage 0
        if rng.nextint(0,100)>30:
            return 0
        #Attack: 20-80
        else:
            dmg = rng.nextint(20,80)
            return dmg

print('Which gamemode do you want to play? Against CPU (cpu) or against another player?(1v1)')
gamemode = input()
#This person is too lazy to wrote a 1v1 gamemode, but will write an against cpu mode. 
#f you want it please code it yourself
if gamemode == cpu:
    print('We will be fighting aganist a dumb CPU.')
    rowCounter = 0
    while hp_1>0 and hp_2>0:
        rowCounter=rowCounter+1
        print(str(rowCounter),'. turn')
        print("Use your attack type! Your available moves are"
        print("(axe) Axe Strike, Accuracy: 50, Attack: 25-40 ")
        print("(sword) Sword Slash, Accuracy: 50, Attack: 25-40 ") Spell of Destruction
        input
        

    







