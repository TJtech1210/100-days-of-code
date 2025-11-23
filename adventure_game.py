print(r'''
*     __                                                      
     /  l                                                     
   .'   :               __.....__..._  ____                   
  /  /   \          _.-"        "-.  ""    "-.                
 (`-: .---:    .--.'          _....J.         "-.             
  """y     \,.'    \  __..--""       `+""--.     `.           
    :     .'/    .-"""-. _.            `.   "-.    `._.._     
    ;  _.'.'  .-j       `.               \     "-.   "-._`.   
    :    / .-" :          \  `-.          `-      "-.      \  
     ;  /.'    ;          :;               ."        \      `,
     :_:/      ::\        ;:     (        /   .-"   .')      ;
       ;-"      ; "-.    /  ;           .^. .'    .' /    .-" 
      /     .-  :    `. '.  : .- / __.-j.'.'   .-"  /.---'    
     /  /      `,\.  .'   "":'  /-"   .'       \__.'          
    :  :         ,\""       ; .'    .'      .-""              
   _J  ;         ; `.      /.'    _/    \.-"                  
  /  "-:        /"--.b-..-'     .'       ;                    
 /     /  ""-..'            .--'.-'/  ,  :                    
:`.   :     / : bug         `-i" ,',_:  _ \                   
:  \  '._  :__;             .'.-"; ; ; j `.l                  
 \  \          "-._         `"  :_/ :_/                       
  `.;\             "-._                                       
    :_"-._             "-.                                    
      `.  l "-.     )     `.                                  
        ""^--""^-. :        \                                 
                  ";         \                                
                  :           `._                             
                  ; /    \ `._   ""---.                       
                 / /   _      `.--.__.'                       
                : :   / ;  :".  \                             
                ; ;  :  :  ;  `. `.                           
               /  ;  :   ; :    `. `.                         
              /  /:  ;   :  ;     "-'                         
             :_.' ;  ;    ; :                                 
                 /  /     :_l                                 
                 `-'                                          

''')
print("Welcome to Spider-Treasure Island.")
print("Your mission is to find the treasure.")
input("Press enter to continue...")

# ---- FIRST CHOICE ----
direction = input("Left or Right? ").lower()

if direction == "right":
    print("You have died. GAME OVER.")
else:
    print("You arrive at a boat.")

    # ---- SECOND CHOICE ----
    choice = input("Get on the boat or swim? ").lower()

    if choice == "swim":
        print("Oh no, you're drowning!")
        print("Wait, what is that?")
        stay = input("Stay and find out or leave? ").lower() #.lower() means that no matter the input it will come out lowercase

        if stay == "stay":
            print("It's SPIDER-MAN!!")
            ask = input("Ask SPIDER-MAN for help? Y or N ").upper() #.upper() means that no matter the input it will come out uppercase

            if ask == "Y":
                print("SPIDER-MAN drops you at the treasure. YOU WIN!")
            else:
                print("You refused help. You died.")
        else:
            print("You swam away and died. GAME OVER.")

    else:  # got on the boat
        print("The boat takes you to an island.")
        door = input("Choose a door: Red or Blue? ").lower()

        if door == "red":
            print("You found the treasure! YOU WIN!")
        else:
            print("Wrong door. You are a loser.")
