"""
Foundations in App Development: Pet Check-In System

Checks a dog or cat into an available boarding spot, collecting the
relevant details for each animal type. Dogs staying 2+ days are asked
about grooming. Reports "no space available" if all spots for that
pet type are full.

Implemented from original course pseudocode.
"""

NUM_DOG_SPOTS = 5
NUM_CAT_SPOTS = 5


def check_in_dog(dog_spots, pet_name, pet_age):
    for i, spot in enumerate(dog_spots):
        if spot == "OPEN":
            dog_weight = float(input("Enter dog's weight: "))
            days_stay = int(input("How many days will your dog stay? "))

            grooming = False
            if days_stay >= 2:
                grooming = input("Grooming requested? (yes/no): ").strip().lower() == "yes"

            dog_spots[i] = f"{pet_name} {pet_age} {dog_weight} {grooming}"
            print(f"Check-in complete. Dog assigned to space {i}")
            return

    print("No space available.")


def check_in_cat(cat_spots, pet_name, pet_age):
    for i, spot in enumerate(cat_spots):
        if spot == "OPEN":
            days_stay = int(input("How many days will your cat stay? "))

            cat_spots[i] = f"{pet_name} {pet_age} {days_stay}"
            print(f"Check-in complete. Cat assigned to space {i}")
            return

    print("No space available.")


def check_in_pet(dog_spots, cat_spots):
    pet_type = input("Cat or Dog? ").strip().lower()
    pet_status = input("New or returning pet? ")
    pet_name = input("Enter pet's name: ")

    if pet_status.strip().lower() == "new":
        pet_age = input("Enter pet's age: ")
    else:
        pet_age = input("Enter updated age: ")

    if pet_type == "dog":
        check_in_dog(dog_spots, pet_name, pet_age)
    elif pet_type == "cat":
        check_in_cat(cat_spots, pet_name, pet_age)
    else:
        print("Invalid pet type.")


def main():
    dog_spots = ["OPEN"] * NUM_DOG_SPOTS
    cat_spots = ["OPEN"] * NUM_CAT_SPOTS

    check_in_pet(dog_spots, cat_spots)


if __name__ == "__main__":
    main()
