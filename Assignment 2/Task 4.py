# 4. Skip Failed Students and Display Passed Students (Continue)
# Display only passed students by skipping failed students.

record = {
    "Yash": 80,
    "Om" : 34,
    "Atharv" : 70,
    "Kunal" : 60,
    "Ankit" : 28
}

for i,marks in record.items():
    if marks < 35:
        continue
    print(i, "passed with", marks, "marks")