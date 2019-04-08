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

    def __init__(self, directory):
        """ Initialise university repository """

        self.university = {'student': dict(), 'instructor': dict()}
        self.directory = directory
        self.student_sum = PrettyTable()
        self.instructor_sum = PrettyTable()

        if not os.path.exists(directory):
            raise FileNotFoundError

    def add_student(self, cwid, name, major):
        """ Class method to add a student into the univeristy repository """

        self.university['student'][cwid] = Students(name, major)

    def add_instructor(self, cwid, name, department):
        """ Class method to add an instructor into the university repository """

        self.university['instructor'][cwid] = Instructors(name, department)

    def processing(self, debug=False):
        """ Class method to process data files - returns debug = True if all students and instructors were successfully added to the university repo """

        os.chdir(self.directory)
        cwd = os.getcwd()
    
        file1 = 'students.txt'
        path1 = os.path.join(cwd, file1)
        count1 = 0
        for cwid, name, major in file_reader(path1, fields=3, seperator='\t'):
            self.add_student(cwid, name, major)
            count1 += 1

        file2 = 'instructors.txt'
        path2 = os.path.join(cwd, file2)
        count2 = 0
        for instructor_cwid, instructor_name, department in file_reader(path2, fields=3, seperator='\t'):
            self.add_instructor(instructor_cwid, instructor_name, department)
            count2 += 1

        file3 = 'grades.txt'
        path3 = os.path.join(cwd, file3)
        for cwid, course_name, grades, instructor_cwid in file_reader(path3, fields=4, seperator='\t'):         
            for key, value in self.university.items():
                if key == 'student':
                    for stud_cwid, stud_info in value.items():
                        if stud_cwid == cwid:
                            stud_info.add_course(course_name, grades)

                elif key == 'instructor':
                    for inst_cwid, inst_info in value.items():
                        if inst_cwid == instructor_cwid:
                            inst_info.course_taught(course_name)

        #For test cases
        if debug:
            return len(self.university['student']), len(self.university['instructor'])
        #if count1 == len(self.university['student']) and count2 == len(self.university['instructor']):
        #    debug = True

        #return debug
        

    def student_table(self, debug=False):
        """ Function to generate Pretty Table using repository """

        self.student_sum.field_names = ["CWID", "Name", "Courses"]
        count = 0
        for key, value in self.university.items():
            if key == 'student':
                for cwid, student_info in value.items():
                    self.student_sum.add_row([cwid, student_info.name, sorted(list(student_info.courses))])
                    count += 1
        
        if debug:
            return count
        
        return self.student_sum    

    def instructor_table(self, debug=False):

        self.instructor_sum.field_names = ["CWID", "Name", "Department", "Course Name", "No. of Students"]
        count = 0
        for key, value in self.university.items():
            if key == 'instructor':
                for inst_cwid, inst_info in value.items():
                    if len(inst_info.prof_course) != 0:
                        for course_name, people in inst_info.prof_course.items():
                            self.instructor_sum.add_row([inst_cwid, inst_info.name, inst_info.department, course_name, people])
                            count += 1

        if debug:
            return count

        return self.instructor_sum


class Students:
    """ Student Class to initialize student information, add courses and display student information """

    def __init__(self, name, major):
        """ Initialise student as object with name, major, and courses as attributes """

        self.name = name
        self.major = major
        self.courses = defaultdict(str)

    def add_course(self, subj, *grade):
        """ Class method to add a course and grade """

        if grade:
            self.courses[subj] = grade[0]

        else:
            self.courses[subj]

    def __str__(self):
        """ Dunder string method to display student summary """

        return f"Name: {self.name} Major: {self.major}"


class Instructors:
    """ Instructor class to initialise instructor information, add courses taught and display instructor information """

    def __init__(self, instructor_name, department):
        """ Initialise instructor as an object with instructor name, department and courses taught as attributes """

        self.name = instructor_name
        self.department = department
        self.prof_course = defaultdict(int)

    def course_taught(self, subj):
        """Class method to add a course taught and count the number of students """

        self.prof_course[subj] += 1

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

    Stevens = University(r'C:\Users\mruna\Desktop\Stevens\data_files')
    Stevens.processing()
    print(f"Student Summary: \n{Stevens.student_table()}")
    print(f"Instructor Summary: \n{Stevens.instructor_table()}")
    

if __name__ == '__main__':
    main()
