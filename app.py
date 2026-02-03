from func import link_gen, nums_gen
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

i = "10"
user_path = "./found_urls"
user_w_urls = "working_urls.txt"
user_b_urls = "bad_urls.txt"


while True:
    user_input = input()
    if user_input.upper() == "HELP":
        print("""
        GUIDE: see the detailed explanation
        ITER: input the number of iterations
        FILE: input these values: <path to store files> <filename for working urls> <filename for bad urls>
        LINK: input these values: <protocol> <number of random chars> <number of random numbers> <domain> and generate
        NUMS: input the <protocol> and generate
        EXIT: close the program
        """)

    elif user_input.upper() == "GUIDE":
        print("""There will be something "_"
""")

    elif user_input.upper() == "ITER":
        i = input("(ITER)Your input:")

    elif user_input.upper() == "FILE":
        user_file = input("(FILE)Your input: ")
        user_file = user_file.split()
        user_folder = user_file[0]
        user_w_urls = user_file[1]
        user_b_urls = user_file[2]

    elif user_input.upper() == "LINK":
        link_input = input("(LINK)Your input: ")
        link_input = link_input.split()
        if len(link_input) < 1:
            print("Not enough arguments")
        else:
            try:
                link_gen(link_input+[i])
            except Exception as e:
                print(f"Something went wrong: {e}")

    elif user_input.upper() == "NUMS":
        nums_input = input("(NUMS)Your input: ")
        nums_input = nums_input.split()
        if len(nums_input) < 1:
            print("Not enough arguments")
        else:
            try:
                nums_gen(nums_input+[i])
            except Exception as e:
                print(f"Something went wrong: {e}")

    elif user_input.upper() == "EXIT":
        exit()
