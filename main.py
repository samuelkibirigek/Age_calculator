
"""
    This Program assumes one lives upto 90 years of age to
    tell how much time you have left to live in days, weeks and months.
    Also it will tell how long you have live in weeks, and months.
"""

print("\nNOTE: This program assumes we all live upto 90 years of age.\n")

age = int(input("Kindly enter your current age: \n"))


def time(years):
    days = int(years * 365)
    weeks = int(years * 52)
    months = int(years * 12)
    return f"{days} days, {weeks} weeks and {months} months"


word = time(age)

print(f"You have currently lived for {word}.\n")

time_left = 90 - age
left = time(time_left)

print(f"You have {left} left to live.")
