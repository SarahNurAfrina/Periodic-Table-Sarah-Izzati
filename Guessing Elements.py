import random

def main():    
    """HELLO AND WELCOME TO OUR GAME"""
    print("* * * *  * * * * * * * *  * * *")
    print("*HELLO AND WELCOME TO OUR GAME*")
    print("* * * *  * * * * * * * *  * * *")
    print("Start a guessing elements of the periodic table game")
    print("All the best to Guess the elements!!")
    print("You can choose the answer using the word below")
    print("** ** ** * *")
    print("* -Hydrogen*")
    print("* -Sodium  *")
    print("* -Oxygen  *") 
    print("* -Carbon  *")
    print("* -Chlorine*")
    print("* -Zinc    *")
    print("** ** ** * *")
    
    List = ["Hydrogen","Sodium","Oxygen","Carbon","Chlorine","Zinc"]
    x = random.choice(List)
    guess = None
    
    if x == "Hydrogen":
       print("Clue:petroleum refining and fertilizer production, while transportation and utilities are emerging markets.")
    elif x == "Sodium":
        print("Clue:as a heat exchanger in some nuclear reactors, and as a reagent in the chemicals industry.")
    elif x == "Oxygen":
        print ("Clue:plays a critical role in respiration, the energy-producing chemistry that drives the metabolisms of most living things.")
    elif x == "Carbon":
        print("Clue:Sugar, glucose, proteins etc are all made of it. The food we eat contains an important source of energy which we call carbohydrates")
    elif x == "Chlorine":
        print("Clue:to disinfect water and is part of the sanitation process for sewage and industrial waste.")
    elif x == "Zinc":
        print("Clue:in alloys such as brass, nickel silver and aluminium solder")
        
    
    while x != guess:
        guess = str(input("Guess the elements: "))
        
        if x == guess:
            print("**Congratulations, you are correct!!!**")

        elif x != guess:
            print("Sorry you are wrong, keep going")
    

main()