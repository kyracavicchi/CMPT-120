# oo scary
'''
Instructions:
We're now experts at classes, right?
Yeah?
mkay so do me a favor
Create the class student
every student has these traits:
name
student id (you can pick this number arbitrarily)
year (f/s/j/s)
major
gpa

create a function to see if the student is eligible for the honors program
to be eligible they need to have a gpa above 3.5
return true if they can and false if they cant, and print it out

create a function because this college is a wacky one- every day they generate a student id and if the student id matches a student, that student gets free food that day. 
1. generate a random number the length of however long you choose to make the id number
2. compare if the random number matches your student's id
3. if it matches print out "winner! student (name) gets free lunch!"
4. if not, print "Loser!"
(disclosure: obviously there's a very small chance of your generated number matching the student id number. I just want to see that you're generating and comparing properly)
'''


class Student:

    def __init__(self, name, studentID, year, major, gpa):
        self.name = name
        self.studentID = studentID
        self.year = year
        self.major = major
        self.gpa = gpa

    def honorsProgram(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

    import random
    randomID = random.randrange(00000, 99999)
    print(randomID)

    def freeLunch(self, randomID=None):
        if self.studentID == randomID:
            return ("Winner! {} gets free lunch!".format(self.name))
        else:
            return ("Loser!")


def main():

    # create three students and check if they get free lunch and if they qualify for honors

    student1 = Student("Kyra", 29304, "j", "math", 3.6)
    lunch = student1.freeLunch()
    print(lunch)
    honors = student1.honorsProgram()
    print(honors)

    student2 = Student("Steve", 14731, "sr", "physics", 4.0)
    lunch = student2.freeLunch()
    print(lunch)
    honors = student2.honorsProgram()
    print(honors)

    student3 = Student("Sam", 90123, "f", "biology", 3.1)
    lunch = student3.freeLunch()
    print(lunch)
    honors = student3.honorsProgram()
    print(honors)


main()
