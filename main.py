student_list = []


def create_student_dictionary():
    name = input("Enter student name: ")
    student_record = {'name': name,
                      'marks': []
                      }

    return student_record


# Argument mark is the mark appended to the list in the student dictionary
def add_marks(student, mark):
    student['marks'].append(mark)

    # return None


def my_sum(my_list):
    total = 0
    for numbers in my_list:
        total = total + numbers
    return total


def calculate_average(student):
    if len(student['marks']) == 0:
        return 0

    # total_marks = sum(student['marks'])
    total_marks = my_sum(student['marks'])
    average = total_marks/len(student['marks'])
    return average


def print_student_record(student):
    print("Name: {}\nMarks: {}\nAverage: {}".format(student['name'], student['marks'], calculate_average(student)))


def print_student_list(temp_list):
    for i in temp_list:
        print_student_record(i)


if __name__ == '__main__':
    s = create_student_dictionary()
    print(calculate_average(s))
    add_marks(s, 150)  # passing by reference
    print(calculate_average(s))
    add_marks(s, 30)
    print(calculate_average(s))
    print_student_record(s)
    print()

    a = create_student_dictionary()
    print(calculate_average(a))
    add_marks(a, 50)  # passing by reference
    print(calculate_average(s))
    add_marks(a, 50)
    print(calculate_average(a))
    print_student_record(a)
    print()

    print_student_list([s, a])


'''
A Python variable points to a memory location & the value of variable is stored in that location
Passing by reference: when a function changes the 
original value of the variable using a reference. 
'''

