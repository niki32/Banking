
class Course:
    def __init__(self, name, unit):
        self.name = name
        self.unit = unit

    def __str__(self):
        return "name: " + self.name + " unit: " + str(self.unit)

    def __lt__(self, other):
        return self.unit < other.unit

def search(course_name, lst):
    for i in range(0, len(lst)):
        if course_name == lst[i].name:
            return i

    return -1


# The function for sorting elements in ascending order
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


course_list = []
course1 = Course("CIST-4A", 4)
course2 = Course("CIST-5A", 3)
course3 = Course("ART-101", 5)

course_list.append(course1)
course_list.append(course2)
course_list.append(course3)

index = search("CIST-5B", course_list)
if index > -1:
    print("found, index = ", index)
    # change(course_list[index], "New name")
else:
    print("Not found")

course_list.sort()

course_list.pop(index)
for course in course_list:
    print(course)