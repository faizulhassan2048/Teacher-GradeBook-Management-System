def upload_grades(self, teacher_name, grades):
    if teacher_name not in self.grade_book:
        self.grade_book[teacher_name] = grades
    else:
        self.grade_book[teacher_name].extend(grades)

def print_grade_book(self):
    for teacher, grades in self.grade_book.items():
        print(f"Teacher: {teacher}")
        for student, grade in grades.items():
            print(f"Student: {student}, Grade: {grade}")
