class Course:
    list = []
    list2 = []
    list3 = []
    def __init__(self, name, unit, term):
        self.name = name
        self.unit = unit
        self.term = term


    def addCourse(self):
        list = []
        list2 = []
        list3 = []
        self.name = str(input("Enter the course name: "))
        self.unit = int(input("Enter the number of units"))
        self.term = input("Enter the term you are taking this course: ")
        list.append(self.name)
        list2.append(self.unit)
        list3.append(self.term)

    def removeCourse(self):
        remove = input("Enter the course name to drop: ")
        if remove in list:
            list.pop(self.name)
        else:
            print(self.name, " is not found in your course list.")


    def printlist (self):
        print("Course", end="         ")
        print("Unit", end="        ")
        print("Term")
        print(self.name)
        print(self.unit)
        print(self.term)

    def insertionSort(lst):
        for i in range(1, len(lst)):
            # insert lst[i] into a sorted sublist lst[0..i-1] so that
            #   lst[0..i] is sorted.
            currentElement = lst[i]
            k = i - 1
            while k >= 0 and lst[k] > currentElement:
                lst[k + 1] = lst[k]
                k -= 1


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
