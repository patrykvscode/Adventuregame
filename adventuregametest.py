
import getpass

username = getpass.getuser()

print("welcom to the best adventure of your life {}.".format(username))

answer =input(" would you like to play? (yes/no ")

if answer.lower().strip() == "yes":


    answer = input("You Have Reached a fork in the road would you like to go  left or right?").lower().strip()
    if answer == "left":
        answer = input("You make your way off the path in to the swamp, its starting to get dark, you see a fire you make your way to wards the fire, you finally make it, after walking for 20 minutes you encounter a  Sleeping dragon, what do you do attack or run ")

        if answer == "attack":
            print("you attack the dragon but your attacks are weak,  The dragon awakes!  and burns you to a chrisp  You lost!")
        else:
            print(" Yea that was a good idea")

            answer = input("you see a car and a boat. witch would you like to take (car/boat)")

            if answer == "boat":
                 print(" unfortunetly you do not know how to stear a boat...Game Over")
            else:y
                 print("you got away!")
                 

    elif answer == "right":
        print("you make your way to the right, you see some leaves and you try to step over them, but it's a trap you fall in a hole, with the littel ammout if light that you do have you ")

       
    