#Kenneth Edward Smith
#Simple text game
#Feb 2025

#keep track of player attributes
player = {
    'player_location': 'Entry',
    'inventory': []
    }

#map as a dictionary of rooms and their connections
rooms = {
    "Entry": {'item': '', 'paths': {'North': 'Main Hall'}},
    "Main Hall": {'item': 'Vials of Iron and Steel', 'paths': {'North': 'Tower Base', 'South': 'Entry', 'East': 'Sanctum', 'West': 'Armory'}},
    'Sanctum': {'item': 'An earring', 'paths': {'West': 'Main Hall'}},
    'Armory': {'item': 'Vials of Tin and Pewter', 'paths': {'East': 'Main Hall'}},
    'Tower Base': {'item': 'A Mistborns Obsidian Dagger', 'paths': {'West': 'Inquisitor Chamber', 'East': 'Stairs'}},
    'Inquisitor Chamber': {'item': 'Atium', 'paths': {'South': 'Armory'}},
    'Stairs': {'item': 'A Mistborns second Obsidian Dagger', 'paths': {'East': 'Tower Top', 'West': 'Tower Base'}},
    'Tower Top': {'item': '', 'paths': {'Forward': 'DESTINY', 'FORWARD': 'DESTINY'}}
    }

#helper function for readability in output lines
def get_directions(roo):
    return ", ".join(rooms[roo]['paths'].keys()) if roo != 'Tower Top' else "'forward' to meet your DESTINY!"

#specific for validating move commands
def get_direction_valid(com, roo):
    for room in rooms[roo]['paths'].keys():
        if com.lower() in room.lower():
            return True

#helper function for building the prompt
def item_prompt(roo):
    return "" if rooms[roo]['item'] == '' else "Found Item: {}. ".format(rooms[roo]['item'])

#function for moving between rooms
def move(command):
    if get_direction_valid(command[5:], player['player_location']):
        #print("valid direction detected")
        print(f"moving {command[5:]} to the {rooms[player['player_location']]['paths'][command[5:].capitalize()]}")
        player['player_location'] = rooms[player['player_location']]['paths'][command[5:].capitalize()]
    else:
        print("Selected direction invalid, please enter movement in the form 'move *Direction*'")

#function for collecting items
def get(command):
    contents = rooms[player['player_location']]['item']
    if contents == '' or contents in player['inventory']:
        print("Nothing to get")
    else:
        #print("Item located")
        print("Adding {} to inventory".format(contents))
        player['inventory'].append(contents)
        rooms[player['player_location']]['item'] = ''

#function to check inventory
def inventory():
    print("What have I got in my pocket?")
    if len(player['inventory']) >= 1:
        for i in player['inventory']:
            print(i)
    else:
        print("oh, pockets are empty...")

#start of game with prompt and first command
print("Welcome, to Kredik Shaw. Throne, palace, home to the Lord Ruler")
print("Your destiny approaches, will you discover the secrets of His dark fortress?")
print("Can you defeat the man who has ruled as a god for a thousand years?")
print("(Explore the fortress of Kredik Shaw, command: 'move *Direction*')")
print("(Collect the items you need, command: 'get item')")
command = input(f"In the {player['player_location']}, can go {get_directions(player['player_location'])}: ")



#loop for processing input, and prompting for more input
while player['player_location'] != "exit" or player['player_location'] != 'DESTINY':
    #wxit condition breaks, loop condition also ends for extra protection
    if command.lower() == "exit":
        player['player_location'] = "exit"
        break

    #move command processed
    elif "move" in command.lower():
        #move to different room.
        #print("Move command registered")
        #validate direction, if good, execute move
        move(command)

    #get item processed
    elif "get item" in command.lower():
        get(command)

    #check inventory
    elif 'inventory' in command.lower():
        inventory()

    #help, instructions, or commands
    elif 'help' in command.lower() or 'instructions' in command.lower() or 'commands' in command.lower():
        print("Explore the rooms of Kredik Shaw with the command 'move' followed by the direction you wish to go.")
        print("If you find an item in a room you can add it to your inventory with 'get item'.")
        print("To check your current items use 'inventory'.")
        print("Good Luck!")

    else:
        print("Command not recognized (help for help)")

    #build prompt for next input
    if player['player_location'] == 'DESTINY':
        break
    prompt = "In the {}. {}Can go {}: ".format(player['player_location'], item_prompt(player['player_location']), get_directions(player['player_location']))

    command = input(prompt)

#Game loop ended. Either voluntary exit, or reached end of game
#if end of game, check for victory or defeat.
if player['player_location'] == "exit":
    pass
elif player['player_location'] == "DESTINY":
    if len(player['inventory']) == 6:
        print("You enter the room a silent shadow. Before you facing out the large stained glass windows stands the Lord Ruler.\nAfter a brief intense contest of wills, you overpower him.\nWith the oppressor dead, will you claim his place?\nWhat new fate awaits you?")
    else:
        print("You enter the room a silent shadow. Before you facing out the large stained glass windows stands the Lord Ruler.\n'I have been expecting you', he says, voice the tolling of fate.\nThough you struggle with all your might, you die by his hand, a mere footnote to his rule.")
else:
    print("Something went wrong...")

print("\nThank you for playing! Visit again sometime!")