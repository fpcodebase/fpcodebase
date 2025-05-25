# Python program to demonstarte sorting of a list of dictionaries 

from operator import itemgetter, attrgetter

print("A simple ascending sort of a list")
print("\t", sorted([5, 2, 3, 1, 4]))

print("\n ------------------------------------------------------------------------------------------------------------------ \n")

print("\n Case-insensitive string comparison and sorted: ")
print("\t", sorted("This is a test string from Andrew".split(), key=str.casefold))

print("\n ------------------------------------------------------------------------------------------------------------------ \n")

print("\n User defined function for the key parameter -- this example sorts the list by the number closest to 10")
def myfunc(n):
    print(10-n)
    return abs(10-n)

a = (5, 3, 1, 11, 2, 12, 17)
x = sorted(a, key=myfunc)
print(x)


print("\n ------------------------------------------------------------------------------------------------------------------ \n")

print("\n Sort complex objects using some of the object's indices as keys -- List of Tuples -- sort by age")
student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'C', 10),
]

print("\t -- Using lambda as the key --- ", sorted(student_tuples, key=lambda student: student[2])) # sort by age

print("\t -- Using Operator--itemgetter one key ---", sorted(student_tuples, key=itemgetter(2)))

print("\t -- Using Operator--attrgetter two keys ---", sorted(student_tuples, key=itemgetter(1, 2)))

print("\n ------------------------------------------------------------------------------------------------------------------ \n")

print("\nSort a list of dictionaries based on key using itemgetter: ")
# Initialize the student data which is stored in a list of dictionaries
student_data = [ {'name': 'Harini', 'age': 14, 'grade': 10},
                 {'name': 'Ram', 'age': 10, 'grade': 5},
                 {'name': 'Shilpa', 'age': 12, 'grade': 7},
                 {'name': 'Vivek', 'age': 9, 'grade': 6}
                ]

# sort student data based on the age
print('\n', sorted(student_data, key = itemgetter('age')), '\n')

# sort student data by grade and then by age
print('\n', sorted(student_data, key = itemgetter('grade', 'age')), '\n')

print("\n ------------------------------------------------------------------------------------------------------------------ \n")

print("\nThe same techniques work for object with named attributes -- A class with class attributes & its instantiated objects")
class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age

    def __repr__(self):
        return repr((self.name, self.grade, self.age))
    
student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10)
]

print('\n', sorted(student_objects, key = lambda student : student.age), '\n')