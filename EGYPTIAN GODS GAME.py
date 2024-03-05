print("""  
.______________________________________________________________________________.
|       _    _         _    _        _    _         _    _        _    _       |
|  /}    \/}/     /}    \/}/     /}   \/}/     /}    \/}/     /}   \/}/     /} |
|_/|\_    |_    _/|\_    |_    _/|\_   |_    _/|\_    |_    _/|\_   |_    _/|\_|
| / \     | \    / \     | \    / \    | \    / \     | \    / \    | \    / \ |
|vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv|
|                                                                              |
|                               EGYPTIAN GODS GAME                             |
|                                                                              |
|     _                                                                  _     |
|    /_\                                                                /_\    |
|    =|=                                                                =|=    |
|               .*.                                          .*.               |
|              ;(;);________________________________________;(;);              |
|              |;;;    _    _         _    _        _    _   ;;;|              |
|              | ;/}    \/}/     /}    \/}/     /}   \/}/    /; |              |
|              |_/|\_    |_    _/|\_    |_    _/|\_   |_   _/|\_|              |
|              | / \     | \    / \     | \    / \    | \   / \ |              |
|            __|vvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvvv|__            |
|___________|______________________________________________________|__________lc
  

""")
print("Welcome to Egyptian Gods Game.")
print("Your mission is to survive and get the power or die with the secrets.") 


print("You are walking in the Egyptian desert and you see a temple, Are you curious to enter it?")

