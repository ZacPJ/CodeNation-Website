replay = 0 #A replay value, to check if the player has restarted after completing the game, for now, just stops the settings reappearing
from os import system, name #Will use this to clear the console after each area

if name == "nt": #Checks for the ubuntu system and uses the specific clear function
    _ = system("cls")
else: #Checks for any other system and uses a general clear function
    _ = system("clear")
gameLoop = False #This loop will never be changed as I used the exit() functions elsewhere
speed = 0.03 #Speed text appears on the screen
while gameLoop == False: #This will loop the entire game unless exited
    

    import time
    import sys
    import random
    
    health = 10 #The player's starting health, did not need to give it a maximum value as uncapped works better for the game
    map= False #Checks whether the player has the map to access more areas
    weapon = "None" #This is the starting weapon of the character, wipes to none for if the game is restarted
    damage = 0
    def clear(): #Creates a clear function to clear the console so it is less cluttered after each area
        global speed
        temp_speed = speed #Stores the old speed setting
        speed = 0.05 #Slows the text speed for DRAMATIC EFFECT
        typewriter("\n\nPress enter to continue") 
        choice = input() #An empty input so no matter what it continues but it also waits for the player to press enter before continuing, illusion of choice
        time.sleep(0.5) #Gives a pauce to the code for more DRAMATIC EFFECT
        if name == "nt": #Clears the ubuntu based console
            _ = system("cls") 
        else: #Clears the general console
            _ = system("clear")
        speed = temp_speed #Reverts the typewriter speed to the users previous choice
    def weapons(area):#This randomises the weapons the player can get based on the area they are in. If we were to expand the game there would be more areas with more loot
        global weapon
        global damage
        loop = False
        if area == "High-Loot": #This is currently only the police station but the loot here will do more damage
            weapon_choice = ["Police Baton","Military Knife"]
            weapon_random = random.randint(0,len(weapon_choice)-1) #choose a random item from the list above
            weapon_gain = weapon_choice[weapon_random]
            typewriter(f"Oh you found a {weapon_gain}, would you like to \n1. Take it \n2. Leave it") #Lets the player choose to replace the weapon or not
            choice = input(">>>") #Uses a string input to allow for both letters and numbers
            choice = choice.lower() #Makes the answer lower case
            choice = choice.strip() #Strips any blank space from before or after the answer
            while loop == False:
                if choice == "settings":
                    settings()
                    typewriter(f"Oh you found a {weapon_gain}, would you like to \n1. Take it \n2. Leave it") #Gives the choice to take or leave the weapon, in case the player is a masochist
                elif choice == "1":
                    typewriter(f"You take the {weapon_gain}") #Replaces the current weapon with the random one chosen
                    weapon = weapon_gain
                    damage = 4 + (weapon_random*2) # Increases the damage by a bit more, the knife specifically goes up by 2 compared to the baton
                    loop = True #Ends the loop
                elif choice == "2":
                    typewriter(f"You leave the weapon behind, was this a good idea?") #Does nothing as the weapon does not need to be updated
                    loop = True
                else: 
                    typewriter("Thats not an option") #Catches other options

        elif area == "Low-Loot":
            weapon_choice = ["Pipe","Wooden Board","Hammer"] #Stores the choices of weapons only at the end did I make the hammer the best one here
            weapon_random = random.randint(0,len(weapon_choice)-1)
            weapon_gain = weapon_choice[weapon_random]
            typewriter(f"Oh you found a {weapon_gain}, would you like to \n1. Take it \n2. Leave it") #Gives the choice to take or leave the weapon, in case the player is a masochist, currently the player cannot leave this weapon permanently as they need a weapon for the first fight
            while loop == False:
                choice = input(">>>")
                choice = choice.lower() #Makes the answer lower case
                choice = choice.strip() #Strips any blank space from before or after the answer
                if choice == "settings": 
                    settings()
                    typewriter(f"Oh you found a {weapon_gain}, would you like to \n1. Take it \n2. Leave it") #Since the typewriter is outside the while loop I put this hear since the console was cleared from the settings   
                elif choice == "1":
                    typewriter(f"You take the {weapon_gain}")
                    weapon = weapon_gain
                    damage = 1 + weapon_random #These weapons are worse overall, since the weapon_random could be 0 I added a 1 to the damage after some trial and error
                    loop = True
                elif choice == "2":
                    typewriter(f"You leave the weapon behind, was this a good idea?")
                    loop = True
                else: 
                    typewriter("Thats not an option")


    def typewriter(text): #Creates a typewriter effect, this function can be used instead of print()
        for i in text:
            global speed
            print (i, end = "")
            sys.stdout.flush()
            time.sleep(speed) #The time it waits inbetween each character in seconds
        print("") #Prints a new line for when the text is finished, so the entire programme isn't on the same line

    def zombie_art():#This will be called whenever zombie art is used, I chose to put all the art seperately since it looks neater below, if the game gets expanded on it can help in the future too.
            print(r"""
                                .....            
                                C C  /            
                                /<   /             
                ___ __________/_#__=o             
                /(- /(\_\________   \              
                \ ) \ )_      \o     \             
                /|\ /|\       |'     |             
                                |     _|             
                                /o   __\             
                                / '     |             
                                / /      |             
                                /_/\______|             
                                (   _(    <              
                                \    \    \             
                                \    \    |            
                                \____\____\           
                                ____\_\__\_\          
                                /`   /`     o\          
                                |___ |_______|.. .

            """)

    def knife_art():#Creates an easter egg for the knife
        print(r"""
                                _----..................___
    __,,..,-====>       _,.--''------'' |   _____  ______________`''--._
    \      `\   __..--''                |  /::: / /::::::::::::::\      `\
    \       `''                        | /____/ /___ ____ _____::|    .  \
    \                           ,.... |            `    `     \_|   ( )  |
        `.                       /`     `.\ ,,''`'- ,.----------.._     `   |
        `.                     |        ,'       `               `-.      |
            `-._                 \                                    ``.. /
                `---..............
        """)

    def library_art():#Creates the art for the library
        print(r"""
        _____________________________________________
    |.'',        Public_Library_Halls         ,''.|
    |.'.'',                                 ,''.'.|
    |.'.'.'',                             ,''.'.'.|
    |.'.'.'.'',                         ,''.'.'.'.|
    |.'.'.'.'.|                         |.'.'.'.'.|
    |.'.'.'.'.|===;                 ;===|.'.'.'.'.|
    |.'.'.'.'.|:::|',             ,'|:::|.'.'.'.'.|
    |.'.'.'.'.|---|'.|, _______ ,|.'|---|.'.'.'.'.|
    |.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
    |,',',',',|---|',|'|???????|'|,'|---|,',',',',|
    |.'.'.'.'.|:::|'.|'|???????|'|.'|:::|.'.'.'.'.|
    |.'.'.'.'.|---|','   /%%%\   ','|---|.'.'.'.'.|
    |.'.'.'.'.|===:'    /%%%%%\    ':===|.'.'.'.'.|
    |.'.'.'.'.|%%%%%%%%%%%%%%%%%%%%%%%%%|.'.'.'.'.|
    |.'.'.'.','       /%%%%%%%%%\       ','.'.'.'.|
    |.'.'.','        /%%%%%%%%%%%\        ','.'.'.|
    |.'.','         /%%%%%%%%%%%%%\         ','.'.|
    |.','          /%%%%%%%%%%%%%%%\          ','.|
    |;____________/%%%%%Spicer%%%%%%\____________;|
        """)
    def hammer_art():#Creates the easter egg for the hammer
        print(r"""
        
        T                                    \`.    T
        |    T     .--------------.___________) \   |    T
        !    |     |//////////////|___________[ ]   !  T |
             !     `--------------'           ) (      | !
                                              '-'      !
        """)
    def park_title():#Creates a title for the park
        print(r"""
    .----------------.  .----------------.  .----------------.  .----------------. 
    | .--------------. || .--------------. || .--------------. || .--------------. |
    | |   ______     | || |      __      | || |  _______     | || |  ___  ____   | |
    | |  |_   __ \   | || |     /  \     | || | |_   __ \    | || | |_  ||_  _|  | |
    | |    | |__) |  | || |    / /\ \    | || |   | |__) |   | || |   | |_/ /    | |
    | |    |  ___/   | || |   / ____ \   | || |   |  __ /    | || |   |  __'.    | |
    | |   _| |_      | || | _/ /    \ \_ | || |  _| |  \ \_  | || |  _| |  \ \_  | |
    | |  |_____|     | || ||____|  |____|| || | |____| |___| | || | |____||____| | |
    | |              | || |              | || |              | || |              | |
    | '--------------' || '--------------' || '--------------' || '--------------' |
    '----------------'  '----------------'  '----------------'  '----------------' 
        """)
    def police_title():#Creates a title for the police station
        print(r"""
    _____        _  _                        _____  _          _    _               
    |  __ \      | |(_)                      / ____|| |        | |  (_)              
    | |__) |___  | | _   ___  ___   ______  | (___  | |_  __ _ | |_  _   ___   _ __  
    |  ___// _ \ | || | / __|/ _ \ |______|  \___ \ | __|/ _` || __|| | / _ \ | '_ \ 
    | |   | (_) || || || (__|  __/           ____) || |_| (_| || |_ | || (_) || | | |
    |_|    \___/ |_||_| \___|\___|          |_____/  \__|\__,_| \__||_| \___/ |_| |_|
                            
        """)
    def school_title():#Creates a title for the school


        print(r"""
    _____      _                 _ 
    / ____|    | |               | |
    | (___   ___| |__   ___   ___ | |
    \___ \ / __| '_ \ / _ \ / _ \| |
    ____) | (__| | | | (_) | (_) | |
    |_____/ \___|_| |_|\___/ \___/|_|
                                    
    """)    
    def hospital_art():#Creates the art for the hospital
        print(r'''
                    _ _.-'`-._ _
                    ;.'________'.;
        _________n.[____________].n_________
        |""_""_""_""||==||==||==||""_""_""_""]
        |"""""""""""||..||..||..||"""""""""""|
        |LI LI LI LI||LI||LI||LI||LI LI LI LI|
        |.. .. .. ..||..||..||..||.. .. .. ..|
        |LI LI LI LI||LI||LI||LI||LI LI LI LI|
    ,,;;,;;;,;;;,;;;,;;;,;;;,;;;,;;,;;;,;;;,;;,,
    ;;jgs;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;     
        ''')                      
    def zombieboss_art():#Creates the zombie boss art, originally it would all print as a single thing, I split it up into lines for DRAMATIC EFFECT and so it would play in the console a little bit nicer
            
        print(r"    ../MMMMMMM\ ")
        time.sleep(0.02)
        print(r"    ./MMMMMMMMMMMMM\ ")
        time.sleep(0.02)
        print(r"    /MMMMMMMMMMMMMMMMM\ ")
        time.sleep(0.02)
        print(r"    /MMMMMMMMMMMMMMMMMMM\ ")
        time.sleep(0.02)
        print(r"    /MMMMMMMMMMMMMMMMMMMMM\ ")
        time.sleep(0.02)
        print(r"    |MMMMMMMMMMMMMMMMMMMMMMM ")
        time.sleep(0.02)
        print(r"    |MMMMMMMMMMMMMMMMMMMMMMM ")
        time.sleep(0.02)
        print(r"    |MMM/.......\MMMMMMMMMM| ")
        time.sleep(0.02)
        print(r"    \ \".........\MMMMMMM-\"| ")
        time.sleep(0.02)
        print(r"    ) \".. ___..   \MM/..|| ")
        time.sleep(0.02)
        print(r"    . _./||||      \\.I.|:\ ")
        time.sleep(0.02)
        print(r"        \||||HHH:::`.....(::..\ ")
        time.sleep(0.02)
        print(r"        `||HH:::::............\ ")
        time.sleep(0.02)
        print(r"        ||:.:::::: .......|..#\ ")
        time.sleep(0.02)
        print(r"        ||') .::::..........#####\_____ ")
        time.sleep(0.02)
        print(r"            \`  ::)..... /|.#|######::::::`   __ ")
        time.sleep(0.02)
        print(r"            //::::::. /#||\#########-#######:##|\ ")
        time.sleep(0.02)
        print(r"            \ \::: /##|##|###/############::####|\ ")
        time.sleep(0.02)
        print(r"            /-----###|####|\|#############::::###| ")
        time.sleep(0.02)
        print(r"            /#####-##- ######\#############::::####\ ")
        time.sleep(0.02)
        print(r"            /::::################\####################| ")
        time.sleep(0.02)
        print(r"        /:::::#################\##################|| ")
        time.sleep(0.02)
        print(r"        _/::::###################################\##:#|\ ")
        time.sleep(0.02)
        print(r"    /:###########################\########'   `#####|\ ")
        time.sleep(0.02)
        print(r"    /:#######:::###################\#####'      `|####|\ ")
        time.sleep(0.02)
        print(r"    /::######:::::######################'         ####||| ")
        time.sleep(0.02)
        print(r"    /::#######::######'       `#######\#'       .##|###|##\ ")
        time.sleep(0.02)
        print(r"    |::######::######'          `######       .####|######|\ ")
        time.sleep(0.02)
        print(r"    |:####:##### |##'             `###  L   .######|#######|\ ")
        time.sleep(0.02)
        print(r"    |:###########|#' .:####.          /#    \#####'/|`######| ")
        time.sleep(0.02)
        print(r"    |:###########||  ########:.         #    `##'  |#:::`###\ ")
        time.sleep(0.02)
        print(r"    `|:####:###:|||  ############         .       .|:\#######| ")
        time.sleep(0.02)
        print(r"    |\####:::::|VK|  `########'       #.|##     ##|\:\###`###\ ")
        time.sleep(0.02)
        print(r"    |#\####:::#|\|||.                 ##|###   ###| \:\#/#####\ ")
        time.sleep(0.02)
        print(r"    ########::#|:\||:#.       \###    ###\##.  `|#| |::::#####| ")
        time.sleep(0.02)
        print(r"    /########::#|`::\|#######.  \#||    ##|####  ##| |::::######\ ")
        time.sleep(0.02)
        print(r"    |||#:####:##| \:::\#######.   `#|  ####\##'  ##| |:::\###:##| ")
        time.sleep(0.02)
        print(r"    |||#:###::##|  \::::\####`#.   #        \   .### |::::\##::#| ")
        time.sleep(0.02)
        print(r"    |||########:/    \:::\#### #.            \  ####\ \::::#:::##\ ")
        time.sleep(0.02)
        print(r"    |:||########'     `\::###'###.           | ####|#\ \:::|::#:#| ")
        time.sleep(0.02)
        print(r"    |:#########|        \:\#######.############'  `###\ `::|#::##| .-X ")
        time.sleep(0.02)
        print(r"    |:#:#::#:##|         |:##########.     `##'    `|#\  |:|####.-XXXX ")
        time.sleep(0.02)
        print(r"    |:###::\\##|         |:#' #####`##.     `##.    `##| |::#.-XXXXXXX ")
        time.sleep(0.02)
        print(r"    |:|##::###\|         |::########`##.     `##.    ##| |.-XXXXXXXXX- ")
        time.sleep(0.02)
        print(r"    `||##\::\|#|          /:\### #\##`##.   .########|#.-XXXXXXXXX-'XX ")
        time.sleep(0.02)
        print(r"    |||###:#\#|         /:::#####|\################.-XXXXXXXXX-'XXXXX ")
        time.sleep(0.02)
        print(r"    |#|##\::##|        /:::########|\###########.-'XXXXX..X..XXXXXXXX ")
        time.sleep(0.02)
        print(r"    |:####\:##|       ':::#|#########\#######.-XXXXXXXX(#:#|::\XXXXXX ")
        time.sleep(0.02)
        print(r"    |:#####::##|     |::::|###########\###.-XXXXXXXXX(##\###\::\XX.-' ")
        time.sleep(0.02)
        print(r"    \:#|###|:##|     |::::|############.-XXXXXXXXX-'(#####`::`\::' ")
        time.sleep(0.02)
        print(r"    `:##|##|###|     |::::\`########.-XXXXXXXXX-'\\XX\#`\####\##`) ")
        time.sleep(0.02)
        print(r"    \:#:|#|::##|    |:::::######.-XXXXXXXXX-'\\\\\\XX\##`\###) ")
        time.sleep(0.02)
        print(r"    \####|:###|    |:::::#'#.-XXXXXXXXX-'X\\\\\\\\\XX\###) ")
        time.sleep(0.02)
        print(r"    ||###|####|    |:::::.-XXXXXXXXX-'\XXXX\\\\\\\\\-'| ")
        time.sleep(0.02)
        print(r"        \|#:\# ##|    |::.-'\\\XXXXX-'\\\\\XXXX\\\\\-'###| ")
        time.sleep(0.02)
        print(r"        \|#:\#::#    .-'\\\\\\\XXXX\\\\\\\\XXXX\-'######| ")
        time.sleep(0.02)
        print(r"        \|#'\:::\.-'\\\\\\\\\\\XXXX\\\\\\\\X-'#########| ")
        time.sleep(0.02)
        print(r"        `###-##::\\\\\\\\\\\\\\\XXXX\\\\\-'############| ")
        time.sleep(0.02)
        print(r"        \:####:::'\\\\\\\\\\\\\\XXXX\-'##|############| ")
        time.sleep(0.02)
        print(r"        |\\#####::#####`\\\\\\\\\X-'#####|############|     ")

    def settings():
        global speed
        global replay
        if replay == 0:
            typewriter("These are the game settings for the typewriter speed the speeds available are \n1. Slow \n2. Normal \n3. Fast \nIf you want to change these settings at any point, type \"Settings\" to get back to this section.")
            loop = False
            while loop == False: 
                choice = input(">>>")
                choice = choice.lower() #Makes the answer lower case
                choice = choice.strip() #Strips any blank space from before or after the answer
                if choice in ["1","one","slow"]: #Allows a few choiced for these settings, one to show off
                    speed = 0.05
                    loop = True
                    replay = 0 #Sets the replay value to zero to allow this to be used again
                    typewriter("Speed set to slow") 
                elif choice in ["2","two","normal"]:#Allows a few choiced for these settings, one to show off
                    speed = 0.03
                    loop = True
                    typewriter("Speed set to normal")
                elif choice in ["3","three","fast"]:#Allows a few choiced for these settings, one to show off
                    speed = 0.01
                    replay = 0
                    loop = True     
                    typewriter("Speed set to fast")
                elif choice in ["debug"]: # Debug speed to be 0 so its as fast as possible, this is more for my own sanity since I had to replay the code so often
                    speed = 0
                    replay = 0
                    loop = True
                else:
                    typewriter("That is not a choice")
            clear()
    def attic_loop(): #This is the loop of what to do in the attic, will not let the player continue on without their mother
        loop = False
        typewriter("Do you \n1. Help your mother\n2. Leave her to fend for herself.\n3. I'm too scared lets end here.") #This is outside the loop so it doesn't interfere with text from other options
        while loop == False:
            choice = input(">>>") #Uses a string input to allow for both letters and numbers
            choice = choice.lower() #Makes the answer lower case
            choice = choice.strip() #Strips any blank space from before or after the answer
            if choice == "settings":
                settings()
                typewriter("Do you \n1. Help your mother\n2. Leave her to fend for herself.\n3. I'm too scared lets end here.") #This is outside the loop so it doesn't interfere with text from other options

            elif  choice in ["1","one"] :
                typewriter("You try to help your mother get to the hospital")
                loop = True # Ends the loop as they have their mother
            elif choice in ["2","two"]:
                typewriter("I will ask again will you\n1. Help your mother\n2. Be heartless and leave her. \n3. This is too much responsibility, lets just end here.")#Does not end the loop, forces the player to answer "one"
            elif choice in ["3", "three"]:
                typewriter("You are very weak willed. You barely made your first choice...")
                exit()#Completely closes the game down. As a post-coding thought I wish I had planned around this better to allow a break function to work and restart the entire code loop. I could do if through a variable that is continiously checked for in each def statement
            else:#Catches any other answers
                typewriter("What are you trying to do?\nDo you \n1. Help your mother\n2. Leave her to fend for herself.\n3. I'm too scared lets end here.")

    def attic_attack(): #This will be the first zombie attack
        typewriter("Zombie attack")
        global weapon
        #Creates a loop for the combat
        global health #Pulls the health value globally
        while weapon == "None": 
            typewriter("Do you \n1. Attack now\n2. Find a weapon")
            choice = input(">>>") #Uses a string input incase anything wrong is used
            choice = choice.lower() #Makes the answer lower case
            choice = choice.strip() #Strips any blank space from before or after the answer
            if choice == "settings":
                settings() #Since the typewriter to attack is within the loop it doesnt need to be used again here
            elif choice == "1": #Try punching, it doesn't work
                typewriter ("Your fists do nothing")
                health -= 1
                typewriter (f"The zombie claws at you dealing 1 damage. Your health is now {health} ") #Shows the player their health
            elif choice == "2":
                weapons("Low-Loot") #The attic is classed as low level loot
                if weapon == "Hammer":
                    hammer_art() #This shows the hammer art easter egg
                loop = True #ends the combat loop and the function
            else:
                typewriter("That is not an option")
            if health <= 0: #When your hp is less than 0 the game ends, comes before checking if the zombie died 
                global speed 
                speed = 0.5
                dot_print(random.randint(1,10))
                typewriter("You die. ")
                exit()#Closes the programme

    def attic_fight(zombie_num): #This is the actual fight portion of the zombie attack, can be reused later in the code, used currently for all but the boss fight since that fight has a few differences
        loop = False
        zombie_art() #This calls the zombie art each time, makes the code look slightly cleaner
        global health  #Pulls the global health
        zombie_health = 2*zombie_num #Gives the zombie health, since there can be more than one zombie it will multiply it by the zombie amount
        global weapon
        global damage

        while loop == False:
            zombie_damage = random.randint(1,(zombie_health//2)+1)#This makes the zombie damage equal to the health of the zombie divided by 2 which will give a rough number of zombies left after taking damage. The +1 at the end was because a single zombie could be rounded down to 0 and then call out of range errors.
            zombie_hit = random.randint(1,4) #this is to give the zombies a 1 in 4 chance to gain a stronger attack
            zombie_miss = random.randint(1,5)#This gives the zombies a 1 in 5 chance to miss completely
            if zombie_hit == 4:
                typewriter("The zombies ready a more powerful attack, I should block this")
                zombie_damage *= 2 #The zombies gain double damage for this attack
            typewriter(f"With your {weapon} in hand, do you want to \n1. Attack\n2. Block")
            choice= input()
            choice = choice.lower() #Makes the answer lower case
            choice = choice.strip() #Strips any blank space from before or after the answer
            if choice == "settings":
                settings()
            elif choice == "1":
                typewriter(f"You swing with your {weapon} dealing {damage} damage.") #Shows the damage value and the weapon used
                zombie_health -= damage #Uses the weapon damage
                if zombie_miss != 5: #The zombie misses on a roll of a 5
                    typewriter(f"You are damaged, a zombie has bitten you, dealing {zombie_damage} damage")
                    health -= zombie_damage
                    typewriter(f"Your health is {health}")
                else:
                    typewriter("The zombies stumble, narrowly missing you")
                    typewriter(f"Your health is {health}")#The zombie misses, as such no health change is needed, shows the health just so the plaer knows
            elif choice == "2":
                block_chance = random.randint(1,10)
                if block_chance != 10:
                    typewriter("You block the attack.")#Blocking allows the player to prevent all damage that turn with a 1 in 10 chance to fail and a 1 in 3 chance to heal if successful. This is used mainly for when zombies do their stronger attacks.
                    block_chance = random.randint(1,3)
                    if block_chance == 3:
                        typewriter("While blocking this attack, you catch your breath regaining 1hp")
                        health += 1 #Blocking will have a 1 in 3 chance to heal, this was to give some more skill to the game, or at least strategy, since you can heal a small amount but  have the chance to miss the overall block
                        typewriter(f"Your health is {health}")
                else:
                    typewriter("You fumble and do not block the attack")#A small chance to miss the block and take the full damage from the zombie
                    health -= zombie_damage
                    typewriter(f"Your health is {health}")
            if health <= 0: #When your hp is less than 0 the game ends, comes before checking if the zombie died 
                global speed
                speed = 0.5
                dot_print(random.randint(1,5)) #This adds a slower speed to the type writer and prints a random amount of dots slowly, once again for DRAMATIC EFFECT
                typewriter("You died. ")
                exit()#Closes the programme
            if zombie_health <= 0:
                typewriter("The last zombie dies.")
                loop = True #Ends the loop only if the zombie is defeated




    def police_station():#This used to be part of area A, I seperated it into its own defined function to allow it to be chosen randomly
        global health
        global map
        police_title()
        typewriter("The police station has a higher intensity of zombies, however if you manage to stay safe you may be able to find better weapons and other handy materials.")
        typewriter("You have 4 zombies incoming, prepare yourself!")
        attic_fight(4) #This calls the previous fight with a total of 4 zombies
        typewriter("Wow, lucky you, you just found a medkit and healed 5 health points.")
        health +=5 #Increases the player's HP
        typewriter(f"your health is {health}") #Shows the player their health -- don't know if the typewriter function would work for this, could make a seperate function
        weapons("High-Loot")
        if weapon == "Military Knife":#This gives the knife art easter egg
            knife_art()
        map_chance = random.randint(1,2)#Since you may need more healing or want to loot more there is a 50% chance you find the map to the next area.
        if map_chance == 2: #gives a small chance to find a map
            typewriter("Well would you look at that, that's the map to West Glade, it'll point us to areas of interest before we get to the hospital.")
            map = True#Gives the player the map to extra areas


    def school():#This used to be part of area A, I seperated it into its own defined function to allow it to be chosen randomly
        global health
        school_title()#Shows the title for the school
        typewriter("This primary school has a few zombies roaming the halls. There doesnt seem to be much of use here, maybe something to bandage your wounds?.")
        typewriter("You have 2 zombies incoming, prepare yourself!")
        attic_fight(2)#A fight is called with 2 zombies total
        typewriter("Wow, lucky you, you just found a medkit and healed 8 health points.")
        health +=8 #You heal more hp but at the cost of no better weapon
        typewriter(f"your health is {health}")
        typewriter("Well would you look at that, that's the map to West Glade, it'll point us to areas of interest before we get to the hospital.")#You are guaranteed to find the map on this route. The map gives an option for even more healing or a weapon damage increase.
        global map#Uses the global map variable
        map = True#Gives the player the map to extra areas

    def area_a ():#This is the Area A now, it used to be a choice but was changed to be random. This would allow for expanding total areas and give the game more replayability. Due to time constraints we decided not to add more areas for this time.
        global health
        zombie_health = 2 #Creates zombie hp
        loop = False
        typewriter("The city Glade has many points of interest for you to explore before making your way to the hospital. Do you go to \n1. Loot one of the nearby buildings? \n2. Continue onto the hospital")#Gives the choice to loot, at the cost of health, or just continue to the boss without any upgrades
        while loop == False:
            choice = input(">>>")
            choice = choice.lower() #Makes the answer lower case
            choice = choice.strip() #Strips any blank space from before or after the answer
            if choice == "settings":
                settings()
                typewriter("\n1. Loot one of the nearby buildings? \n2. Continue onto the hospital")#Since this statement is not within the while loop it needs to be called again due to being cleared
            elif choice == "1":
                random_area = random.randint(1,3)#This chooses a random number between 1 and 3, this was to give the police station a slightly higher chance to appear
                if random_area > 1:#The police station will appear 66% of the time
                    police_station()#Calls the police station from above
                    loop = True
                    typewriter("You continue on to the hospital")
                elif random_area == 1:#The player randomly goes to the school 33% of the time
                    school() #Calls the school defined above
                    loop = True
            elif choice == "2": #If they choose to leave, they will end the loop and continue onwards to the hospital
                typewriter("You continue on to the hospital")
                loop = True
            else: 
                typewriter("What are you trying to do? \n1. Loot one of the nearby buildings? \n2. Continue onto the hospital")#Catches any other answers.

    def area_b():#Area B is setup like the original area A, giving the player a choice between a good amount of healing or a weapon upgrade and minor healing
        global map
        if map == True:#Checks if the map was gained for this area
            global health
            zombie_health = 2 #Creates zombie hp
            loop = False
            typewriter("Using the map you found you see 2 major points of interest. Who knows what could be there. \n1. The park, a fenced area you could rest \n2. The library, they do say knowledge is power, even in an apocalypse")
            while loop == False:
                choice = input(">>>")
                choice = choice.lower() #Makes the answer lower case
                choice = choice.strip() #Strips any blank space from before or after the answer
                if choice == "settings":
                    settings()
                    typewriter("Using the map you found you see 2 major points of interest. Who knows what could be there. \n1. The park, a fenced area you could rest \n2. The library, they do say knowledge is power, even in an apocalypse")#Since this statement is not within the while loop it needs to be called again due to being cleared
                elif choice == "1":#If they choose the park
                    park_title()#Displays the parks name
                    typewriter("No zombies here giving you a chance to rest") 
                    typewriter("You rest heal 10 health")#Player heals here, no zombies attack
                    health +=10 #Increases the player's HP
                    typewriter(f"your health is {health}") #Shows the player their health -- don't know if the typewriter function would work for this, could make a seperate function
                    loop = True#Ends the loop
                elif choice =="2":
                    typewriter("Glade Library")
                    library_art()#Shows art for the library
                    typewriter("We can learn about zombies.")
                    typewriter("You have 3 zombies incoming, prepare yourself!")
                    attic_fight(3)#Initiates a fight with 3 enemies
                    typewriter("You survived the horde, you can now hit harder. And feel a little healthier")
                    global damage
                    damage += 2 #Gives a flat damage increase that stacks onto the current used weapon
                    health += 3 #Increases health slightly as it was VERY likely to die from this route, but it can allow for a "glass cannon" type build with low health but very high damage
                    typewriter(f"your health is {health}")#Shows the players new health
                    typewriter("We must head to the hospital now.")
                    loop = True#Ends the loop
                else:
                    typewriter("That is not an option") #Catches any other inputs
        else:
            typewriter("We must head on to the hospital")#If there is no map then continue onto the boss fight

    def dot_print(dots):#This defines a print of dots for DRAMATIC EFFECT
        for i in range(0,dots):
            print (".", end = "")#Prints a number of dots chosen for each time this is called
            timesleep = random.randint(1,10)#uses a random number
            time.sleep(timesleep/10)#Sleeps for between 0.1 and 1 second is divided since I forgot you can do random floats and it already works

    def boss_Fight():#This is the boss fight area, it uses similar code to the previous fights but instead of making a lot of different variables previously I chose to make this one more specific here
        hospital_art()#Shows the art for the hospital
        typewriter("Finally, you see the hospital in the distance, but blocking your way is a much larger zombie")
        dot_print(random.randint(1,10))#Prints a random number of dots for the final fight
        typewriter("\nBefore you can think of a plan, the large zombie attacks")
        zombieboss_art()#Shows the zombie boss
        loop = False 
        global health  #Pulls the global health
        zombie_health = round(10 + 0.75*damage) #Gives the zombie health, scales slightly with the player's damage
        if health >=15:
            zombie_health = health//1.5 #Gives a little bit more health if the player gained a lot more health
        zombie_max = zombie_health #Saves the zombies max hp to call when it looks hurt
        while loop == False:
            zombie_damage = random.randint(0,5 + int(round(0.75*damage)))#The zombie damage will scale with player damage, it only affects the max damage not the minimum. This is to allow for higher levels of damage if the player looted for all the damage buffs
            zombie_hit = random.randint(1,4)#The boss is just as likely to do a more powerful attack, it will just do more damage
            zombie_miss = random.randint(1,8) #The boss is less likely to miss
            if zombie_health <= zombie_max/2:#Tells the player if the zombie is below half health, it took till the end for me to realise I needed to save the original max hp for the zombie
                typewriter("The zombie looks hurt, not much more to go now")
            if zombie_hit == 4:
                typewriter("The zombie readies a much more powerful attack, I should block this")
                zombie_damage *= 3 #The boss deals even more damage
            typewriter(f"With your {weapon} in hand, do you want to \n1. Attack\n2. Block")
            choice= input(">>>")
            choice = choice.lower() #Makes the answer lower case
            choice = choice.strip() #Strips any blank space from before or after the answer
            if choice == "settings":
                settings()#No need for the typewriter statement as its within the larger loop
            elif choice == "1":
                typewriter(f"You hit it with your {weapon} dealing {damage} damage")
                zombie_health -= damage #The zombie takes damage from the player based on the players base damage added to a weapon
                if zombie_miss != 8: #The zombie is less likely to miss but still can miss
                    typewriter(f"You are damaged, the zombie has bites you hard dealing {zombie_damage} damage")
                    health -= zombie_damage
                    typewriter(f"Your health is {health}")#Show the player's health
                else: 
                    typewriter("The zombie narrowly misses you")#If the zombie misses no health is lost
                    typewriter(f"Your health is {health}")
            elif choice == "2":
                block_chance = random.randint(1,10)#gives the player chance to block
                if block_chance != 10:
                    typewriter("You block the attack.")
                    block_chance = random.randint(1,3)#Randomises heal chance
                    if block_chance == 3:
                        typewriter("While blocking this attack, you catch your breath regaining 1hp")
                        health += 1#Small chance to heal
                        typewriter(f"Your health is {health}")
                else:
                    typewriter("You fumble and do not block the attack")#if missed take full damage
                    health -= zombie_damage#Catches the else which is if the miss chance was 10 and as such you fumbled and took full damage
                    typewriter(f"Your health is {health}")
            else:
                typewriter("That is not an option")
            if health <= 0: #When your hp is less than 0 the game ends, comes before checking if the zombie died 
                speed = 0.5
                dot_print(random.randint(1,5))#DRAMATIC EFFECT dots
                typewriter("You died. ")
                exit()#Closes the programme
            if zombie_health <= 0:
                typewriter("The zombie finally falls over, you have won.")
                loop = True #Ends the loop only if the zombie is defeated






    settings() #Calls the settings for the start 

    def end_game():#This is the endgame, we thought it would be kinda funny to give a random chance to have a good ending or bad ending, we could expand on it later to be if you looted too much you were too late but for the current game this should be enough
        definitely_a_skill_based_ending = random.randint(1,2)#This is 100% skill and definitely not an arbitrary 50% chance for a good or bad ending
        if definitely_a_skill_based_ending == 1:
            typewriter ("After a long day of fighting the zombie hordes, the final zombie finally dies. You make your way to the hospital to help and find the required medicine. You find a car on your way out and drive back home. Here you find your mother has already passed. Good job.")
        if definitely_a_skill_based_ending == 2:
            typewriter ("After a long day of fighting the zombie hordes, the final zombie finally dies. You make your way to the hospital to help and find the required medicine. You find a car on your way out and drive back home. Here you finally help your mother and she is now on her way to make a full recovery. Good job.")
    #The game begins
    print(r"""
     ________.__              .___       __________            ___.   .__           _________                  .__              .__   
    /  _____/|  | _____     __| _/____   \____    /____   _____\_ |__ |__| ____    /   _____/__ ____________  _|__|__  _______  |  |  
   /   \  ___|  | \__  \   / __ |/ __ \    /     //  _ \ /     \| __ \|  |/ __ \   \_____  \|  |  \_  __ \  \/ /  \  \/ /\__  \ |  |  
   \    \_\  \  |__/ __ \_/ /_/ \  ___/   /     /(  <_> )  Y Y  \ \_\ \  \  ___/   /        \  |  /|  | \/\   /|  |\   /  / __ \|  |__
    \______  /____(____  /\____ |\___  > /_______ \____/|__|_|  /___  /__|\___  > /_______  /____/ |__|    \_/ |__| \_/  (____  /____/
            \/          \/      \/    \/          \/           \/    \/        \/          \/                                  \/    
    """)


    typewriter("Welcome to Glade, the epicentre of the zombie outbreak. In this city you control yourself by typing the number of the option you wish to choose. Without any more delay we begin.\nYour mother is currently ill in the attic and needs medical supplies from the hospital. However, a zombie is walking up the stairs.") #Tutorial/intro on how the game will work, basic story setup
    replay = 0#This resets the replay to being zero, allowing the player to use their settings again, it seems late in the code but it is only just after the first settings menu is used
    #Since I defined basically everything in the game as a function the overall calling is actually fairly simple here.
    attic_loop()#Starts off calling that original attic loop asking if you will help or not *Spoiler* you have no choice.
    attic_attack()#This is misnamed but kind of works, its the starting fight where the zombie breaks inside and you need to choose a starting weapon, you can die here
    attic_fight(1)#This starts the generic zombie fights using a single zombie
    clear()#This clears all the text that took place in the starting room of the game, its not needed anymore and this will de-clutter it, also needs player input to continue
    area_a()#Runs area A with a random chance for police station or school
    clear()#Clears text from area A
    area_b()#Runs area B with a chance to miss this entirely, but gives a choice between offence and defense
    clear()#Clears text from area B
    boss_Fight()#Runs the final boss fight
    clear()#Clears boss fight spam
    end_game()#Runs the totally not random ending to the game

    typewriter("Would you like to start again, maybe try for a different ending? \n1. Yes\n2. No")#This is a seperate area I didnt see a need to define, it would only ever be used once at the end for now to ask if the winning player would like to start over
    loop_choice = False #usual loop for the player to be trapped in until a valid input is given, this is a different name since its not its own function and I didnt want variables to bleed over and overwrite one another
    while loop_choice == False:
        temp_speed = 0 #Saves a temporary state for the typewriter speed, this lets me alter it without affecting the players choice originally
        temp_speed = speed#Sets the temp speed to be the player chosen speed
        restart_choice = input(">>>") #Since this is in the main code it needs its own variable name to prevent overwriting, just incase
        restart_choice = restart_choice.lower() #Makes the answer lower case
        restart_choice = restart_choice.strip() #Strips any blank space from before or after the answer
        if restart_choice == "1":#If they choose to restart I wish them luck
            loop_choice = True#Will end the loop
            speed = 0.07#The text will run slower for the final DRAMATIC EFFECT
            typewriter("Good Luck")
            replay = 1#This sets replay to 1 so that the original settings menu will not popup again
            speed = temp_speed#Resets the slowed down speed back to the one the player chose
            clear()#Clears the console for a clean slate start
        elif restart_choice == "2":#If the player chooses no
            typewriter("Goodbye, thanks for playing")
            exit()#I could end it with a break here or something like that but I decided against it for now since I used exit() in every other case and maybe the break wouldnt work as I expect
        elif restart_choice == "settings":
            settings()#The final choice needs to check if the player chose to change their settings at the end
        else:
            typewriter("We came so far, that is still not an option, I will ask again. \n Will you \n1. Restart the game \n2 End it all here")#If they are still inputting answers wrong here this will poke a little fun