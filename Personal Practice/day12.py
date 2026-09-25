# ============================================================
# DAY 12 — PYTHON DICTIONARIES
# Topic: Dictionary Basics & Nested Dictionaries
# Practice: Sufi Kalam Dictionary
# Practiced and completed by: Maham Fayyaz
# ============================================================

sufi_kalam = {
    "title" : "Allah Hoo",
    "poet" : "Sultan Bahu",           # Create Dictionary
    "language" : "Punjabi",
    "genre" : "Sufi Kalam",
    "theme" : "Ishqe Haqiqi"
}
print(sufi_kalam)
print(sufi_kalam["title"])
print(sufi_kalam["theme"])

sufi_kalam["region"] = "Punjab"        # addition metod in dictionary             
print(sufi_kalam)                  

sufi_kalam["language"] = "Punjabi & Urdu"  # data update in dictionary    
print(sufi_kalam)

del sufi_kalam["genre"]    #Data delete in dictionary method
print(sufi_kalam)

print(sufi_kalam.keys())   # key method in dictionary  

print(sufi_kalam.values()) # values method in dictionary

print(sufi_kalam.items()) # item method in dictionary 

print(sufi_kalam.get("theme"))
print(sufi_kalam.get("singer"))     #get method in dictionary

for key in sufi_kalam:
    print(key)

for key, value in sufi_kalam.items():
    print(key, ":", value)    

sufi_kalams = {
    "sufi_kalam1" : {
        "title" : "Allah Hoo",
         "poet": "Sultan Bahu",
        "language" : "Punjabi"
    },
    "sufi_kalam2" : {
        "title" : "Bhar do jhuli meri ya muhammad",
        "poet" : "Sabri Brothers",
        "language" : "Urdu"
    }   
}
print(sufi_kalams["sufi_kalam1"]["title"])
print(sufi_kalams["sufi_kalam2"]["poet"])

for kalam, data in sufi_kalams.items():
    print(kalam)
    print(data)

for kalam, data in sufi_kalams.items():
    print("Title:" , data["title"])
    print("Poet:" , data["poet"])

print(len(sufi_kalams))

remove = sufi_kalams["sufi_kalam1"].pop("language") 
print(remove)
print(sufi_kalams)

sufi_kalams.clear()
print(sufi_kalams)

print("poet" in sufi_kalam)
print("singer" in sufi_kalam)

# ============================================================
# DAY 12 DICTIONARY PRACTICE COMPLETED ✅
# Practiced: Create, Access, Add, Update, Delete,
# keys(), values(), items(), get(), len(), pop(),
# clear(), in, Loops & Nested Dictionaries.
# ============================================================