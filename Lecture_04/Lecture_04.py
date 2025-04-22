# 2. WAP to enter marks of 3 subjects from the user and store them in a dictionary. 
# Start with an empty dictionary & add one by one. USe subject name as key and key & marks as value.


marks = {}
x = int(input("Enter the phy marks: "))
marks.update({"phy": x})
x = int(input("Enter the chem marks: "))
marks.update({"chem": x})
x = int(input("Enter the math marks: "))
marks.update({"math": x})

print(marks)
