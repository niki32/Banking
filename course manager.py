class Course:
    list = []
    list2 = []
    list3 = []
    def __init__(self, name, unit, term):
        self.name = name
        self.unit = unit
        self.term = term


    def addCourse(self):
        self.name = str(input("Enter the course name: "))
        self.unit = int(input("Enter the number of units"))
        self.term = input("Enter the term you are taking this course: ")


    #def search (self):

    #def removecourse(self):



    def printlist (self):
        print(self.name)
        print(self.unit)
        print(self.term)


def menu():
    print("Please choose 1 of the following options:")
    print("  1. List all courses")
    print("  2. Add a course")
    print("  3. Drop a course")
    print("  4. Sort courses based on course name")
    print("  5. Sort courses based on number of units")
    print("  6. Exit")
    print(" ")
    choice = input("Enter your option: ")

#program starts running
loop = 1
while loop == 1:
    choice = menu()
    if choice == 1:
        Course.printlist()
    elif choice == 2:
        Course.addCourse()