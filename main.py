student_list = []


class Student:
    # constructor or initializer
    def __init__(self):
        self.name = "Pau"
        self.marks = []


def create_student():
    name = input("Enter student name: ")
    student_data = Student()

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


def calculate_average(student):
    if len(student.marks) == 0:
        return 0

    # total_marks = sum(student.marks)
    total_marks = my_sum(student.marks)
    average = total_marks/len(student.marks)
    return average


def individual_student_record(student):
    print("Name: {}\nMarks: {}\nAverage: {}\n".format(student.name, student.marks, calculate_average(student)))


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

