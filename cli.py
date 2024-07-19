import os     
import time                                                                              

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    
    ascii_art = ''' 
 d888888b d8b   db .d8888. d888888b d8888b.  .d8b.    .d8888. d88888b db    db   db      d888888b d8b   db db   dD    .d8b.  d8888b.  .d8b.  d888888b db    db  .d88b.  
  `88'   888o  88 88'  YP   `88'   88  `8D d8' `8b   88'  YP 88'     88    88   88        `88'   888o  88 88 ,8P'   d8' `8b 88  `8D d8' `8b   `88'   `8b  d8' .8P  Y8. 
   88    88V8o 88 `8bo.      88    88oobY' 88ooo88   `8bo.   88ooooo 88    88   88         88    88V8o 88 88,8P     88ooo88 88oooY' 88ooo88    88     `8bd8'  88    88 
   88    88 V8o88   `Y8b.    88    88`8b   88~~~88     `Y8b. 88~~~~~ 88    88   88         88    88 V8o88 88`8b     88~~~88 88~~~b. 88~~~88    88     .dPYb.  88    88 
  .88.   88  V888 db   8D   .88.   88 `88. 88   88   db   8D 88.     88b  d88   88booo.   .88.   88  V888 88 `88.   88   88 88   8D 88   88   .88.   .8P  Y8. `8b  d8' 
Y888888P VP   V8P `8888Y' Y888888P 88   YD YP   YP   `8888Y' Y88888P ~Y8888P'   Y88888P Y888888P VP   V8P YP   YD   YP   YP Y8888P' YP   YP Y888888P YP    YP  `Y88P'  
                                                                                                                                                                       




                                                                                               
    _ __ ___  _ _ __   ___ ___          
    | '_ ` _ \| | '_ \ / _ \ __|   
    | | | | | | | | | |  __\__ \ 
    |_| |_| |_|_|_| |_|\___|___/ 
                              
                              

                                                                                                                                                                                                                                                                       
'''
    print(ascii_art)


def select_mine():
    while True:
        user_input = input("    adicione sua url (escreva ela completo): ")
        if user_input.startswith(("https", "www")):
            
            time.sleep(1)
            print("\033[92m    suas minas estão carregando..\033[0m")
            
            time.sleep(4)
            print("\033[92m    suas minas estão carregando..\033[0m")
            
            time.sleep(3)
            print("\033[92m    carregando detalhes..\033[0m")
            
            time.sleep(1)
            print("\033[92m    verificando taxa de acertividade..\033[0m")
            
            time.sleep(4)
            print("\033[92m    suas minas estão carregando, aguarde..\033[0m")
            
            time.sleep(5)
            print("\033[92m    os quadradinhos que você deve escolher são:\033[0m")


            

            break
        else:
            print("Invalid selection. Try again!")




clear_screen()
print_ascii_art()
select_mine()
