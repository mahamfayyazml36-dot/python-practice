# My Mini Project 15: Job Application Profile & Resume Analyzer
# Name: Maham Fayyaz
# What it does: Clean and validate job application information,
# remove duplicate skills, calculate project points, and format a resume profile.
# What I learned: string methods, strip, title, endswith, in, isdigit,
# len(), set, join, f-string formatting, if-else, and previous concepts.

name = "  maham fayyaz   "
email = "goalkjhs@gmail.com"
phone_number = "03025697585"
city = "  sialkot  "
career_field = "artificial intelligence"
skills = ["Python", "Git", "Machine learning", "SQL", "Python", "Git"]
project_count = 15
test_score = 85.7
clean_name = name.strip()
formatted_name = clean_name.title()
email_has_at = "@" in email
email_has_com = email.endswith(".com")
email_valid = email_has_at and email_has_com
phone_is_digit = phone_number.isdigit()
phone_length_valid = len(phone_number) == 11
phone_valid = phone_is_digit and phone_length_valid
clean_city = city.strip()
formatted_city = clean_city.title()
formatted_career_field = career_field.title()
unique_skills = set(skills)
formatted_skills = " | ".join(unique_skills)
project_points = project_count * 2
formatted_score = f"{test_score:.2f}"
score_percentage = (test_score/100)*100
formatted_percentage = f"{score_percentage:.2f}%"

if email_valid == True:
    email_status = "Valid"
else:
    email_status = "Invalid"    
if phone_valid == True:
    phone_status = "Valid"
else:
    phone_status = "Invalid"        

print("========== JOB APPLICATION PROFILE ==========")
print(f"Name: {formatted_name}\nEmail: {email}\tEmail Status: {email_status}\nPhone: {phone_number}\tPhone Status: {phone_status}\nCity: {formatted_city}\nCareer Field: {formatted_career_field}\nSkills: {formatted_skills}\nProject Completed: {project_count}\nProject Points: {project_points}\nTest Score: {formatted_score}\nAssessment Percentage: {formatted_percentage}")

# Mini Project day 15 complete.
# This program creates a Job Application Profile & Resume Analyzer
# using string methods, validation, set, join, f-string formatting,
# and previous Python concepts.
# It cleans information, validates email and phone,
# removes duplicate skills, calculates project points,
# and generates a formatted job application profile.