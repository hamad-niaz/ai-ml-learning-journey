# List - 
marks = [85, 92, 78, 90]
print(marks[0]) # 85

# Dictionary -\
student = {'name':'Ali', 'marks':85, 'city':'Lahore'}
print(student['name'])

# Loop - 
for m in marks:
    if m >= 80:
        print(m, "Pass")

# Function - 
def check_pass(marks):
    return "Pass" if marks >= 50 else "Fail"

print(check_pass(85))