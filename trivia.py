#Trivia Game
#Plays a trivia game
#4/30/15
#Djordje Vrankovic

import QnA
import random
from threading import Timer

Lifelines=["Hint","Ask the audience"]



#Timer with lifelines
def input_with_timeout(x,categoryQ,corrAnsw,categoryHint):    
    
    t = Timer(x,time_up) # x is amount of time in seconds
    t.start()
    try:
        print(categoryQ)
        answer = input("\nPlease choose an answer: ").lower()
    except Exception:
        print ('pass\n')
        answer = None

    if answer=="000" or answer=="111":
        if answer=="000":
            print("You used a hint")
            print("Hint: ",categoryHint)
            Lifelines.remove("Hint")
            answer = input("\nPlease choose an answer: ").lower()
            if answer ==corrAnsw:
                print("Correct")
                t.cancel()
            else:
                print("\nThat is incorrect")
                print("The correct answer was: ",corrAnsw.upper())
                t.cancel()
        if answer=="111":
            Lifelines.remove("Ask the audience")
            total=0
            while total!=100:
                if corrAnsw=="a":
                    aAudience=random.randint(50,99)
                    bAudience=random.randint(1,49)
                    cAudience=random.randint(1,49)
                    dAudience=random.randint(1,49)
                    total=aAudience+bAudience+cAudience+dAudience
                elif corrAnsw=="b":
                    aAudience=random.randint(1,49)
                    bAudience=random.randint(50,99)
                    cAudience=random.randint(1,49)
                    dAudience=random.randint(1,49)
                    total=aAudience+bAudience+cAudience+dAudience
                elif corrAnsw=="c":
                    aAudience=random.randint(1,49)
                    bAudience=random.randint(1,49)
                    cAudience=random.randint(50,100)
                    dAudience=random.randint(1,49)
                    total=aAudience+bAudience+cAudience+dAudience
                elif corrAnsw=="d":
                    aAudience=random.randint(1,49)
                    bAudience=random.randint(1,49)
                    cAudience=random.randint(1,49)
                    dAudience=random.randint(50,99)
                    total=aAudience+bAudience+cAudience+dAudience
                if total==100:
                    print("\nYou selected Ask The Audience, so let's see what they thought...","\nA. ",aAudience,"%","\nB. ",bAudience,"%","\nC. ",cAudience,"%","\nD. ",dAudience,"%")
                

            answer = input("\nPlease choose an answer: ").lower()
            if answer ==corrAnsw:
                print("Correct")
                t.cancel()
            else:
                print("\nThat is incorrect")
                print("The correct answer was: ",corrAnsw.upper())
                t.cancel()
    elif answer ==corrAnsw:
            print("Correct")
            t.cancel()
    else:
        print("\nThat is incorrect")
        print("The correct answer was: ",corrAnsw.upper())
        t.cancel()

    return answer
def time_up():
    answer= None
    print ("Time is up...\nPress enter.")


#Prints title
def Title():
    print("""
████████╗██████╗ ██╗██╗   ██╗██╗ █████╗      ██████╗  █████╗ ███╗   ███╗███████╗
╚══██╔══╝██╔══██╗██║██║   ██║██║██╔══██╗    ██╔════╝ ██╔══██╗████╗ ████║██╔════╝
   ██║   ██████╔╝██║██║   ██║██║███████║    ██║  ███╗███████║██╔████╔██║█████╗  
   ██║   ██╔══██╗██║╚██╗ ██╔╝██║██╔══██║    ██║   ██║██╔══██║██║╚██╔╝██║██╔══╝  
   ██║   ██║  ██║██║ ╚████╔╝ ██║██║  ██║    ╚██████╔╝██║  ██║██║ ╚═╝ ██║███████╗
   ╚═╝   ╚═╝  ╚═╝╚═╝  ╚═══╝  ╚═╝╚═╝  ╚═╝     ╚═════╝ ╚═╝  ╚═╝╚═╝     ╚═╝╚══════╝""")

#Prints lifeline rules
def LifeRules():
    print("""\nLifeline Rules: \n\t1.Hints: Gives you a hint
\t2. Ask the audience: Polls the audience and gives you a percentage of \n\twhat they thought""")

#Creates character
def CharCreate():
    stillGoing=True
    name=input("\nPlease enter your name: ")
    while stillGoing:
        try:
            age=int(input("Please enter your age: "))
            stillGoing=False
        except ValueError:
            print("Your age needs to be a whole number.Please enter a valid age")
    return name,age

map=["\n\nCategories:\n\tHistory","  | ","Road Rules ","|","  Geography",\
     "\n\t-------------------------------------",\
     "\n\t  Math  "," |","   Sports   ","|","  Programming",\
     "\n\t-------------------------------------",\
     "\n\t Movies "," |","   Games  ","  |","    Misc.\n"]

#Prints map
def printMap():
    for x in map:
        print(x,end="")

