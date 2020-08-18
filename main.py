def create_student_dictionary():
    name = input("Enter student name: ")
    student_record = {'name': name,
                      'marks': []
                      }

    return student_record


if __name__ == '__main__':
    print(create_student_dictionary())