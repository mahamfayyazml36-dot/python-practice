# 🐍 Day 11 — Unique Data Analyzer

## 📌 Project Overview

**Unique Data Analyzer** is a beginner-level Python mini project that analyzes product data using **Sets**.

The project takes a list of products, identifies unique products, counts duplicate entries, checks product availability, and provides an interactive data analysis menu.

## 🎯 Learning Objectives

This project was created to practice:

* Python Sets
* Converting Lists into Sets
* Removing duplicate data
* `len()` function
* Membership operator `in`
* `while` loop
* `if`, `elif`, and `else`
* `break` statement
* User input
* Basic data analysis

## 🧠 Concepts Used

### 1. List to Set

```python
unique_products = set(products)
```

Converting the product list into a set automatically removes duplicate products.

### 2. Counting Products

```python
total_products = len(products)
total_unique_products = len(unique_products)
```

These values show the total number of products and the number of unique products.

### 3. Product Availability

```python
if search_product in unique_products:
```

The `in` operator checks whether the searched product exists in the unique product set.

### 4. Duplicate Count

```python
duplicate_count = total_products - total_unique_products
```

This calculates how many duplicate entries were present in the original data.

### 5. Interactive Menu

The project uses a `while True` loop to keep the menu running until the user selects the Exit option.

## 📋 Menu Options

| Option | Function                  |
| ------ | ------------------------- |
| 1      | View Original Products    |
| 2      | View Unique Products      |
| 3      | View Total Products       |
| 4      | View Unique Product Count |
| 5      | View Duplicate Count      |
| 6      | Exit                      |

## 📦 Sample Product Data

The project uses sample martial arts and boxing products:

* Boxing Gloves
* Hand Wraps
* Shin Guards
* MMA Gloves

Some products are intentionally repeated so that the Set can remove the duplicates.

## 💡 What I Learned

Through this project, I learned how Sets can be useful for cleaning and analyzing data by removing duplicate values.

I also practiced combining Sets with Lists, conditions, user input, loops, and basic calculations to create an interactive Python program.

## 🚀 Future Improvements

Possible future improvements include:

* Add new products through the menu
* Remove products
* Search products inside the menu
* Analyze multiple product categories
* Add product prices
* Create more detailed data statistics

## 👩‍💻 Author

**Maham Fayyaz**

Python & AI Learner

**Goal:** AI Engineer → AI Architect → AI Researcher

---

### ✅ Project Status

**Day 11 — Sets: Completed**

**Mini Project: Unique Data Analyzer — Completed**

**Practiced and completed by: Maham Fayyaz**
