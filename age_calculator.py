
# Age Calculator

print("📅 --- Age Calculator ---")

try:
    age_years = int(input("Enter your age in years: "))
except ValueError:
    print("Please enter a valid number.")
    exit()

age_months = age_years * 12
age_days = int(age_years * 365.25)
age_hours = age_days * 24
age_minutes = age_hours * 60

print("\nYou have lived approximately:")
print(age_months, "months")
print(age_days, "days")
print(age_hours, "hours")
print(age_minutes, "minutes")
