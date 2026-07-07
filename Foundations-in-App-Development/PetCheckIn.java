import java.util.Scanner;

/**
 * Foundations in App Development: Pet Check-In System
 *
 * Checks a dog or cat into an available boarding spot, collecting the
 * relevant details for each animal type. Dogs staying 2+ days are asked
 * about grooming. Reports "no space available" if all spots for that
 * pet type are full.
 *
 * Implemented from original course pseudocode.
 */
public class PetCheckIn {

    static final int NUM_DOG_SPOTS = 5;
    static final int NUM_CAT_SPOTS = 5;

    static Scanner scanner = new Scanner(System.in);

    public static void main(String[] args) {
        String[] dogSpots = new String[NUM_DOG_SPOTS];
        String[] catSpots = new String[NUM_CAT_SPOTS];

        for (int i = 0; i < NUM_DOG_SPOTS; i++) {
            dogSpots[i] = "OPEN";
        }
        for (int i = 0; i < NUM_CAT_SPOTS; i++) {
            catSpots[i] = "OPEN";
        }

        checkInPet(dogSpots, catSpots);
    }

    static void checkInPet(String[] dogSpots, String[] catSpots) {
        System.out.print("Cat or Dog? ");
        String petType = scanner.nextLine().trim().toLowerCase();

        System.out.print("New or returning pet? ");
        String petStatus = scanner.nextLine().trim();

        System.out.print("Enter pet's name: ");
        String petName = scanner.nextLine();

        String petAge;
        if (petStatus.equalsIgnoreCase("new")) {
            System.out.print("Enter pet's age: ");
            petAge = scanner.nextLine();
        } else {
            System.out.print("Enter updated age: ");
            petAge = scanner.nextLine();
        }

        if (petType.equals("dog")) {
            checkInDog(dogSpots, petName, petAge);
        } else if (petType.equals("cat")) {
            checkInCat(catSpots, petName, petAge);
        } else {
            System.out.println("Invalid pet type.");
        }
    }

    static void checkInDog(String[] dogSpots, String petName, String petAge) {
        for (int i = 0; i < dogSpots.length; i++) {
            if (dogSpots[i].equals("OPEN")) {
                System.out.print("Enter dog's weight: ");
                double dogWeight = Double.parseDouble(scanner.nextLine());

                System.out.print("How many days will your dog stay? ");
                int daysStay = Integer.parseInt(scanner.nextLine());

                boolean grooming = false;
                if (daysStay >= 2) {
                    System.out.print("Grooming requested? (yes/no): ");
                    grooming = scanner.nextLine().trim().equalsIgnoreCase("yes");
                }

                dogSpots[i] = petName + " " + petAge + " " + dogWeight + " " + grooming;
                System.out.println("Check-in complete. Dog assigned to space " + i);
                return;
            }
        }

        System.out.println("No space available.");
    }

    static void checkInCat(String[] catSpots, String petName, String petAge) {
        for (int i = 0; i < catSpots.length; i++) {
            if (catSpots[i].equals("OPEN")) {
                System.out.print("How many days will your cat stay? ");
                int daysStay = Integer.parseInt(scanner.nextLine());

                catSpots[i] = petName + " " + petAge + " " + daysStay;
                System.out.println("Check-in complete. Cat assigned to space " + i);
                return;
            }
        }

        System.out.println("No space available.");
    }
}