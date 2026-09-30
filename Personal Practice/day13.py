# My Day 13 Python Practice
# Name: Maham Fayyaz
# What I learned today: dictionaries (revision) + sets
# (set methods: add, remove, discard, pop, clear)

surahs = {
    "surah_1": "Al-Fatihah",
    "surah_2": "Al-Baqarah",
    "surah_3": "An-Nisa",
    "surah_4": "Al-Ma'ida",
    "surah_5": "Yunus"
}
print(surahs.get("surah_3"))  # get() -> existing key of value
print(surahs.get("surah_6"))  # get() -> missing key on None (no error)
print(surahs.keys())          # keys()
print(surahs.values())        # values()
print(surahs.items())         # items()
surahs.update({"surah_6": "Al'Fat'h"}) # Add new key and value update()
print(surahs)
surahs.pop("surah_1")          # pop() with key remove specific key
print(surahs)
surahs.popitem()            # popitem() removes last inserted item
print(surahs)
surahs.clear()             # clear() empties the dictionary
print(surahs)

# Part 2 Set Methods
sultans = {
    "Osman I",
    "Orhan",
    "Murad I",
    "Bayezid I",
    "Bayezid",
    "Mehmed I",
    "Murad II",
    "MuradII",
    "Mehmed II",
    "Selim"
}
print(sultans)                # Create set (unordered, no duplicates)
sultans.add("Abdulhamid")       # add() insert new element
print(sultans)
#sultans.remove("Mustafah IV")    # remove() KeyError if not found
#print(sultans)
sultans.remove("Murad II")       # remove() existing element remove
print(sultans)
sultans.discard("Selim")        # discard() removes if exists
print(sultans)
sultans.discard("Abdulaziz")     # discard() no error if missing
print(sultans)
sultans.pop()                   # pop() removes random element
print(sultans)
sultans.clear()                # clear() empties the set
print(sultans)

# Today's practice is complete.
# I revised dictionaries (get, keys, values, items, update, pop,
# popitem, clear) and learned sets (add, remove, discard, pop, clear).
# Difference noted: remove() gives error if missing, discard() does not.