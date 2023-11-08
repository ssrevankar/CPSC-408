import csv
import sqlite3
import random

conn = sqlite3.connect('StudentDB.db')
mycursor = conn.cursor()

#student advisor list
student_advisor_list = ["Seraphina Blake", "Xavier Rodriguez", "Luna Harper", "Desmond Chang", "Amara Thompson"]

#TO RESET THE DATABASE
mycursor.execute("DELETE FROM Student")
conn.commit()

with open("/Users/saniyarevankar/Downloads/students.csv", 'r') as file:
    csvreader = csv.DictReader(file)
    for row in csvreader:
        sql = "INSERT INTO Student(FirstName, LastName, Address, City, State, ZipCode, MobilePhoneNumber, Major, GPA, FacultyAdvisor, isDeleted) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?,?)"
        val = (
            row['FirstName'],
            row['LastName'],
            row['Address'],
            row['City'],
            row['State'],
            row['ZipCode'],
            row['MobilePhoneNumber'],
            row['Major'],
            row['GPA'],
            random.choice(student_advisor_list),
            0
        )
        mycursor.execute(sql, val)

conn.commit()


#make a menu prompting user for options

print ("Welcome to the Student Database.")
print ("What would you like to do?")

print ("Type 1 to Display All Students and Information.")
print ("Type 2 to Add New Students to the Database.")
print ("Type 3 to Update the Major, Advisor, Mobile Phone Number of a Specific Student.")
print ("Type 4 to Delete A Student Based off their Student ID.")
print ("Type 5 to Search/Display students by Major, GPA, City, State and Advisor.")
print ("Type 6 to Exit.")

#user should be able to choose option, lead to each query
menu_option = input("Enter your value: ")
menu_option = int(menu_option)

loop = True


# TEST TO SEE IF MENU WORKS
#print(menu_option)

