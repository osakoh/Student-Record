def create_student_dictionary():
    name = input("Enter student name: ")
    student_record = {'name': name,
                      'marks': []
                      }

    return student_record


# student_mark: mark appended to the list in the student dictionary
def add_marks(student, mark):
    student['marks'].append(mark)

    # return None


def my_sum(myList):
    total = 0
    for numbers in myList:
        total = total + numbers
    return total


if __name__ == '__main__':
    s = create_student_dictionary()
    add_marks(s, 40)  # passing by reference
    print(s)

'''
A Python variable points to a memory location & the value of variable is stored in that location
Passing by reference: when a function changes the 
original value of the variable using a reference. 
'''

