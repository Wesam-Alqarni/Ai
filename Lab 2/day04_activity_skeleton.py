"""
Day 4 Activity: Parse nested dictionaries (student database).
Tasks:
1) Get Alice's AI301 grade
2) Calculate Bob's GPA (weighted by credits)
3) Find all students in CS101
4) Get average grade across all courses
5) Find student with highest GPA
"""
students = {
    "S001": {
        "name": "Alice Chen",
        "courses": {
            "CS101": {"grade": 92, "credits": 3},
            "MATH201": {"grade": 88, "credits": 4},
            "AI301": {"grade": 95, "credits": 3},
        },
        "advisor": "Dr. Smith",
    },
    "S002": {
        "name": "Bob Lee",
        "courses": {
            "CS101": {"grade": 85, "credits": 3},
            "MATH201": {"grade": 90, "credits": 4},
        },
        "advisor": "Dr. Patel",
    },
}
# 1) Get Alice's AI301 grade
grade = students["S001"]["courses"]["AI301"]["grade"]
print("Alice's AI301 grade:", grade)
# 2) Calculate Bob's GPA
bob_courses = students["S002"]["courses"]
points = 0
credits = 0
for course in bob_courses.values():
    points += course["grade"] * course["credits"]
    credits += course["credits"]
bob_gpa = points / credits
print("Bob's GPA:", bob_gpa)
# 3) Find all students in CS101
cs101_names = []
for student in students.values():
    if "CS101" in student["courses"]:
        cs101_names.append(student["name"])
print("Students in CS101:", cs101_names)
# 4) Get average grade across all courses
grades_list = []
for student in students.values():
    for course in student["courses"].values():
        grades_list.append(course["grade"])
average = sum(grades_list) / len(grades_list)
print("Average grade:", average)
# 5) Find student with highest GPA
best_name = ""
best_gpa = 0
for student_id, student in students.items():
    points = 0
    credits = 0         
    for course in student["courses"].values():
        points += course["grade"] * course["credits"]
        credits += course["credits"]            
    gpa = points / credits
    if gpa > best_gpa:
        best_gpa = gpa
        best_name = student["name"]
print(f"Highest GPA: {best_name} with {best_gpa:.2f}")