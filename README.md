# mistbornTextGame
simple fun with a basic text game

Main constructs:
  -Nested dictionarys representing the game map.
    Map contains rooms, rooms contain their connections to other rooms and an item.
  -A dictionary representing the player.
    attributes are current location and inventory.

  Game startup sets initial values, and issues initial prompt to player.
  Input triggers the beginning of the game loop:
    input is validated and analyzed
      valid actions include moving to a connected room or picking up an item.
    corrisponding changes to the game state are implemented.
    prompt for the next action is output.

  If the end condition is met (entering the final room) during a loop cycle
    If the victory conditions are met show the victory narration.
    if not show the failure narration.

TODO:
- upgrade map and player constructs with class definitions.
- upgrade player construct to include attributes and abilities.
- expand valid command list.
- expand map size.
- upgrade item definitions to include gameplay effects, eg healing, movement enhacement.
- create combat system.
- define enemies.
