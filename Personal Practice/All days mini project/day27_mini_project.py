# My Day 27 Python Mini Project
# Project: Economic Data Builder & Analyzer
# What I practiced today: Dictionary & Set Comprehension, Filtering, 
# Classification, and Data Analysis
economic_data = {
    "poland" : {
        "gdp_growth" : 3.8,
        "inflation" : 4.2,
        "unemployment" : 5.2
    },
    "Germany" : {
        "gdp_growth" : 1.8 ,
        "inflation" : 2.4,
        "unemployment" : 5.9
    },
    "Spain" : {
        "gdp_growth" : 2.7,
        "inflation" : 2.8,
        "unemployment" : 7.9
    },
        "Italy": {
        "gdp_growth": 0.9,
        "inflation": 3.1,
        "unemployment": 8.9
    },
        "France": {
        "gdp_growth": 1.2,
        "inflation": 2.5,
        "unemployment": 7.4
    },
}
gdp_growth = {
    country : data["gdp_growth"]
    for country,data in economic_data.items()
}

high_growth = {
    country : growth
    for country,growth in gdp_growth.items()
    if growth > 2
}

unique_growth ={
    rate 
    for rate in gdp_growth.values()
}

high_unemployment = {
    country : data["unemployment"]
    for country,data in economic_data.items()
    if data["unemployment"] > 7
}

low_inflation = {
    country : data["inflation"]
    for country,data in economic_data.items()
    if data["inflation"] < 3
}

growth_category = {
    country: (
        "High Growth"
        if data["gdp_growth"] > 3
        else "Moderate Growth"
        if data["gdp_growth"] >= 2
        else "Low Growth"
    )
    for country, data in economic_data.items()
}



unique_categories = {
    category
    for category in growth_category.values()
}


best_country = max(
    gdp_growth,
    key=gdp_growth.get
)
print("=========Economics Program=========")
print("GDP Growth:", gdp_growth)
print("High Growth:", high_growth)
print("Unique Growth:", unique_growth)
print("High Unemployment:", high_unemployment)
print("Low Inflation:", low_inflation)
print("Growth Category:", growth_category)
print("Unique Category:",unique_categories)
print("Best country:", best_country)
print("GDP Growth Best Country:", gdp_growth[best_country])
print("=========Project Completed!=========")
# Today's practice is complete.
# Day 27 completed successfully!