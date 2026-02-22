

# # create a TODO list 
# # add items
# #remov_items
# # update element
# #view element


items =[]
while True:

    print("1 to remove items")
    print("2 to remove items")
    print("3 to update items")
    print("4 to view items")
    print("5 exit from program")

    option = input("enter an option to start ")
    
    def add_element():
        add = input("enter the name of an item to be added ")
        items.append(add)
        print(f"new item added {items}")
    def remove_item():
        rem = input("enter the item name to remove ")
        try:    
           items.remove(rem)
        except :
            if rem not in items:
               print("the element to delete not found")
    def edit_element():
        edit_old = input("enter the name of item to edit ")
        edit_new = input("enter the name of item to be replace ")
        found = items.index(edit_old)
        items[found] = edit_new
        print(f"new update {items}")
        
    def view_item():
        if len(items) == 0:
            print("nothing is found on the item list")
        else:    
           print(f"all items {items}")

    if option == '1':
        add_element()
    elif option == '2':
        remove_item()
    elif option == "3":
        edit_element()
    elif option == "4":
        view_item()
    else:
        break
        
    

import random
random_num = random.randint(1,10)
guess = 0
try_guessing = 0
while True:
    uesr = int(input("make a guess to find the hidden number(1-10) "))

    if random_num > uesr:
        print("to low try again!")
        try_guessing += 1
        print(try_guessing)
    elif  uesr > random_num:
        print("to high try again!")
        try_guessing += 1
    elif random_num == uesr:
        print("you guess rightly!")
        guess =+ 1
    
    if try_guessing == 3:
        print("you can't anymore again!")
        break



while True:
    choices = ["rock","paper","scissors"]   
    abre = ["r","p","s"]
    computer = random.choice(choices)
    uesr_choice = input("Enter rock(r) paper(p) scissors(s) to start the game: ")
    uesr_choice = uesr_choice.lower()

    s = 'scissors'
    p = 'paper'
    r = 'rock' 
    
    if uesr_choice not in choices and uesr_choice not in abre:
        print("option not found! please choose either r s p")
    elif uesr_choice == 's' or 'scissors' and computer == 'rock' or uesr_choice == 'p' or 'paper' and computer == 'scissors' :
        print(f'you played {uesr_choice} and computer played {computer} and you win!')

    elif uesr_choice == 'r' or 'rock' and computer == 'scissors' or uesr_choice == 'p' or 'paper' and computer == 'rock' :
        print(f'you played {uesr_choice} and computer played {computer} and you win!')

    elif (uesr_choice == computer):
        print(f'Draw! you played {uesr_choice} and computer played {computer}')
    else:
        print(f"you played {uesr_choice} and computer played {computer} and you lose!")

    