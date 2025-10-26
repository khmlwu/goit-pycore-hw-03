from datetime import datetime, date

def get_days_from_today(input_date: str) -> int: #Function to calculate number of days between a questioned date and today in integers.
    try: 
        target_date = datetime.strptime(input_date, "%Y-%m-%d").date() #Format a string into a date in question
    except ValueError:
        raise ValueError("Please indicate a date in YYYY-MM-DD format (Ex: 1970-01-01)")
    today = date.today() #Get today's date
    return (today - target_date).days #Calculate a difference between a date in question and today's date

print(get_days_from_today("2025-10-27")) #Print the difference