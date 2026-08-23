# ============================================================
# Kaggle - Intro to Programming
# Day 5: Lists
# Topics Covered:
# - Creating Lists
# - List Indexing
# - List Slicing
# - len() Function
# - Adding Items using append()
# - Removing Items using remove()
# - min(), max(), and sum() Functions
# - Calculating Averages
# - Working with Lists inside Functions
# - Boolean Lists and List Comprehension
# - String split() Method
# - Practical Data Analysis with Lists
# ============================================================

flowers = ["tulip", "Rose", "lily", "sunflower"]
print(flowers)
print(type(flowers))
print(flowers[:2])
print(flowers[-3:])

favorite_things = ["Python", "Ai", "Book", "Data"]
print(favorite_things)
print(type(favorite_things))
print(favorite_things[0])
print(favorite_things[3])               #Indexing        # len()
print(favorite_things[2])
print(favorite_things[1])
print(len(favorite_things))
print(favorite_things[:3])
print(favorite_things[-2:])
favorite_things.remove("Ai")
print(favorite_things)
favorite_things.append("C++")
print(favorite_things)


sales =[120, 123, 155, 150, 156, 5500, 88555]
print(sales)
print("LENGTH:", len(sales))
print(sales[0])
print(sales[6])
print(sales[:4])
print(sales[-5:])
sales.remove(150)
print("REMOVE:", sales)
sales.append(450)
print("ADD:", sales)
print("Minimum:", min(sales))
print("Maximum:", max(sales))
print("Total:", sum(sales))


price = [ 50, 550, 500, 600, 800, 900, 2000]
average = sum(price)/len(price)
print("Average:", average)




#Question1
def percentage_growth(num_users, yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
print(percentage_growth(num_users_test, 1))
print(percentage_growth(num_users_test, 7))
#Question2
def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    percentage_liked = sum(list_liked)/len(list_liked)
    return percentage_liked
print(percentage_liked([1, 2, 3, 4, 5, 4, 5, 1]))
#Question3
test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings]
print(test_liked)
#Question2
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"
letters = alphabet.split(".")
formatted_address = address.split(",")
#Question1
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,
                 141, 148, 132, 147, 168, 153, 170, 161, 148, 152,
                 141, 151, 131, 149, 164, 163, 143, 143, 166, 171]
avg_first_seven = sum(num_customers[:7])/7 
avg_last_seven = sum(num_customers[-7:])/7
max_month = max(num_customers)
min_month = min(num_customers)
#Question1
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']
menu.remove("bean soup")
print(menu)
menu.append("roasted beet salad")
print(menu)



# ============================================================
# DAY 5 SUMMARY & KEY TAKEAWAYS
# ============================================================
# 1. Lists:
#    - Created and stored multiple values in lists.
#    - Used indexing to access individual items.
#    - Used slicing to access parts of a list.
#
# 2. List Operations:
#    - len() finds the number of items in a list.
#    - append() adds a new item to a list.
#    - remove() removes a specific item from a list.
#
# 3. Data Analysis:
#    - min() finds the smallest value.
#    - max() finds the largest value.
#    - sum() calculates the total.
#    - Used sum() and len() to calculate averages.
#
# 4. Functions with Lists:
#    - Created functions that receive lists as parameters.
#    - Performed calculations using list elements.
#
# 5. Boolean Lists:
#    - Used conditions to create True/False values in a list.
#    - Practiced basic list comprehension.
#
# 6. Strings:
#    - Used split() to divide strings into separate list items.
#
# 7. Practical Practice:
#    - Analyzed user data, ratings, customers, sales, and menu items.
#
# Status: All Kaggle Day 5 Concepts and Exercises Completed Successfully!
# ============================================================