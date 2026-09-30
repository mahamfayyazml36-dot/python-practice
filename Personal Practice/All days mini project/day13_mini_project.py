# My Mini Project 13: Ghazwa-e-Uhud Data Manager
# Name: Maham Fayyaz
# What it does: View, search, update, and delete battle data
# using dictionaries + view topics using sets.
# What I learned: dictionaries (get, update, pop, items),
# sets, while loop, if-elif-else
uhud_data = {
    "name": "Ghazwa-e-Uhud",
    "location": "Madinah",
    "year": 625,
    "type": "Battle"
}

uhud_topics = {
    "Battle",
    "Madinah",
    "Quraysh",
    "Archers",
    "Martyrs"
}

while True:
    print("========== GHAZWA-E-UHUD DATA MANAGER ==========")
    print("1. View Battle Data")
    print("2. Search Battle Data")
    print("3. Update Battle Data")
    print("4. Delete Battle Data")
    print("5. View Topics")
    print("6. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        print("------Battle Data display------")
        for key, value in uhud_data.items():
            print(key, ":", value)
    elif choice == 2:    
        print("------Search Battle Data------")
        search_key = input("Enter key to search:")
        print(uhud_data.get(search_key))
    elif choice == 3:
        print("------Update Battle Data------")
        update_key = input("Enter key to update:")
        update_value = input("Enter new value:")
        uhud_data.update({update_key: update_value})
        for key, value in uhud_data.items():
            print(key, ":", value)
    elif choice == 4:
        print("------Delete Battle Data------")
        delete_key = input("Enter key to delete:")
        uhud_data.pop(delete_key)
        for key, value in uhud_data.items():
            print(key, ":", value)
    elif choice == 5:
        print("------View Topics------")
        for uhud_topic in uhud_topics:
            print(uhud_topic)
    elif choice == 6:
        print("Exiting Ghazwa-e-Uhud Data Manager")
        break
    else:
        print("Please select the correct choice (1 to 6)")

# Mini Project day 13 complete.
# This program is a menu-based battle data manager using
# dictionaries (for data) and sets (for topics).