answer1 = input("Type 'Yes' or 'No' \n").lower()
if answer1 == "yes": 
  print("""      
                   __________
                  |  __  __  |
                  | |  ||  | |
                  | |  ||  | |
                  | |__||__| |
                  |  __  __()|
                  | |  ||  | |
                  | |  ||  | |
                  | |  ||  | |
                  | |  ||  | |
                  | |__||__| |
                  |__________|   """)

  
  print("you find 2 tombs, one is red and one is blue")
  answer2 = input("Which one do you choose? Type 'red' or 'blue'\n").lower()
  if answer2 == "red":
    print("""

       +------+       +------+      
       |`.    |`.     |\     |\      
       |  `+--+---+   | +----+-+     
       |   |  |   |   | |    | |       
       +---+--+   |   +-+----+ |     
        `. |   `. |    \|     \|      
          `+------+     +------+     

    """)
    print("you found Isis, The Goddess of Magic and Wisdom, she gives you a magic wand and you use it to cast a spell and you are teleported to a room ")
    answer3 = input("You see 2 treasure boxes, one made of gold and the other made of silver, which one do you choose? Type 'gold' or 'silver'\n").lower()
    if answer3 == "silver":
      print("""

        __.-=-.            .-=-.__
          --<(_)>            <(_)>--
        *.__.'|                |'.__.* 

      """)
      
      print("You found the power of the gods, which power would you choose?")
      answer4 = input("Type 'wisdom', 'moon power' or 'strength'\n").lower()
      if answer4 == "moon power":
        print("Khonsu, the god of the moon, bless you with the power of the moon, you win!")
        print("""
                           ?
                       ____"_                   |   |
                      /"  _)))                  |\_/|______,
                     /===( _\                  /::| Q  ____)
                    ("___|   >   ,_           /:::|   /    ,_
                       o  _=    / _///       /::::|_ /    / _///
                 _______| |____/ |         _|:::::| |:___/ |
                |  __)  \_/ /____|        | '----'\_/  /___|
               _| / \    ) )             _| /  \   :  /
           _\\\__/   \    /          _\\\__/    \    /
                     /   (                      /===(
                    / \   \                    /     \
                   /   \   \                  /       \
                   |    \   \                 |        \
                   |     \   \                |         \
                   |      \   \               |,_________\
                   |       \   \               /  )  / )
                   |,_______\___\             /  /  (  |
                     | /   \ |                | /    \ |
                     |/     \|                |/      \|
                     S__     S__              S__      S__
                    /___\   /___\            /___\    /___\


        """)
      else:
        print("""
                               ... 
                             ;::::;
                           ;::::; :;
                         ;:::::'   :;
                        ;:::::;     ;.
                       ,:::::'       ;           OOO\
                       ::::::;       ;          OOOOO\
                       ;:::::;       ;         OOOOOOOO
                      ,;::::::;     ;'         / OOOOOOO
                    ;:::::::::`. ,,,;.        /  / DOOOOOO
                  .';:::::::::::::::::;,     /  /     DOOOO
                 ,::::::;::::::;;;;::::;,   /  /        DOOO
                ;`::::::`'::::::;;;::::: ,#/  /          DOOO
                :`:::::::`;::::::;;::: ;::#  /            DOOO
                ::`:::::::`;:::::::: ;::::# /              DOO
                `:`:::::::`;:::::: ;::::::#/               DOO
                 :::`:::::::`;; ;:::::::::##                OO
                 ::::`:::::::`;::::::::;:::#                OO
                 `:::::`::::::::::::;'`:;::#                O
                  `:::::`::::::::;' /  / `:#
                   ::::::`:::::;'  /  /   `#
         """ )
        print("You are a disgrace to the gods, you die. Game over")
    else:
      print("""
                             ... 
                           ;::::;
                         ;::::; :;
                       ;:::::'   :;
                      ;:::::;     ;.
                     ,:::::'       ;           OOO\
                     ::::::;       ;          OOOOO\
                     ;:::::;       ;         OOOOOOOO
                    ,;::::::;     ;'         / OOOOOOO
                  ;:::::::::`. ,,,;.        /  / DOOOOOO
                .';:::::::::::::::::;,     /  /     DOOOO
               ,::::::;::::::;;;;::::;,   /  /        DOOO
              ;`::::::`'::::::;;;::::: ,#/  /          DOOO
              :`:::::::`;::::::;;::: ;::#  /            DOOO
              ::`:::::::`;:::::::: ;::::# /              DOO
              `:`:::::::`;:::::: ;::::::#/               DOO
               :::`:::::::`;; ;:::::::::##                OO
               ::::`:::::::`;::::::::;:::#                OO
               `:::::`::::::::::::;'`:;::#                O
                `:::::`::::::::;' /  / `:#
                 ::::::`:::::;'  /  /   `#
       """ )
      print("That was the cursed box, Amun-Ra The Sun God burns you alive, Game Over") 
  else:
    print("""
                           ... 
                         ;::::;
                       ;::::; :;
                     ;:::::'   :;
                    ;:::::;     ;.
                   ,:::::'       ;           OOO\
                   ::::::;       ;          OOOOO\
                   ;:::::;       ;         OOOOOOOO
                  ,;::::::;     ;'         / OOOOOOO
                ;:::::::::`. ,,,;.        /  / DOOOOOO
              .';:::::::::::::::::;,     /  /     DOOOO
             ,::::::;::::::;;;;::::;,   /  /        DOOO
            ;`::::::`'::::::;;;::::: ,#/  /          DOOO
            :`:::::::`;::::::;;::: ;::#  /            DOOO
            ::`:::::::`;:::::::: ;::::# /              DOO
            `:`:::::::`;:::::: ;::::::#/               DOO
             :::`:::::::`;; ;:::::::::##                OO
             ::::`:::::::`;::::::::;:::#                OO
             `:::::`::::::::::::;'`:;::#                O
              `:::::`::::::::;' /  / `:#
               ::::::`:::::;'  /  /   `#
     """ )
    print("you found Anubis, The God of Death, he kills you with his scythe. GAME OVER")   
else:
  print("""
                         ... 
                       ;::::;
                     ;::::; :;
                   ;:::::'   :;
                  ;:::::;     ;.
                 ,:::::'       ;           OOO\
                 ::::::;       ;          OOOOO\
                 ;:::::;       ;         OOOOOOOO
                ,;::::::;     ;'         / OOOOOOO
              ;:::::::::`. ,,,;.        /  / DOOOOOO
            .';:::::::::::::::::;,     /  /     DOOOO
           ,::::::;::::::;;;;::::;,   /  /        DOOO
          ;`::::::`'::::::;;;::::: ,#/  /          DOOO
          :`:::::::`;::::::;;::: ;::#  /            DOOO
          ::`:::::::`;:::::::: ;::::# /              DOO
          `:`:::::::`;:::::: ;::::::#/               DOO
           :::`:::::::`;; ;:::::::::##                OO
           ::::`:::::::`;::::::::;:::#                OO
           `:::::`::::::::::::;'`:;::#                O
            `:::::`::::::::;' /  / `:#
             ::::::`:::::;'  /  /   `#
   """ )
  print("Ba-Pef, The God of Terror, he hunts you down. GAME OVER")
