import csv
import course

csv_filename = "students.csv"
fields = ["idNum", "firstName", "lastName", "course", "yearLevel"]


def check_IDNo(idNo):
    with open(csv_filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=fields)
        for row in csvreader:
            if idNo == row["idNum"]:
                return True
                break

def check_ccode(course_code):
    with open(csv_filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=fields)
        for row in csvreader:
            if course_code == str(row["course"]).upper():
                return True
                break

def add_student():
    idNo = input("Enter Student ID number: ")
    if check_IDNo(idNo) is True:
        print("Student", idNo, "already exists.\n")
    else:
        first_name = input("Enter Student's First Name: ")
        last_name = input("Enter Student's Last Name: ")
        yr_level = input("Enter Student's Current Year Level: ")
        course_code = input("Enter Course Code (ex: BSCS for BS Computer Science): ")
        if course.check_course(course_code) is True:
            with open(csv_filename, "a", newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow([idNo, first_name, last_name, course_code, yr_level])
            print("Student added successfully!\n")
        else:
            print("Student cannot be added.\n")


def view_students():
    data = []
    with open(csv_filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=fields)
        next(csvreader)
        for row in csvreader:
            data.append(row)
    print("Course Code, Year Level, ID Number, Last Name, First Name")
    for row in data:
        print(row["course"], row["yearLevel"], row["idNum"], row["lastName"], ", ", row["firstName"])
    print()


def delete_student():
    delIDNo = input("Enter Student ID number to be deleted: ")
    data = []
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        found = False
        for row in reader:
            if row[0] == delIDNo:
                found = True
                print("Student", delIDNo, "deleted successfully!\n")
                continue
            data.append(row)
        if not found:
            print("Student", delIDNo, "not found!\n")
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def deleteByCourse(course_code):
    data = []
    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            if str(row[3]) == course_code:
                continue
            data.append(row)
    with open(csv_filename, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerows(data)


def edit_student():
    idNo = input("Enter Student ID number to be edited: ")

    with open(csv_filename, 'r') as csvfile:
        reader = csv.reader(csvfile)
        data = list(reader)

    found = False
    for i, row in enumerate(data):
        if row[0] == idNo:
            found = True
            print("Enter new student information:")
            new_first_name = input("First name: ") or data[i][1]
            new_last_name = input("Last name: ") or data[i][2]
            new_yr_level = input("Year Level: ") or data[i][4]
            new_course_code = input("Course code: ") or data[i][3]
            if course.check_course(new_course_code) is True:
                data[i] = [idNo, new_first_name, new_last_name, new_course_code, new_yr_level]
                print("Student Information edited successfully!\n")
            else:
                print("Student Information not edited.\n")
            break
    if not found:
        print("Student", idNo, "not found!\n")
    else:
        with open(csv_filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(data)


def search_student():
    search_key = input("Enter Search Key: ")
    print()
    with open(csv_filename, "r") as csvfile:
        csvreader = csv.DictReader(csvfile, fieldnames=fields)
        found = False
        next(csvreader)
        for row in csvreader:
            if search_key.lower() in str(row["idNum"]).lower() or search_key.lower() in str(row["firstName"]).lower() or search_key.lower() in str(row["lastName"]).lower() or search_key.lower() in str(row["course"]).lower() or search_key.lower() in str(row["yearLevel"]).lower():
                found = True
                print("ID Number: ", row["idNum"])
                print("First Name: ", row["firstName"])
                print("Last Name: ", row["lastName"])
                print("Year Level: ", row["yearLevel"])
                print("Course: ", row["course"], "\n")
        if not found:
            print("Student not found.\n")
