#Fantasy game inventory
backpack = {"Rope" : 1,
"Knife" : 2}
TempItems = {}

def displayinventory(inventory):
    print("Inventory :")
    item_total = 0
    for k, v in inventory.items():
        print(str(v) + " " + k)
        item_total = item_total + v
    print("Item total : " + str(item_total))

def addtoinventory(inventory,addedItems):
    for k , v in addedItems.items():
        if k in inventory.keys():
            inventory[k] = inventory[k] + v
        else:
            inventory[k] = v

displayinventory(backpack)
while True :
    print("Do you wish to add an item ? Y or N, C to show the temporary inventory")
    choice = input()
    choice = choice.lower()
    if choice == "y":
        NewItem = ""
        while NewItem == "":
            print("Please add the name of your object")
            NewItem = input()
            if NewItem.isdigit():
                print("Please use at least one alphabetical letter")
            elif NewItem.isspace():
                print("Funny, please use proper names")
            elif not NewItem :
                print("Maybe write something ?")
            else:
                NewItem = NewItem.capitalize()
                TempItems[NewItem] = 0
                while TempItems[NewItem] == 0 :
                    print("Please add the amount you have")
                    NNewItem = input()
                    if NNewItem == str(0) :
                        print("Haha funny try again")
                    elif NNewItem.isdigit() :
                        TempItems[NewItem] = int(NNewItem)
                        print("You currently have ")
                        print(TempItems)
                        print("in the temporary inventory")
                        break
                    else :
                        print("Please use a number")
    elif choice == "n":
        print("Then get lost !")
        addtoinventory(backpack,TempItems)
        displayinventory(backpack)
        break
    elif choice == "c":
        displayinventory(TempItems)
        print("Do you wish to clean this up ? Y or N ")
        while choice == "c" :
            choice = input()
            choice = choice.lower()
            if choice == "y":
                print(TempItems)
                print("Please write the stuff you want gone")
                try:
                    del TempItems[input()]
                    break
                except KeyError:
                    print("Value Error, please type exactly what you need deleted.")
            elif choice == "n":
                print("Ok then.")
                break
            else :
                print("Y or N.")
                break
    else:
        print("It's not hard to press Y or N, dude.")


