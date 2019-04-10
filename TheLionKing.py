"""
Author: @MrunalSalvi
SSW 810 - Homework 09 
Date: April 3, 2019 

"""

from collections import defaultdict
from prettytable import PrettyTable
import os

class University:
    """ University Class to process and store student and instructor information """

    def __init__(self, directory, pt=True):
        """ Initialise university repository """

        self.directory = directory
        os.chdir(self.directory)
        self.student = dict()
        self.instructor = dict()
        self.student_sum = PrettyTable()
        self.instructor_sum = PrettyTable()

        if not os.path.exists(self.directory):
            raise FileNotFoundError

        cwd = os.getcwd()
        file1 = 'students.txt'
        path1 = os.path.join(cwd, file1)
        for cwid, name, major in file_reader(path1, fields=3, seperator='\t'):
            self.add_student(cwid, name, major)

        file2 = 'instructors.txt'
        path2 = os.path.join(cwd, file2)
        for instructor_cwid, instructor_name, department in file_reader(path2, fields=3, seperator='\t'):
            self.add_instructor(instructor_cwid, instructor_name, department)

        file3 = 'grades.txt'
        path3 = os.path.join(cwd, file3)
        for cwid, course_name, grades, instructor_cwid in file_reader(path3, fields=4, seperator='\t'):
            for key, value in self.student.items():
                if key == cwid:
                    self.student[cwid].add_course(course_name, grades)

            for key1, value1 in self.instructor.items():
                if key1 == instructor_cwid:
                    self.instructor[instructor_cwid].course_taught(course_name)

        if pt:
            self.student_sum.field_names = Students.fields
            for studs in self.student.values():
                self.student_sum.add_row(studs.pt_row())

            self.instructor_sum.field_names = Instructors.fields
            for inst in self.instructor.values():
                for i in inst.pt_row():
                    self.instructor_sum.add_row(i)
            
            print(f"Student Summary: \n {self.student_sum}")
            print(f"Instructor Summary: \n {self.instructor_sum}")

    def add_student(self, cwid, name, major):
        """ Class method to add a student into the univeristy repository """

        self.student[cwid] = Students(cwid, name, major)

    def add_instructor(self, cwid, name, department):
        """ Class method to add an instructor into the university repository """

        self.instructor[cwid] = Instructors(cwid, name, department)

class Students:
    """ Student Class to initialize student information, add courses and display student information """

    fields = ["CWID", "Name", "Courses"]

    def __init__(self, cwid, name, major):
        """ Initialise student as object with name, major, and courses as attributes """

        self.cwid = cwid
        self.name = name
        self.major = major
        self.courses = defaultdict(str)

    def add_course(self, subj, *grade):
        """ Class method to add a course and grade """

        if grade:
            self.courses[subj] = grade[0]

        else:
            self.courses[subj]

    def pt_row(self):
        """ Class method for Pretty Table """
        
        return [self.cwid, self.name, sorted(list(self.courses))]

    def __str__(self):
        """ Dunder string method to display student summary """

        return f"Name: {self.name} Major: {self.major}"


class Instructors:
    """ Instructor class to initialise instructor information, add courses taught and display instructor information """

    fields = ["CWID", "Name", "Department", "Course Name", "No. of Students"]

    def __init__(self, instructor_cwid, instructor_name, department):
        """ Initialise instructor as an object with instructor name, department and courses taught as attributes """
        self.cwid = instructor_cwid
        self.name = instructor_name
        self.department = department
        self.prof_course = defaultdict(int)

    def course_taught(self, subj):
        """Class method to add a course taught and count the number of students """

        self.prof_course[subj] += 1

    def pt_row(self):
        """ Class method for Pretty Table """

        new_list = []
        if len(self.prof_course) != 0:
            for key, value in self.prof_course.items():
                new_list.append([self.cwid, self.name, self.department, key, value])

        return new_list

    def __str__(self):
        """ Dunder string method to display instructor information """

        return f"Name: {self.name} Department: {self.department}"

def file_reader(path, fields, seperator = ',', header = False):
    """ File Reader Function to clean a field separated file """

    try:
        fp = open(path, 'r')

    except FileNotFoundError:
        print(f"Cant Open: {path}")

    else:
        with fp:
            if header:
                next(fp)

            for num, line in enumerate(fp, 1):
                line = line.strip()

                if line.count(seperator) == fields - 1:
                    yield tuple(line.split(seperator))

                else:
                    raise ValueError(f"{path} has {line.count(seperator) + 1} fields on line {num} but expected {fields} fields")

def main():
    """ Main Function to interact with the user """

    Stevens = University(r'C:\Users\mruna\Desktop\StevensRepo\data_files')


if __name__ == '__main__':
    main()