while menu_option != 6:
    if menu_option == 1:
        print ("Display all students")

        # Display All
        mycursor.execute("SELECT * FROM Student WHERE isDeleted = 0")
        result = mycursor.fetchall()
        for outputs in result:
            print(outputs)
        conn.commit()

        print ("Would you like to continue? Answer Y or N")
        continue_option = input("Enter your value: ")

        if continue_option == "Y":
            print("What would you like to do?")

            print("Type 1 to Display All Students and Information.")
            print("Type 2 to Add New Students to the Database.")
            print("Type 3 to Update the Major, Advisor, Mobile Phone Number of a Specific Student.")
            print("Type 4 to Delete A Student Based off their Student ID.")
            print("Type 5 to Search/Display students by Major, GPA, City, State and Advisor.")
            print("Type 6 to Exit.")

            # user should be able to choose option, lead to each query
            menu_option = input("Enter your value: ")
            menu_option = int(menu_option)

            loop = True
        else:
            print("You are exiting the Database.")
            break

    if menu_option == 2:
        print("Add students")

        # Add New Students
        existing_student = True

        if existing_student:
            while True:
                try:
                    new_first_name = input("Enter new Student's first name: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        if existing_student:
            while True:
                try:
                    new_last_name = input("Enter new Student's last name: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        if existing_student:
            while True:
                try:
                    new_address = input("Enter new Student's address: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        if existing_student:
            while True:
                try:
                    new_city = input("Enter new Student's city: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        if existing_student:
            while True:
                try:
                    new_state = input("Enter the new Student's state: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        if existing_student:
            while True:
                try:
                    new_zipcode = input("Enter the new Student's ZipCode: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        if existing_student:
            while True:
                try:
                    new_mobile = input("Enter the new Mobile Phone Number: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        if existing_student:
            while True:
                try:
                    new_major = input("Enter the new major: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        if existing_student:
            while True:
                try:
                    new_gpa = input("Enter the new GPA: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        if existing_student:
            while True:
                try:
                    new_advisor = input("Enter the new advisor: ")
                except ValueError:
                    print("Error, Re-enter value.")
                    continue
                else:
                    break

        # Use a parameterized query to avoid SQL injection
        query = "INSERT INTO Student (FirstName, LastName, Address, City, State, Zipcode, MobilePhoneNumber, Major, FacultyAdvisor, GPA) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?,?)"

        # Tuple of values to be inserted
        values = (
        new_first_name, new_last_name, new_address, new_city, new_state, new_zipcode, new_mobile, new_major, new_advisor, new_gpa)

        mycursor.execute(query, values)
        conn.commit()


        print("Would you like to continue? Answer Y or N")
        continue_option = input("Enter your value: ")

        if continue_option == "Y":
            print("What would you like to do?")

            print("Type 1 to Display All Students and Information.")
            print("Type 2 to Add New Students to the Database.")
            print("Type 3 to Update the Major, Advisor, Mobile Phone Number of a Specific Student.")
            print("Type 4 to Delete A Student Based off their Student ID.")
            print("Type 5 to Search/Display students by Major, GPA, City, State and Advisor.")
            print("Type 6 to Exit.")

            # user should be able to choose option, lead to each query
            menu_option = input("Enter your value: ")
            menu_option = int(menu_option)

            loop = True
        else:
            print("You are exiting the Database.")
            break

    if menu_option == 3:
        print("Update students")

        # Update
        while True:
            new_first_name = input("Enter student's first name: ")
            new_last_name = input("Enter student's last name: ")

            mycursor.execute("SELECT * FROM Student WHERE FirstName = ? AND LastName = ?",
                             (new_first_name, new_last_name))

            existing_student = mycursor.fetchone()

            if existing_student:
                break  # Exit the loop if the student exists
            else:
                print("Student not found. Please try again.")

        # Now that the student exists, get the new information
        while True:
            try:
                new_major = input("Enter the new major: ")
            except ValueError:
                print("Error, Re-enter value.")
                continue
            else:
                break

        while True:
            try:
                new_advisor = input("Enter the new advisor: ")
            except ValueError:
                print("Error, Re-enter value.")
                continue
            else:
                break

        while True:
            try:
                new_mobile = input("Enter the new Mobile Phone Number: ")
            except ValueError:
                print("Error, Re-enter value.")
                continue
            else:
                break

        # Update the database with the new information
        mycursor.execute('UPDATE Student SET Major=?, Advisor=?, MobilePhoneNumber=? WHERE FirstName=? AND LastName=?',
                         (new_major, new_advisor, new_mobile, new_first_name, new_last_name))
        conn.commit()

        print("Student information updated successfully.")


        print("Would you like to continue? Answer Y or N")
        continue_option = input("Enter your value: ")

        if continue_option == "Y":
            print("What would you like to do?")

            print("Type 1 to Display All Students and Information.")
            print("Type 2 to Add New Students to the Database.")
            print("Type 3 to Update the Major, Advisor, Mobile Phone Number of a Specific Student.")
            print("Type 4 to Delete A Student Based off their Student ID.")
            print("Type 5 to Search/Display students by Major, GPA, City, State and Advisor.")
            print("Type 6 to Exit.")

            # user should be able to choose option, lead to each query
            menu_option = input("Enter your value: ")
            menu_option = int(menu_option)

            loop = True
        else:
            print("You are exiting the Database.")
            break

    if menu_option == 4:
        print("Delete students")

        # Soft delete on students -> set isDeleted to true
        # Update the isDeleted from false to true
        print ("Which student would you like to delete? Enter the student ID")
        student_option = input("Enter your value: ")
        student_option = int(student_option)

        mycursor.execute('UPDATE Student SET isDeleted =? WHERE StudentID=?', ("1", student_option))
        print("Student is deleted.")
        conn.commit()

        print("Would you like to continue? Answer Y or N")
        continue_option = input("Enter your value: ")

        if continue_option == "Y":
            print("What would you like to do?")

            print("Type 1 to Display All Students and Information.")
            print("Type 2 to Add New Students to the Database.")
            print("Type 3 to Update the Major, Advisor, Mobile Phone Number of a Specific Student.")
            print("Type 4 to Delete A Student Based off their Student ID.")
            print("Type 5 to Search/Display students by Major, GPA, City, State and Advisor.")
            print("Type 6 to Exit.")

            # user should be able to choose option, lead to each query
            menu_option = input("Enter your value: ")
            menu_option = int(menu_option)

            loop = True
        else:
            print("You are exiting the Database.")
            break

    if menu_option == 5:
        print("Display students")

        existing_student = True

        # Search/Display students by Major, GPA, City, State and Advisor
        # Order by one of they options
        print("What would you like to search by?")

        print("Type 1 to search by Major.")
        print("Type 2 to search by GPA.")
        print("Type 3 to search by City.")
        print("Type 4 to search by State.")
        print("Type 5 to search by Advisor.")

        search_option = input("Enter your value: ")
        search_option = int(search_option)
        # TEST TO SEE IF SEARCH WORKS
        # print(search_option)

        if search_option == 1:

            if existing_student:
                while True:
                    try:
                        search_major = input("Enter the major: ")
                    except ValueError:
                        print("Error, Re-enter value.")
                        continue
                    else:
                        break

            mycursor.execute(
                'SELECT FirstName, LastName, Address, City, State, Zipcode, MobilePhoneNumber, Major, GPA FROM Student WHERE Major=?',
                (search_major,))
            # Fetch the results after executing the query
            output = mycursor.fetchall()

            # Do something with the results, for example, print them
            for output in output:
                print(output)

        if search_option == 2:
            if existing_student:
                while True:
                    try:
                        search_gpa = input("Enter the GPA: ")
                    except ValueError:
                        print("Error, Re-enter value.")
                        continue
                    else:
                        break

            mycursor.execute(
                'SELECT FirstName, LastName, Address, City, State, Zipcode, MobilePhoneNumber, Major, GPA FROM Student WHERE GPA=?',
                (search_gpa,))
            # Fetch the results after executing the query
            output = mycursor.fetchall()

            # Do something with the results, for example, print them
            for output in output:
                print(output)

        if search_option == 3:
            if existing_student:
                while True:
                    try:
                        search_city = input("Enter the city: ")
                    except ValueError:
                        print("Error, Re-enter value.")
                        continue
                    else:
                        break

            mycursor.execute(
                'SELECT FirstName, LastName, Address, City, State, Zipcode, MobilePhoneNumber, Major, GPA FROM Student WHERE City=?',
                (search_city,))
            # Fetch the results after executing the query
            output = mycursor.fetchall()

            # Do something with the results, for example, print them
            for output in output:
                print(output)

        if search_option == 4:
            if existing_student:
                while True:
                    try:
                        search_state = input("Enter the state: ")
                    except ValueError:
                        print("Error, Re-enter value.")
                        continue
                    else:
                        break

            mycursor.execute(
                'SELECT FirstName, LastName, Address, City, State, Zipcode, MobilePhoneNumber, Major, GPA FROM Student WHERE State=?',
                (search_state,))
            # Fetch the results after executing the query
            output = mycursor.fetchall()

            # Do something with the results, for example, print them
            for output in output:
                print(output)

        if search_option == 5:
            if existing_student:
                while True:
                    try:
                        search_advisor = input("Enter the advisor: ")
                    except ValueError:
                        print("Error, Re-enter value.")
                        continue
                    else:
                        break

            mycursor.execute(
                'SELECT FirstName, LastName, Address, City, State, Zipcode, MobilePhoneNumber, Major, GPA FROM Student WHERE Advisor=?',
                (search_advisor,))
            # Fetch the results after executing the query
            output = mycursor.fetchall()

            # Do something with the results, for example, print them
            for output in output:
                print(output)

        else:
            print("Invalid Input")

        print("Would you like to continue? Answer Y or N")
        continue_option = input("Enter your value: ")

        if continue_option == "Y":
            print("What would you like to do?")

            print("Type 1 to Display All Students and Information.")
            print("Type 2 to Add New Students to the Database.")
            print("Type 3 to Update the Major, Advisor, Mobile Phone Number of a Specific Student.")
            print("Type 4 to Delete A Student Based off their Student ID.")
            print("Type 5 to Search/Display students by Major, GPA, City, State and Advisor.")
            print("Type 6 to Exit.")

            # user should be able to choose option, lead to each query
            menu_option = input("Enter your value: ")
            menu_option = int(menu_option)

            loop = True
        else:
            print("You are exiting the Database.")
            break
    else:
        print("You have entered an Invalid Input. Retry.")
        print("What would you like to do?")

        print("Type 1 to Display All Students and Information.")
        print("Type 2 to Add New Students to the Database.")
        print("Type 3 to Update the Major, Advisor, Mobile Phone Number of a Specific Student.")
        print("Type 4 to Delete A Student Based off their Student ID.")
        print("Type 5 to Search/Display students by Major, GPA, City, State and Advisor.")
        print("Type 6 to Exit.")

        # user should be able to choose option, lead to each query
        menu_option = input("Enter your value: ")
        menu_option = int(menu_option)
        loop = True


if menu_option == 6:
    print("You are exiting the Database.")

conn.close()



