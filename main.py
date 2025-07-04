import os
from colorama import Fore, Style, init # Importing colorama for colored text output and different text styles
init(autoreset=True) # Initialize colorama and change text color automatically

if os.path.exists("students.txt") == False:
    with open("students.txt", "w") as f:
        f.write("Student Marks Manager Initialized\n")

students = []
i = 1
new_students = []
if os.path.exists("students.txt"):
    with open("students.txt","r") as f:
        lines=f.readlines()
        for line in lines:
            if "Name:" in line and "Marks:" in line:
                name = line.split("Name:")[1].split("Marks:")[0].strip()
                marks = line.split("Marks:")[1].strip("[]\n").replace(" ", "")
                marks = list(map(int, marks.split(",")))
                students.append({name: marks})

print(Fore.CYAN + "Welcome to Student Marks Manager")
while True:
    print(Fore.YELLOW + "1. Add Student")
    print(Fore.YELLOW + "2. View Students")
    print(Fore.YELLOW + "3. Update Student Marks")
    print(Fore.YELLOW + "4. Save (overwrite) and Exit")
    print(Fore.YELLOW + "5. Save(append) and Exit")
    print(Fore.YELLOW + "6. Exit without saving")
    i = int(input("Enter your choice: "))

    if(i==1):
        print(Fore.MAGENTA + "You have chosen to add a student")
        name=input("Enter student name: ")
        marks=input("Enter students marks separated by comas: ")
        marks=list(map(int, marks.split(",")))
        students.append({name:marks})
        new_students.append({name: marks})
        print(Fore.GREEN + "Student added successfully.")

    elif(i==2):
        print(Fore.MAGENTA + "You have chosen to view students")
        for student in students:
            for name,marks in student.items():
                print("Name:", name, "Marks:", marks)
                total_marks=sum(marks)
                print("Total Marks:", total_marks)
                average_marks=total_marks/len(marks)
                print("Average Marks:", average_marks)

    elif(i==3):
        print(Fore.MAGENTA + "You have chosen to update student marks")
        namei=input("Enter student name to update marks: ")
        flag=0
        for student in students:
            for name,marks in student.items():
                if(namei == name):
                    new_marks = input("Enter new marks separated by comas:")
                    new_marks = list(map(int, new_marks.split(",")))
                    student[name] = new_marks
                    flag=1
                    print(Fore.GREEN + "Marks updated successfully.")
                    break
            break
        if flag == 0:
                    print(Fore.RED + "Student not found.")

    elif(i==4):
        print(Fore.MAGENTA + "You have chosen to save(overwrite) and exit")
        with open("students.txt","w") as f:
            f.write("Student Marks Manager Initialized\n")
            for student in new_students:
                for name, marks in student.items():
                    f.write("Name:"+ name + " Marks:"+ str(marks) + "\n")
            print(Fore.GREEN + "Data saved successfully.")
        break

    elif(i==5):
         print(Fore.MAGENTA + "You have chosen to save(append) and exit")
         with open("students.txt", "a") as f:
            for student in new_students:
                for name,marks in student.items():
                    f.write("Name:" + name + " Marks:" + str(marks) + "\n")
            print(Fore.GREEN + "Data saved successfully.")
         break
    
    elif(i==6):
        print(Fore.MAGENTA + "You have chosen to exit without saving")
        break

    else:
        print(Fore.RED + "Invalid option. Please choose a valid option from the menu.")
