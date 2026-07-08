# Text Analyzer Features

# Input:
# Enter a paragraph:
# Program should calculate:
# total characters
# total words
# uppercase count
# lowercase count
# numbers count
# special characters count
# unique words
print("\tWelcome to text Analyzer")
para = input("Enter you Paragraph here- ")
char_counter = 0
upper_counter = 0
lower_counter = 0
digit_counter = 0
special_counter = 0
for char in para:
    para.count(char)
    char_counter+=1

    if char.isupper() == True:
        upper_counter += 1

    if char.islower() == True:
        lower_counter += 1

    if char.isdigit() == True:
        digit_counter += 1

    if char.isalnum() == True:
        special_counter += 1

print("Total Characters- ",char_counter)
a=para.split(" ")
print("Total Words- ",len(a))
char_counter = 0 
print("Uppercase Count- ",upper_counter)
print("Lower Count- ",lower_counter)
print("Digit Count- ",digit_counter)
c=set(a)
print("Unique words- ",len(c))
'''OUTPUT - S C:\Users\Yash\OneDrive\Desktop\30DaysOfPython> & C:\Users\Yash\AppData\Local\Programs\Python\Python313\python.exe "c:/Users/Yash/OneDrive/Desktop/30DaysOfPython/Practice Project/para analyzer.py"
        Welcome to text Analyzer
Enter you Paragraph here- Python is one of the most popular programming languages in the world. Many students learn Python because it is simple, powerful, and useful for AI, web development, and automation. Yash started learning Python in 2026 and practices coding every day. Sometimes he makes mistakes, but solving problems improves his logical thinking and confidence. Python 3 is widely used in data science, machine learning, and software development!
Total Characters-  430
Total Words-  66
Uppercase Count-  9
Lower Count-  339
Digit Count-  5
Unique words-  54 '''