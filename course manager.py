course_list = []
class Course:

    def __init__(self, name, term, unit):
        self.name = name
        self.term = term
        self.unit = unit

    def __str__(self):
        return self.term, self.unit, self.name

    def __lt__(self, other):
        return self.unit < other.unit

    '''
    This function allows the user to add a course to their course list.
    '''

    def addCourse(self):
        self.name = str(input("Enter course name: "))
        course_list.append(self.name)
        self.unit = int(input("Enter class units: "))
        course_list.append(self.unit)
        self.term = (input("Enter the term for this class: "))
        course_list.append(self.term)

    '''
    This function allows the user to drop a course from their course list.
    '''

    def removeCourse(self):
        removed = input("Enter that course that you would like to remove: ")
        if removed in course_list:
            course_list.remove(self.name)
            course_list.remove(self.unit)
            course_list.remove(self.term)
        else:
            print("The course", removed, "does not exist.")

    '''
    This function allows the user to print their list.
    '''

    def printList(self):
        print("Course", end="         ")
        print("Unit", end="         ")
        print("Term")
        for x in range(len(course_list)):
            print(course_list[x],end="         ")
    '''
    This function allows the user to print their list in alphabetical order.
    '''

    def courseSort(self):
        name_list = []
        for x in course_list[::3]:
            name_list.append(x)
        name_list.sort()
        print("Course", end="         ")
        print("Unit", end="         ")
        print("Term")
        for n in range(len(name_list)):
            print(name_list[n], end="       ")

    def courseSortnum(self):
        unit_list = []
        for x in course_list[::1]:
            unit_list.append(x)
        unit_list.sort()
        print("Course", end="         ")
        print("Unit", end="         ")
        print("Term")
        for n in range(len(unit_list)):
            print(unit_list[n], end="       ")
            
'''
This function displays the menu.
'''


def menu():
    print(" ")
    print("Please choose 1 of the following options:")
    print("  1. List all courses")
    print("  2. Add a course")
    print("  3. Drop a course")
    print("  4. Sort courses based on course name")
    print("  5. Sort courses based on number of units")
    print("  6. Exit")
    print(" ")
    return eval(input("Enter your option: "))

#program starts running
loop = 1

Course1 = Course("", "", 0)

while loop == 1:
    choice = menu()
    if choice == 1: #option 1 is displayed
        if len(course_list) == 0:
            print("No classes have been inputted.")
        else:
            Course1.printList()
    elif choice == 2: #option 2 is displayed
        Course1.addCourse()
    elif choice == 3: #option 3 is displayed
        Course1.removeCourse()
    elif choice == 4: #option 4 is displayed
        print("\n")
        Course1.courseSort()
    elif choice == 5: #option 5 is displayed
        Course1.courseSortnum()
    elif choice == 6: #option 6 is displayed
        loop = 0
        print("Thank you for using the course list application")  # end the application
    elif choice <= 0:
        print("Invalid selection. Please try again.")  # error checking
    elif choice > 6:
        print("Invalid selection. Please try again.")  # error checking
