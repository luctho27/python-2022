
##########################
#IMPORTS
##########################

from adventurelib import *
import time

##########################
#DEFINE ROOMS
##########################

eroom = Room("You are in a big entrance room")
dhall = Room("your in a long hallway which leads to a bedroom")
stairs = Room("You are on a steep staircase")
guestbed = Room("Small bedroom with a mysterious spare room")
keyroom = Room("Dusty room with a small key on a desk")
uphall = Room("small hallway leading to another bathroom and bedroom")
bathroom = Room("spacious bathroom, nothing special")
masterbed = Room("massive room with a safe on a bed")

##########################
#DEFINE CONNECTIONS
##########################

eroom.east = dhall
eroom.north = stairs
dhall.west = eroom
dhall.north = guestbed
guestbed.south = dhall
guestbed.east = keyroom
keyroom.west = guestbed
stairs.south = eroom
stairs.north = uphall
uphall.south = masterbed
uphall.west = stairs	
uphall.north = bathroom
bathroom.south = uphall
masterbed.north = masterbed

##########################
#DEFINE ITEMS
##########################

key = Item("key")
key.description = "The key is rusted but in one piece"
safe = Item("safe")
safe.description = "Small safe with a key slot in the middle"

##########################
#DEFINE BAGS
##########################

Room.items = Bag()

##########################
#ADD ITEMS TO BAGS
##########################

keyroom.items.add(key)
masterbed.items.add(safe)

##########################
#DEFINE ANY VARIABLES
##########################

current_room = eroom
inventory = Bag()
key_used = False
safe_opened = False

##########################
#BINDS (eg"@when(look"))
##########################

@when("look")
def look():
	print(current_room)
	print("There are rooms to the",current_room.exits())
	if len(current_room.items) > 0:
		print("You also see:")
		for item in current_room.items:
			print(item)

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def get_item(item):
	#check if item is in room
	#take it out of room
	#put into inventory
	#otherwise tell user there is no item
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You picked up the {item}")
	else:
		print(f"You don't see a {item}")

@when ("use ITEM")
def use(item):
	if item == "key" and current_room == masterbed:
		print("You open the safe and money spills out")
		print("You have won")
		safe_opened = True


@when("inventory")
def check_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)

@when("go DIRECTION")
@when("DIRECTION")
@when("travel DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		#Checks if the current room list of exits has
		#The direction the player wants to go
		current_room = current_room.exit(direction)
		print(f"You go {direction}")
		print(current_room)
	else:
		print("You can't go that way")
##########################
#MAIN FUNCTION
##########################
def main():
	print(current_room)
	start()
	#start the main loop

main()
