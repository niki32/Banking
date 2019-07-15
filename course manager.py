class Course:

    def __init__(self, name, unit, term):
        self.name = name
        self.unit = unit
        self.term = term


    def addCourse(self):
        course_list = []
        self.name = input("enter class name: ")
        self.unit = int(input("Enter class units: "))
        self.term = int(input("Enter the term for this class"))
        course1 = Course(self.name, self.unit, self.term)

    def removeCourse(self):
        course_list = course1
        remove = input("Enter the course name to drop: ")
        if remove in course_list:
            course_list.pop(self.name, self.unit, self.term)
        else:
            print(self.name, " is not found in your course list.")


    def printlist (self):
        if len(course_list) == 0:
            print("No classes inputted.")
        else:
            print("no")


    def insertionSort(lst):
        for i in range(1, len(lst)):
            # insert lst[i] into a sorted sublist lst[0..i-1] so that
            #   lst[0..i] is sorted.
            currentElement = lst[i]
            k = i - 1
            while k >= 0 and lst[k] > currentElement:
                lst[k + 1] = lst[k]
                k -= 1

            # Insert the current element into lst[k + 1]
            lst[k + 1] = currentElement


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
    choice = 1
    menu()
    if choice == 1:
        Course.printlist()
    elif choice == 2:
        Course.addCourse()
