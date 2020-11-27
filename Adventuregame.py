
import getpass



username = getpass.getuser()

print(" Welcom to, Kingdom of Peril {}.".format(username))

answer =input(" would you like to play? (yes/no ")

print('Name Your Warrior:')
player_name = input()
print('Welcom to Kingdom of peril {}  ,'.format(player_name))


player_race = ["elf", "dwarf", "human"]
print("Chose your Race!")
player_race = input(player_race)
print(f"you have chosen {player_race}")

print("chouse your Class ")
player_class = [" Atomic  Wizard "," Arcane Archer "," Swardan the Conquer "]



player_class = input(player_class)
print(f"  {player_name}  The  {player_class} of the {player_race} Race. Good luck on your Quest, Dont Die to Quick or you will be talking me agin, Mwahah!")







print(f"its time you Head out on your adventure! {player_name} The {player_class}")

   


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
            else:
                 print("you got away!")
                 

    elif answer == "right":
        print("you walk aimlessly to the right and fall on a patch of ice you indure your leg and can not contune. game over")

    