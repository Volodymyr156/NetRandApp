from func import link_gen
#Main Menu
import os

print("""
░███    ░██               ░██    ░█████████                               ░██    ░███                          
░████   ░██               ░██    ░██     ░██                              ░██   ░██░██                         
░██░██  ░██  ░███████  ░████████ ░██     ░██  ░██████   ░████████   ░████████  ░██  ░██  ░████████  ░████████  
░██ ░██ ░██ ░██    ░██    ░██    ░█████████        ░██  ░██    ░██ ░██    ░██ ░█████████ ░██    ░██ ░██    ░██ 
░██  ░██░██ ░█████████    ░██    ░██   ░██    ░███████  ░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██ ░██    ░██ 
░██   ░████ ░██           ░██    ░██    ░██  ░██   ░██  ░██    ░██ ░██   ░███ ░██    ░██ ░███   ░██ ░███   ░██ 
░██    ░███  ░███████      ░████ ░██     ░██  ░█████░██ ░██    ░██  ░█████░██ ░██    ░██ ░██░█████  ░██░█████  
                                                                                         ░██        ░██        
                                                                                         ░██        ░██        
                                                                                                               
Hello! This program is designed to help people find random websites on the internet so that they can discover something new. 
For further information, type 'HELP' in your terminal. :)
The input is not case-sensitive.""")


user_folder = "./found_urls"
user_w_urls = "working_urls.txt"
user_b_urls = "bad_urls.txt"


while True:
    user_input = input()

    if user_input.upper() == "HELP":
        print("""
        HINT: see some hints
        LINK: input these values: <protocol> <number of random chars> <number of random numbers> <domain> <number of iterations> and generate
        IPLINK: input these values: <protocol> 4x<number of random numbers> <domain> <number of iterations> and generate
        #CLEAR: clear the terminal
        EXIT: close the program
        """)

    elif user_input.upper() == "HINT":
        print("""HINTS:
-
""")

    elif user_input.upper() == "LINK":
        link_input = input("Your input(space is the delimiter): ")
        link_input = link_input.split()
        if len(link_input) < 5:
            print("Not valid input")
        else:
            link_gen(link_input)

    elif user_input.upper() == "EXIT":
        exit()
