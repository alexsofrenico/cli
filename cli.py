import os     
import time                                                                              

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_ascii_art():
    
    ascii_art = ''' 
  _           _                              _ _       _            _           _           
 (_)         (_)                            | (_)     | |          | |         (_)          
  _ _ __  ___ _ _ __ __ _   ___  ___ _   _  | |_ _ __ | | __   __ _| |__   __ _ ___  _____  
 | | '_ \/ __| | '__/ _` | / __|/ _ \ | | | | | | '_ \| |/ /  / _` | '_ \ / _` | \ \/ / _ \ 
 | | | | \__ \ | | | (_| | \__ \  __/ |_| | | | | | | |    | (_| | |_) | (_| | | (_) |     |
 |_|_| |_|___/_|_|  \__,_| |___/\___|\__,_| |_|_|_| |_|_|\_\  \__,_|_.__/ \__,_|_/_/\_\___/ 




                                                                                               
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