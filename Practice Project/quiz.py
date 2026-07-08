# Quiz Application
# Requirements
# Features
# Ask multiple questions
# Take user answers
# Check correct/wrong
# Increase score
# Show final result

print("\tWelcome to the easie quize Quiz challenge")

print("Q1) CPU stands for -" \
"\n\t1. Central Process Unit" \
"\n\t2. Central Processing Unit" \
"\n\t3. Computer Processing Unit")

Ans = int(input("Enter your choose(No)- ")) 
if Ans == 2:
    print("Your answer is correct")
    q1 = 1
else: 
    print("Your answer is incorrect")
    q1 =0

print("Q2) HTML stands for -" \
"\n\t1. Hyper Text Markup Language" \
"\n\t2. High Text Markdown Language" \
"\n\t3. Hyper Transfer Markup Language")

Ans = int(input("Enter your choose(No)- ")) 
if Ans == 2:
    print("Your answer is correct")
    q2 =1
else: 
    print("Your answer is incorrect")
    q2=0

print("Q3) RAM stands for -" \
"\n\t1. Random Access Memory" \
"\n\t2. Read Access Memory" \
"\n\t3. Rapid Access Memory")

Ans = int(input("Enter your choose(No)- ")) 
if Ans == 1:
    print("Your answer is correct")
    q3=1
else: 
    print("Your answer is incorrect")
    q3=0

print("Q4) Python is a -" \
"\n\t1. Programming Language" \
"\n\t2. Operating System" \
"\n\t3. Web Browser")

Ans = int(input("Enter your choose(No)- ")) 
if Ans == 1:
    print("Your answer is correct")
    q4=1
else: 
    print("Your answer is incorrect")
    q4=0

print("Q5) AI stands for -" \
"\n\t1. Artificial Interface" \
"\n\t2. Artificial Intelligence" \
"\n\t3. Automated Internet")

Ans = int(input("Enter your choose(No)- ")) 
if Ans == 2:
    print("Your answer is correct")
    q5=1
else: 
    print("Your answer is incorrect")
    q5=0

total = q1+q2+q3+q4+q5

print("You have scored ",total," out of 5")