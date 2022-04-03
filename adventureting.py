##########################
#IMPORTS
##########################

from adventurelib import *

##########################
#DEFINE ROOMS
##########################

eroom = room("You are in a big entrance room")
dhall = room("your in a long hallway which leads to a bedroom")
stairs = room("You are on a steep staircase")
guestbed = room("Small bedroom with a mysterious spare room")
keyroom = room("Dusty room with a small key on a desk")
uphall = room("small hallway leading to another bathroom and bedroom")
bathroom = room("spacious bathroom, nothing special")
masterbed = room("massive room with a safe on a bed")

##########################
#DEFINE CONNECTIONS
##########################

eroom.east = dhall
eroom.north = staircase
dhall.west = eroom
dhall.north = guestbed
guestbed.south = dhall
guestbed.east = keyroom
keyroom.west = guestbed
staircase.south = eroom
staircase.north = uphall
uphall.south = masterbed
uphall.west = staircase	
uphall.north = bathroom
bathroom.south = uphall
masterbed.north = masterbed

##########################
#DEFINE ITEMS
##########################

key = item("A key")
key.description = "The key is rusted but in one piece"
safe = item("A safe")
safe.description = "Small safe with a key slotin the middle"

##########################
#DEFINE BAGS
##########################

Room.items = Bag()

##########################
#ADD ITEMS TO BAGS
##########################


##########################
#DEFINE ANY VARIABLES
##########################

current_room = eroom

##########################
#BINDS (eg"@when(look"))
##########################


##########################
#MAIN FUNCTION
##########################