

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
        
    

    
