# My Day 12 Python Practice
# Name: Maham Fayyaz
# What I learned today: dictionaries 
# (create, access, add, update, delete, keys, values, items, get, 
# len, pop, clear, in, nested dictionaries)

sufi_kalam = {
    "title": "Allah Hoo",
    "poet": "Sultan Bahu",           # Create dictionary
    "language": "Punjabi",
    "genre": "Sufi Kalam",
    "theme": "Ishq-e-Haqiqi"
}
print(sufi_kalam)
print(sufi_kalam["title"])
print(sufi_kalam["theme"])

sufi_kalam["region"] = "Punjab"       # Add new key    
print(sufi_kalam)                  

sufi_kalam["language"] = "Punjabi & Urdu"  # Update value 
print(sufi_kalam)

del sufi_kalam["genre"]      # Delete key
print(sufi_kalam)

print(sufi_kalam.keys())    # keys()

print(sufi_kalam.values()) # values()

print(sufi_kalam.items())  # items()

print(sufi_kalam.get("theme"))
print(sufi_kalam.get("singer"))      # get()

for key in sufi_kalam:
    print(key)

for key, value in sufi_kalam.items():
    print(key, ":", value)    

sufi_kalams = {
    "sufi_kalam1": {
        "title": "Allah Hoo",
        "poet": "Sultan Bahu",
        "language": "Punjabi"
    },
    "sufi_kalam2": {
        "title": "Bhar Do Jhuli Meri Ya Muhammad",
        "poet": "Sabri Brothers",
        "language": "Urdu"
    }   
}
print(sufi_kalams["sufi_kalam1"]["title"])
print(sufi_kalams["sufi_kalam2"]["poet"])

for kalam, data in sufi_kalams.items():
    print(kalam)
    print(data)

for kalam, data in sufi_kalams.items():
    print("Title:", data["title"])
    print("Poet:", data["poet"])

print(len(sufi_kalams))

remove = sufi_kalams["sufi_kalam1"].pop("language") 
print(remove)
print(sufi_kalams)

sufi_kalams.clear()
print(sufi_kalams)

print("poet" in sufi_kalam)
print("singer" in sufi_kalam)

# Today's practice is complete.
# I practiced dictionaries: create, access, add, update, delete,
# keys, values, items, get, len, pop, clear, in, and nested dictionaries.