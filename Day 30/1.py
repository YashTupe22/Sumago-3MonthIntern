import re
text = "The phone number is +91 86689 18164 and email is yashrtupe01@gmail.com"
phone_pattern = r'\d{2} \d{5} \d{5}'
phone = re.search(phone_pattern,text)
print(phone.group())

email_pattern = r'\b[A-Za-z0-9,_%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{2,}\b'
email = re.search(email_pattern,text)
print(email.group())