#Prints the numpad
def numberMap():
    print("""\n\nNumpad:
        7  | 8 | 9
	-----------
	4  | 5 | 6
	-----------
	1  | 2 | 3""")



#Prints rules
def Rules():
    print("""\nRules:\n\t1.Nine questions which you can choose
        2.Each question is a different category
        2.Twenty seconds for each question
        3.Four choices for each question
        4.Two lifelines per game
        5.Failure to answer three questions within the time, GAME OVER!!""")
    LifeRules()
    input("\nPress anything to get started.")

#Prints menu
def Menu():
    print("""
1.Start Game
2.Quit Game


""")

#Prints lifelines if still available
def DisplayLife():
    print("\nLifelines:")
    if "Hint" in Lifelines:
        print("000:","Hint")
    if "Ask the audience" in Lifelines:
        print("111:","Ask the audience")
    if Lifelines=="":
        print("No lifelines left")
    print("""\nThese are the special codes for the lifelines.If you want to use one,\n\
then type the code during the question.""")


def DisplayScore():
    print(CorrAnsw)
    print(WrongAnsw)
    score=(CorrAnsw*100)
    print(score)
def highScore():
    try:
        f=open("scores.txt", "a+")
        highScores = []
    except:
        print("OK")
            
    
        

    name = input("Enter your name:")
    playerScore = int(input("What was your score? "))
    entry = (name, playerScore)
    highScores.append(entry)
    highScores.sort(reverse=True)
    highScores = highScores[:5]     

    

#Chooses question 

def ChooseQ():
    
    CategoriesLeft=["History","RoadRules","Geography","Math","Sports","Programming","Movies"\
                    "Games","Misc"]
    stillGoing=True
    correct=0
    wrong=0
    hintsUsed=0
    while stillGoing:
        printMap()
        numberMap()
        DisplayLife()
        playerQ=int(input("\nPlease select a category using the numpad : "))
        if playerQ==7 and map[0]!="\t    X  ":
            print("You selected:",playerQ,"which is History")
            input_with_timeout(20,QnA.HistoryQ,"a",QnA.History.get("Hint"))
            map[0]="\t    X  "
        elif playerQ==8 and map[2]!="    X      ":
            print("You selected:",playerQ,"which is Road Rules")
            input_with_timeout(20,QnA.RoadRulesQ,"c",QnA.RoadRules.get("Hint"))
            map[2]="    X      "
        elif playerQ==9 and map[4]!="      X":
            print("You selected:",playerQ,"which is Geography")
            input_with_timeout(20,QnA.GeographyQ,"d",QnA.Geography.get("Hint"))
            map[4]="      X"
        elif playerQ==4 and map[6]!="\n\t    X   ":
            print("You selected:",playerQ,"which is Math")
            input_with_timeout(20,QnA.MathQ,"a",QnA.Math.get("Hint"))
            map[6]="\n\t    X   "
        elif playerQ==5 and map[8]!="     X      ":
            print("You selected:",playerQ,"which is Sports")
            input_with_timeout(20,QnA.SportsQ,"c",QnA.Sports.get("Hint"))
            map[8]="     X      "
        elif playerQ==6 and map[10]!="      X":
            print("You selected:",playerQ,"which is Programming")
            input_with_timeout(20,QnA.ProgrammingQ,"a",QnA.Programming.get("Hint"))
            map[10]="      X"
        elif playerQ==1 and map[12]!="\n\t    X   ":
            print("You selected:",playerQ,"which is Movies")
            input_with_timeout(20,QnA.MoviesQ,"b",QnA.Movies.get("Hint"))
            map[12]="\n\t    X   "
        elif playerQ==2 and map[14]!="     X    ":
            print("You selected:",playerQ,"which is Games")
            input_with_timeout(20,QnA.GamesQ,"c",QnA.Games.get("Hint"))
            map[14]="     X    "
        elif playerQ==3 and map[16]!="      X":
            print("You selected:",playerQ,"which is Misc.")
            input_with_timeout(20,QnA.MiscQ,"d",QnA.Misc.get("Hint"))
            map[16]="      X"
        elif map[0]=="\t    X  " and map[2]=="    X      " and map[4]=="      X" and map[6]=="\n\t    X   " and map[8]=="     X      " and map[10]=="      X" and map[12]=="\n\t    X   " and map[14]=="     X    " and  map[16]=="      X":
            print("Game Over")
            print("""
     ▄▄▄▄▀ ▄  █ ██      ▄   █  █▀  ▄▄▄▄▄   
  ▀▀▀ █   █   █ █ █      █  █▄█   █     ▀▄ 
      █   ██▀▀█ █▄▄█ ██   █ █▀▄ ▄  ▀▀▀▀▄   
     █    █   █ █  █ █ █  █ █  █ ▀▄▄▄▄▀    
    ▀        █     █ █  █ █   █            
            ▀     █  █   ██  ▀             """)

            input("Press enter to exit!")
            stillGoing=False
    

