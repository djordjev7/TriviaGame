#Trivia Game
#Plays a trivia game
#4/30/15
#Djordje Vrankovic

import trivia

def main():
    trivia.Title()
    trivia.Menu()
    correct=True
    #Choices for main menu    
    while correct:
        choice=int(input("Please select an option: "))
        if choice==1:
            trivia.Rules()
            trivia.CharCreate()
            trivia.ChooseQ()
            correct=False
        elif choice==2:
            input("Press Enter to exit.")
            correct=False
        else:
            print("That isn't an option.Please choose one")
        
        
main()
