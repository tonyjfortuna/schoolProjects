"""
Introduction to Scripting: Data Center Breach

A text adventure game. You are inside a compromised data center after
a cyberattack has locked down critical systems. Navigate the facility,
collect the network diagram, USB drive, keycard, admin credentials, and
power override, then enter the server room to stop the breach.

Entering the server room without all five items ends the game in failure.

Implemented from original course design document (map layout and
movement/item pseudocode).
"""

rooms = {
    "Lobby": {
        "exits": {"north": "Network Operations Center", "south": "Office Workspace"},
        "item": None,
    },
    "Network Operations Center": {
        "exits": {"south": "Lobby", "east": "IT Storage Room", "west": "Security Office"},
        "item": "network diagram",
    },
    "IT Storage Room": {
        "exits": {"west": "Network Operations Center"},
        "item": "usb drive",
    },
    "Security Office": {
        "exits": {"east": "Network Operations Center"},
        "item": "keycard",
    },
    "Office Workspace": {
        "exits": {"north": "Lobby", "east": "Backup Power Room", "south": "Server Room"},
        "item": "admin credentials",
    },
    "Backup Power Room": {
        "exits": {"west": "Office Workspace"},
        "item": "power override",
    },
    "Server Room": {
        "exits": {"north": "Office Workspace"},
        "item": None,
    },
}

REQUIRED_ITEMS = {
    "network diagram",
    "usb drive",
    "keycard",
    "admin credentials",
    "power override",
}


def print_status(current_room, inventory):
    print(f"\nYou are in the {current_room}")
    print(f"Inventory: {', '.join(inventory) if inventory else 'empty'}")
    print("-" * 40)


def handle_move(command, current_room):
    direction = command.replace("go ", "", 1)
    exits = rooms[current_room]["exits"]

    if direction in exits:
        return exits[direction]

    print("You can't go that way!")
    return current_room


def handle_get(command, current_room, inventory):
    requested_item = command.replace("get ", "", 1)
    room_item = rooms[current_room]["item"]

    if room_item is None:
        print("There is no item in this room.")
        return

    if requested_item == room_item:
        inventory.add(room_item)
        rooms[current_room]["item"] = None
        print(f"{requested_item} retrieved!")
    else:
        print(f"Can't get {requested_item}!")


def main():
    current_room = "Lobby"
    inventory = set()
    game_over = False

    print("You are inside a compromised data center after a cyberattack has")
    print("locked down critical systems. Collect everything you need, then")
    print("reach the Server Room to stop the breach.\n")
    print("Commands: go north/south/east/west, get <item name>\n")

    while not game_over:
        print_status(current_room, inventory)
        player_move = input("Enter your move: ").strip().lower()

        if player_move.startswith("go "):
            current_room = handle_move(player_move, current_room)

            if current_room == "Server Room":
                if inventory == REQUIRED_ITEMS:
                    print("\nAll systems restored. The breach has been stopped. You win!")
                else:
                    missing = REQUIRED_ITEMS - inventory
                    print(f"\nYou entered the Server Room without: {', '.join(missing)}.")
                    print("The breach completes before you can stop it. Game over.")
                game_over = True

        elif player_move.startswith("get "):
            handle_get(player_move, current_room, inventory)

        else:
            print("Invalid input!")


if __name__ == "__main__":
    main()
