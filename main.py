student_list = []


class Student:
    # constructor or initializer
    def __init__(self, name):
        self.name = name
        self.marks = []

    def calculate_average(self):  # is the current object being used
        if len(self.marks) == 0:
            return 0

        # total_marks = sum(self.marks)
        total_marks = my_sum(self.marks)
        average = total_marks / len(self.marks)
        return average


def create_student():
    name = input("Enter student name: ")
    student_data = Student(name)  # creates new Student object using the name parameter

    return student_data


# Argument mark is the mark appended to the list in the student dictionary
def add_marks(student, mark):
    student.marks.append(mark)

    # return None


def my_sum(my_list):
    total = 0
    for numbers in my_list:
        total = total + numbers
    return total


def individual_student_record(student):
    print("Name: {}\nMarks: {}\nAverage: {}\n".format(student.name, student.marks, student.calculate_average()))


def all_student_record(temp_list):
    for index, student in enumerate(temp_list):
        print("ID: {}".format(index))
        individual_student_record(student)


def menu_options():
    print("_______________________________________\n"
          "¦____ Student Registration System ____¦\n"
          "| 1.        Create student name       |\n"
          "| 2.        Add mark to student       |\n"
          "| 3.        Print student list        |\n"
          "| 0.        Exit application          |\n"
          "|_____________________________________|")


def menu():
    menu_options()
    selection = int(input("Enter selection: "))

    while selection != 0:

        if selection == 3:
            if len(student_list) < 1:
                print("No details yet, Please create a student first!\n")
            all_student_record(student_list)
        elif selection == 1:
            student = create_student()
            student_list.append(student)
            print("{} created".format(student.name))
            menu_options()
        elif selection == 2:
            if len(student_list) < 1:
                print("Can't perform action!\n")
            else:
                for index, student in enumerate(student_list):
                    print("ID.{} -> {}".format(index, student.name))
                student_id = int(input("Select student ID: "))

                student = student_list[student_id]

                mark = int(input("Input student mark: "))

                add_marks(student, mark)
                menu_options()
        print()
        selection = int(input("Enter selection: "))


if __name__ == '__main__':
    menu()
    # s = create_student()
    # print(calculate_average(s))
    # add_marks(s, 150)  # passing by reference
    # print(calculate_average(s))
    # add_marks(s, 30)
    # print(calculate_average(s))
    # individual_student_record(s)
    # print()
    #
    # a = create_student()
    # print(calculate_average(a))
    # add_marks(a, 50)  # passing by reference
    # print(calculate_average(s))
    # add_marks(a, 50)
    # print(calculate_average(a))
    # individual_student_record(a)
    # print()
    #
    # b = create_student()
    # print(calculate_average(b))
    # add_marks(b, 100)  # passing by reference
    # print(calculate_average(s))
    # add_marks(b, 80)
    # print(calculate_average(b))
    # individual_student_record(b)
    # print()
    #
    # all_student_record([s, a, b])


'''
A Python variable points to a memory location & the value of variable is stored in that location
Passing by reference: when a function changes the 
original value of the variable using a reference. 
'''

