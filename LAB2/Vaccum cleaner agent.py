
import random

choice = int(input("1. Two Rooms\n2. Four Rooms\nEnter choice: "))

# ---------------- 2 ROOMS ----------------
if choice == 1:

    rooms = ["A", "B"]

    # Random initial condition
    room_A = random.choice(["Dirty", "Clean"])
    room_B = random.choice(["Dirty", "Clean"])

    location = "A"

    print("\nInitial State:")
    print("A =", room_A)
    print("B =", room_B)

    while room_A == "Dirty" or room_B == "Dirty":

        if location == "A":

            if room_A == "Dirty":
                print("A is Dirty -> Cleaning A")
                room_A = "Clean"

            else:
                print("A is Clean -> Moving to B")
                location = "B"

        else:   # location == B

            if room_B == "Dirty":
                print("B is Dirty -> Cleaning B")
                room_B = "Clean"

            else:
                print("B is Clean -> Moving to A")
                location = "A"

    print("\nAll rooms are Clean!")


# ---------------- 4 ROOMS ----------------
elif choice == 2:

    rooms = ["A", "B", "C", "D"]

    # Random initial condition
    A = random.choice(["Dirty", "Clean"])
    B = random.choice(["Dirty", "Clean"])
    C = random.choice(["Dirty", "Clean"])
    D = random.choice(["Dirty", "Clean"])

    location = "A"

    print("\nInitial State:")
    print("A =", A)
    print("B =", B)
    print("C =", C)
    print("D =", D)

    while A == "Dirty" or B == "Dirty" or C == "Dirty" or D == "Dirty":

        if location == "A":

            if A == "Dirty":
                print("A is Dirty -> Cleaning A")
                A = "Clean"

            else:
                print("A is Clean -> Moving Right to B")
                location = "B"

        elif location == "B":

            if B == "Dirty":
                print("B is Dirty -> Cleaning B")
                B = "Clean"

            else:
                print("B is Clean -> Moving Down to C")
                location = "C"

        elif location == "C":

            if C == "Dirty":
                print("C is Dirty -> Cleaning C")
                C = "Clean"

            else:
                print("C is Clean -> Moving Left to D")
                location = "D"

        elif location == "D":

            if D == "Dirty":
                print("D is Dirty -> Cleaning D")
                D = "Clean"

            else:
                print("D is Clean -> Moving Up to A")
                location = "A"

    print("\nAll rooms are Clean!")


else:
    print("Invalid choice!")