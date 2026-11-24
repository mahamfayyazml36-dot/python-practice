# Mini Project 27 - Economic Data Builder & Analyzer

This is my twenty-seventh Python mini project (Day 27 - Dictionary & Set Comprehension + Previous Concepts).

## Concepts Practiced

1. Dictionary Comprehension
2. Dictionary Filtering with Conditions
3. `.items()` and `.values()`
4. Set Comprehension
5. Nested Dictionaries
6. Economic Data Transformation
7. Data Classification
8. Conditional Expressions
9. Finding Maximum Value with `max()`
10. Structured Economic Data Analysis

## What It Does

The program takes economic data for different countries, including GDP growth, inflation, and unemployment rates.

It uses dictionary and set comprehensions to extract, filter, and transform economic data. It also classifies countries by GDP growth, finds unique values, and identifies the country with the highest GDP growth.

## Economic Analysis

- High GDP Growth → Above 2%
- High Unemployment → Above 7%
- Low Inflation → Below 3%
- High Growth → Above 3%
- Moderate Growth → 2%–3%
- Low Growth → Below 2%

## Example Output

```text
=========Economics Program=========

GDP Growth: {'poland': 3.8, 'Germany': 1.8, 'Spain': 2.7, 'Italy': 0.9, 'France': 1.2}

High Growth: {'poland': 3.8, 'Spain': 2.7}

Unique Growth: {3.8, 1.8, 2.7, 0.9, 1.2}

High Unemployment: {'Spain': 7.9, 'Italy': 8.9, 'France': 7.4}

Low Inflation: {'Germany': 2.4, 'Spain': 2.8, 'France': 2.5}

Growth Category: {
    'poland': 'High Growth',
    'Germany': 'Low Growth',
    'Spain': 'Moderate Growth',
    'Italy': 'Low Growth',
    'France': 'Low Growth'
}

Unique Category: {'High Growth', 'Moderate Growth', 'Low Growth'}

Best country: poland
GDP Growth Best Country: 3.8

=========Project Completed!=========
```
## Author

Maham Fayyaz
