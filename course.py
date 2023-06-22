import csv
import student

csv_filename = "courses.csv"
fields = ["courseCode", "courseTitle"]

def check_course(course_code):
    course_already_added = False
    with open(csv_filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=fields)
        for row in csvreader:
            if course_code.lower() == str(row["courseCode"]).lower():
                return True
                break
    if not course_already_added:
        while True:
            print("Course not found on the list. Do you want to add it?\n[1] Yes\n[2] No")
            option1 = input("Enter your choice (1 or 2): ")
            if option1 == '1':
                add_course2(course_code)
                return True
            elif option1 == '2':
                break

def add_course():
    course_already_added = False
    course_code = input("Enter Course Code (ex: BSCS for BS Computer Science): ")
    with open(csv_filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=fields)
        for row in csvreader:
            if course_code.lower() == str(row["courseCode"]).lower():
                print("Course", course_code.upper(), "already added!\n")
                course_already_added = True
                break
    if not course_already_added:
        add_course2(course_code)


def add_course2(course_code):
    with open(csv_filename, "a", newline='') as csvfile:
        writer = csv.writer(csvfile)
        course_title = input("Enter Course Title (ex: BS Computer Science for BSCS): ")
        writer.writerow([course_code.upper(), course_title])
        print("Course added successfully!\n")


def view_course():
    data = []
    with open(csv_filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=fields)
        next(csvreader)
        for row in csvreader:
            data.append(row)
    print("Course Code, Course Title")
    for row in data:
        print(row["courseCode"], "-", row["courseTitle"])
    print()

def edit_course():
    ccode = input("Enter Course Code to be edited: ")

    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    found = False
    for i, row in enumerate(data):
        if row[0].lower() == ccode.lower():
            found = True
            new_course_title = input("Enter new Course Title (ex: BS Computer Science for BSCS): ") or data[i][1]
            data[i] = [ccode.upper(), new_course_title]
            break
    if not found:
        print("Course not found.\n")
    else:
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)
        print("Course updated successfully!\n")

def delete_course():
    delCourseCode = input("Enter Course Code to be deleted: ")
    data = []
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        found = False
        for row in reader:
            if row[0].upper() == delCourseCode.upper():
                found = True
                while True:
                    print("Are you sure to delete this course? Students under this course will also be deleted.\n[1] Yes\n[2] No")
                    option = input("Enter your choice (1-2): ")
                    if option == '1':
                        if student.check_ccode(delCourseCode.upper()) is True:
                            student.deleteByCourse(delCourseCode.upper())
                        print("Course", delCourseCode.upper(), "deleted successfully.\n")
                        break
                    elif option == '2':
                        print("Course", delCourseCode.upper(), "not deleted.\n")
                        data.append(row)
                        break
                    else:
                        print("Invalid choice.\n")
                continue
            data.append(row)
        if not found:
            print("Course", delCourseCode.upper(), "not found!\n")
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)

def search_course():
    search_key = input("Enter Search Key: ")
    print()
    with open(csv_filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=fields)
        found = False
        next(csvreader)
        lower_search_key = search_key.lower()
        for row in csvreader:
            if lower_search_key in str(row["courseCode"]).lower() or lower_search_key in str(row["courseTitle"]).lower():
                found = True
                print("Course Code: ", row["courseCode"])
                print("Course Title: ", row["courseTitle"], "\n")
        if not found:
            print("Course not found.\n")
