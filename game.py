# Boss: Enzo, Cousin:tony, Second seat:Freddo, Protagonist:Gio, Boss daughter: Bella, LI: Rosa, Wardrobe kid:Bruno

############ CHARACTERS OR VARIABLES  #############

protagonist= "Gio"
right_hand= "Freddo"
cousin= "Tony"
boss_daughter ="Bella"
betrothed = "Rosa"
the_boss ="Enzo"
wardrobe_dweller ="kid"

the_game = "Sicillian"

# ############## chapter 1 function creation  #########################

def chapter1_dialogue():
    print('<< Gio is a hard-faced Sicilian who was raised in the rough streets of Palermo>> ')
    print('<< He has recently become entangled in an engagement with a girl he does not want to marry>> ')
    print('<< Gio is looking to escape to new pastures in America, with his cousin>> \n')


def start_game():
    print(f" << You are playing {the_game}!!! >>\n")
    proceed=input("<<>> Press anything to continue <<>>: \n")

    print('<< The Sicilian >>')
    print('<< Welcome to The Sicilian. Its 1950. You are Giovanni Vitale or Gio as known to his close associates. >>\n')
    proceed=input("<<>> Press anything to continue <<>>: \n")


########################### chapter 2 Function creation ######################

def next_level2(): ################# THIS LEADS INTO CHAPTER 2 ####################
        print('Gio gets off the boat and onto the docks where his cousin is waiting.') ############# CHAPTER 2 STARTS HERE ################
        print('Gio gets in cousins car. He offers him a job\n')
        proceed=input("<<>> This next segment is a branching story path, be careful! Press anything to continue <<>>:\n")


        print('Type 1. Gio will go back to Sicily and marry')
        print('Type 2. Gio will say no')
        print('Type 3. Gio will say yes to the job')


##########################################


##################### BRANCHING STORY PATH CHAPTER 1 ##############################



###################################### chapter 1 options################################################


def options_number1():

        print('<<>> What should Gio do? <<>>\n')

        print('Type in 1. Go to America by Plane? (Air travel is dangerous in the 1950s)')
        print('Type in 2. Go to America by Boat? (This choice could take a very long time)')
        print('Type in 3. Stay in Sicily and Marry?')


########################################## chapter 1 optionS ELSE ERRORS ###############################################


def repeat_chapter1_options():
    chapter1_dialogue() ############### CHAPTER 1 STARTS HERE ########################
    proceed=input("<<>> This next segment is a branching story path, be careful! Press anything to continue <<>>:\n")
    
    options_number1() ####################### BRANCHING STORY PATH 1 ###########################
    
    answer=int(input())

    if (answer == 1):
        print('The Pilot was drinking and crashed into the Atlantic Ocean. You are Dead.\n')

        a = input("Would you like to try again?  Type y to try again, Type n to quit game.")

        if a == "y":
            options_number1() 
        else:          

            death_message=input("<<>> GAME OVER! you have aqcuired a tragic end! Press anything to try from the beginning <<>>:\n")
        
            repeat_chapter1_options() ############### RESTARTING GAME AT THIS POINT
    
    elif (answer == 2):
        print('<< Gio arrives in America. Sailing past the Statue of Liberty.>>\n')
        proceed=input("<<>> Press anything to continue <<>>: \n")



###############

def begin_game():

    start_game() ######## GAME START #############
    chapter1_dialogue() ############### CHAPTER 1 STARTS HERE ########################
    proceed=input("<<>> This next segment is a branching story path, be careful! Press anything to continue <<>>:\n")
    
    options_number1() ####################### BRANCHING STORY PATH 1 ###########################
    
    answer=int(input())

    if (answer == 1):
        print('The Pilot was drinking and crashed into the Atlantic Ocean. You are Dead.\n')

        a = input("Would you like to try again?  Type y to try again, Type n to quit game.")

        if a == "y":
            options_number1() 
        else:
            quit()

        death_message=input("<<>> GAME OVER! you have aqcuired a tragic end! Press anything to try from the beginning <<>>:\n")
        
        repeat_chapter1_options() ############### RESTARTING GAME AT THIS POINT
    
    elif (answer == 2):
        print('<< Gio arrives in America. Sailing past the Statue of Liberty.>>\n')
        proceed=input("<<>> Press anything to continue <<>>: \n")


        next_level2() ######################## SHOULD ALLOW PLAYER TO PROCEED ################################

    elif (answer == 3):
        print( 'Gio marries the girl he did not want to. He makes pasta his whole life and dies after a long, mundane life.\n')

        death_message=input("<<>> GAME OVER! you have aqcuired a tragic end! Press anything to try from the beginning <<>>:\n")
        begin_game() ############### RESTARTING GAME AT THIS POINT

    else :
        print('Please type in a correct response or you will make Gio angry. Either 1, 2 or 3. You idiot.\n')

        proceed=input("<<>> Press anything to continue <<>>: \n")

        repeat_chapter1_options() ############### RESTARTING GAME AT THIS POINT ( Can't figure out a way to get it to redo this one part specifically so restarting for now)



        if (answer == 1):
            print('Go back to Siciliy.')
            death_message=input("<<>> GAME OVER! you have aqcuired a tragic end! Press anything to try from the beginning <<>>:\n")
            begin_game() ############### RESTARTING GAME AT THIS POINT
        elif (answer== 2):
            print('Say no.')
        elif (answer == 3):
            print('Say yes and work for cousin.')
            begin_game()
        else:
            print('Please type in a correct response or you will make Gio angry. Either 1, 2 or 3. You idiot.\n')
        input()


begin_game() ############### USING ALL THE CODE FROM ABOVE THIS IS WHERE THE GAME ACTUALLY STARTS ########################

