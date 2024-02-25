class Student:
    def __init__(self, name, student_ID, age, gender):
        self.name = name
        self.student_ID = student_ID
        self.age = age
        self.gender = gender
        
    def set_grade(self, grade):
        self.grade = grade
    
    def get_grade(self):
        print(self.grade)
        
    def display_student_info(self):
        print(f'name:{self.name}, ID:{self.student_ID}, age:{self.age}, gender:{self.gender}, grade:{self.grade}')
        
stu1 = Student("John", 121111, 18, 'male')
stu1.set_grade(56)
stu1.display_student_info()