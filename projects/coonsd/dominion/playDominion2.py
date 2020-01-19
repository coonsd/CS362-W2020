# -*- coding: utf-8 -*-
"""
Created on Thurs Jan 16 18:48:00 2020

@author: coonsd

This version of playDominion has a test scenario where 
there is only one player name provided.

The game does not crash, but it causes the number of 
curse cards to be zero.  It also violates the rule that 
Dominion is played with 2-4 players.
"""

import Dominion
import testUtility
import random
from collections import defaultdict

#Get player names
player_names = testUtility.GetNames()

# TEST SCENARIO
# Remove all players except the first
player_names = player_names[0:1]

#number of curses and victory cards
nV = testUtility.GetNumVictoryCards(player_names)
nC = testUtility.GetNumCurseCards(player_names)

#Define box
box = testUtility.GetBoxes(nV)

# Define supply order
supply_order = testUtility.GetSupplyOrder()

# Construct the supply from the base and random sets
supply = defaultdict(list)
testUtility.AddBaseSupply(supply, player_names, nV, nC)
testUtility.AddRandSupply(supply, box)

#initialize the trash
trash = []

#Costruct the Player objects
players = testUtility.GetPlayerSet(player_names)

#Play the game
turn  = 0
while not Dominion.gameover(supply):
    turn += 1    
    print("\r")    
    for value in supply_order:
        print (value)
        for stack in supply_order[value]:
            if stack in supply:
                print (stack, len(supply[stack]))
    print("\r")
    for player in players:
        print (player.name,player.calcpoints())
    print ("\rStart of turn " + str(turn))    
    for player in players:
        if not Dominion.gameover(supply):
            print("\r")
            player.turn(players,supply,trash)
            

#Final score
dcs=Dominion.cardsummaries(players)
vp=dcs.loc['VICTORY POINTS']
vpmax=vp.max()
winners=[]
for i in vp.index:
    if vp.loc[i]==vpmax:
        winners.append(i)
if len(winners)>1:
    winstring= ' and '.join(winners) + ' win!'
else:
    winstring = ' '.join([winners[0],'wins!'])

print("\nGAME OVER!!!\n"+winstring+"\n")
print(dcs)