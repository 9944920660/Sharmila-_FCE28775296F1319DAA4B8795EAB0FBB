class Student:

  def __init__(self, name, roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_student(student_list):
  sorted_students = sorted (student_list,
                key = lambda student: student. cgpa,
                reverse= True)
  return sorted_students


student = [
  Student("kiruthika", "A123", 7.8),
  Student("sandhiya", "A124", 8.9),
  Student("jeevitha", "A125", 9.1),
  Student("nikitha", "A126", 9.9),
]

sorted_student = sort_student (student)

for student in sorted_student:
  print("Name: {}, Roll Number: {}, CGPA: {}".format(student.name,
                                 student.roll_number,
                                             student.cgpa))