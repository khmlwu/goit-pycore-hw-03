from datetime import datetime, date, timedelta  # Import needed datetime classes

def get_upcoming_birthdays(users):
    today = date.today()  # Get today's date
    date_in_seven_days = today + timedelta(days=7)  # Calculate date in 7 days from today
    upcoming_birthdays = []  # Create (an empty) list

    for user in users:  # Check every dict in the input list
        birthdate = datetime.strptime(user["birthday"], "%Y.%m.%d").date()  # Format the birthday value from each pair in a dict into YYYY.MM.DD format
        birthday_this_year = date(today.year, birthdate.month,birthdate.day)  # Determine current year's birthdate
        if birthday_this_year < today:  # Check if a current year's birthdate has passed
            birthday_this_year = date(today.year + 1,birthday_this_year.month,birthday_this_year.day)  # If passed, define next birthdate of a next year's

        if today <= birthday_this_year <= date_in_seven_days:  # Check if a birthdate is within the next 7 days
            congratulation_date = birthday_this_year  # Define congratulation date as the date of a birthdate

            if congratulation_date.weekday() == 5:  # Check if congratulation date falls on Sat
                congratulation_date += timedelta(days=2)  # If falls on Sat, move to Mon
            elif congratulation_date.weekday() == 6:  # Check if congratulation date falls on Sun
                congratulation_date += timedelta(days=1)  # If falls on Sun, move to Monday
            
            # Add a name and congratulation date to a dict in a list:
            upcoming_birthdays.append({
                "name": user["name"],
                "congratulation_date": congratulation_date.strftime("%Y.%m.%d")
            })
            
    return upcoming_birthdays
 
# Test sample:
users = [
    {"name": "Philippe de Vitry", "birthday": "1291.10.31"},
    {"name": "Howard Hanson", "birthday": "1896.10.28"},
    {"name": "Ennio Morricone", "birthday": "1928.11.10"},
    {"name": "Roger Quilter", "birthday": "1877.11.2"}
]
upcoming_birthdays = get_upcoming_birthdays(users)  # Apply the function to the Test sample
print("У таких осіб дні народження впродовж наступних 7-и днів: ", upcoming_birthdays)