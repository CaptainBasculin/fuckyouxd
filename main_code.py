import os
import random as rng

if 1 == 2:
    print("LOOK AT THIS DUDE, our code broke the possibility chamber")

print("this is a test")
for i in reversed(range(0, 50)):
    print(i, "seconds until forking")
    print(rng.randint(1,80))

print("it's Raping time")

print('Simple Combat Game')
print('Written as a collaboration between collabVM users')

hp_1 = 150
hp_2 = 150

# We need to determine their damage range and their accuracy

def attack (weapon):
    #Sword: Deals moderate damage, has high accuracy
    if weapon == "sword":
        #Determine if hit. if missed return damage 0
        if rng.randint(0,100)>70:
            return 0
        #Attack: 15-30
        else:
            dmg = rng.randint(15,30)
            return dmg
    
    if weapon == "axe":
        #Determine if hit. if missed return damage 0
        #Accuracy: 50
        if rng.randint(0,100)>50:
            return 0
        #Attack: 25-40
        else:
            dmg = rng.randint(25,40)
            return dmg
    
    if weapon == "spell":
        #Determine if hit. if missed return damage 0
        if rng.randint(0,100)>30:
            return 0
        #Attack: 20-80
        else:
            dmg = rng.randint(20,80)
            return dmg
#Type to Text: This function will turn the small names to their meanings in-game
def typetotext (ooF):
    if ooF == "axe":
        return "Axe Strike"
    if ooF == "sword":
        return "Sword Slash"
    if ooF == "spell":
        return "Spell of Destruction"
def atktext (number):
    if number == 0:
        return "missed! "
    elif number < 18:
        return " couldn't focus properly! "
    elif number < 30:
        return " struck the enemy! "
    elif number < 40:
        return " hit it with all it got! "
    else:
        return " did outstanding damage! He hit the enemy with all his might! "
print('Which gamemode do you want to play? Against CPU (cpu) or against another player?(1v1)')
gamemode = input()
#This person is too lazy to wrote a 1v1 gamemode, but will write an against cpu mode. 
#f you want it please code it yourself
if gamemode == "cpu":
    print('We will be fighting aganist a dumb CPU.')
    rowCounter = 0
    while hp_1>0 and hp_2>0:
        rowCounter=rowCounter+1
        print(str(rowCounter),'. turn')
        print("Use your attack type! Your available moves are")
        print("(axe) Axe Strike, Accuracy: 70, Attack: 25-40 ")
        print("(sword) Sword Slash, Accuracy: 50, Attack: 15-30 ")
        print("(spell)  Spell of Destruction, Accuracy: 30, Attack: 20-80")
        AttackType = input()
        #I'll add a check here later
        # while AttackType != 'axe' or AttackType != 'sword' or AttackType != 'spell':
        #     print("You don't have that skill! Please use a skill you know!")
        #     AttackType = input()
        #This is the foe's weapon type (1 = sword, 2 = axe, 3 = spell), determined rngly
        foe_no = rng.randint(1,3)
        if foe_no == 1:
            foe_wp = "sword"
        elif foe_no == 2:
            foe_wp = "axe"
        elif foe_no == 3:
            foe_wp = "spell"
        npc_oldHP = hp_2
        dealt_dmg = attack(AttackType)
        hp_2 = hp_2-dealt_dmg
        print ("You used: ", typetotext(AttackType))
        print("You",atktext(dealt_dmg),"You dealt ",str(dealt_dmg),"damage")
        if hp_2 > 0:
            print("The enemy now has", str(hp_2), " HP")
        else: 
            print ("The enemy is ded!")
        #Now it's the NPC's turn!
        your_oldhp = hp_1
        enemy_dmg = attack(foe_wp)
        hp_1 = hp_1 - enemy_dmg
        print ("The Enemy used: ", typetotext(foe_wp))
        print("The Enemy",atktext(enemy_dmg),"The Enemy dealt ",str(enemy_dmg),"damage")
        if hp_1 > 0:
            print("You have", str(hp_1), " HP")
        else:
            print("You are ded!")
        if hp_1 < 0:
            loser = "You"
        if hp_2 < 0:
            loser = "The Enemy"
    if loser == "You":
        print("You lost!")
    if loser == "The Enemy":
        print("You won!")
else:
    print ("Other gamemodes aren't programmed in yet")
