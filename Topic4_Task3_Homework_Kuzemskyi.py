import re

def normalize_phone(phone_number):
    phone_number = re.sub(r"[^0-9+]", "", phone_number) #Clean up the input with a phone number to only leave digits and a plus
    if phone_number.startswith("+"):
        if phone_number.startswith("+380"):
            normalized = phone_number
        else:
            normalized = f"+38{phone_number.lstrip('+')}"
    else: 
        if phone_number.startswith("380"):
            normalized = f"+{phone_number}"
        else:
            normalized = f"+38{phone_number}"
    return normalized
user_input = input("Enter a phone number: ")
print(normalize_phone(user_input))