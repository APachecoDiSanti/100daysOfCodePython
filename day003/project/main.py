print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
decision = input("You stand at a crossroad. Are you going 'left' or 'right'? ")
if decision.lower() == "left":
    decision = input("You reach the shore. There's an island in the horizon. Do you 'wait' for a boat or 'swim' to the island? ")
    if decision.lower() == "wait":
        decision = input("On the island there's a tower with three colored doors. Do you enter the 'red' door? the 'yellow' one? or maybe the 'blue' one? ")
        if decision.lower() == 'red':
            print("You enter the red door. As soon as you close it, the door locks and a fire starts. You are burned alive.")
            print("Game over!")
        elif decision.lower() == 'blue':
            print("You enter the blue door. As soon as you close it, the door locks and beasts in the room attack you. You are eaten alive.")
            print("Game over!")
        elif decision.lower() == 'yellow':
            print("Before you is a treasure chest gleaming with gold coins and precious stones.")
            print("Well done! You found the treasure!")
        else:
            print(f"You try to enter the '{decision}' door, but while you look for it you die of exhaustion.")
            print("Game over!")
    else:
        print("You swim towards the island. A shark attacks you and kills you.")
        print("Game over!")
else:
    print("You go right and fall into a hole.")
    print("Game over!")
    


    