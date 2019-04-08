"""
Author: @MrunalSalvi
SSW 810 - Homework 09 
Date: April 3, 2019 

"""

import unittest
from StevensRepo import University, Students, Instructors, file_reader
from prettytable import PrettyTable
from collections import defaultdict
import os

class TestStevensRepo(unittest.TestCase):
    """ Test class for the Stevens Repository System """

    def test_university_init(self):
        """ Verify if __init__ method in  University class works properly """

        Columbia = University(r'C:\Users\mruna\Desktop\Stevens\test_files')

        self.assertEqual(Columbia.university, {'student': dict(), 'instructor': dict()})
        self.assertEqual(Columbia.directory, r'C:\Users\mruna\Desktop\Stevens\test_files')
        self.assertEqual(type(Columbia.student_sum), type(PrettyTable()))
        self.assertEqual(type(Columbia.instructor_sum), type(PrettyTable()))

        with self.assertRaises(FileNotFoundError):
            Rutgers = University(r'C:\Users\mruna\Desktop\Steve')
    

    def test_university_add_student(self):
        """ Verify if add_student method in University class works properly """

        Columbia = University(r'C:\Users\mruna\Desktop\Stevens\test_files')
        
        Columbia.add_student('10440989', 'Mrunal, S', 'SFEN')
        Columbia.add_student('10445678', 'Aniruddha, P', 'CS')
        Columbia.add_student('10456789', 'Akash, D', 'MIS')

        self.assertEqual(type(Columbia.university['student']['10440989']), type(Students('Mrunal, S', 'SFEN')))
        self.assertEqual(type(Columbia.university['student']['10445678']), type(Students('Aniruddha, P', 'CS')))
        self.assertEqual(type(Columbia.university['student']['10456789']), type(Students('Akash, D', 'MIS')))

    def test_university_add_instructor(self):
        """ Verify if add_instructor method in University class works properly """

        Columbia = University(r'C:\Users\mruna\Desktop\Stevens\test_files')
        
        Columbia.add_instructor('10440989', 'Mrunal, S', 'SFEN')
        Columbia.add_instructor('10445678', 'Aniruddha, P', 'CS')
        Columbia.add_instructor('10456789', 'Akash, D', 'MIS')

        self.assertEqual(type(Columbia.university['instructor']['10440989']), type(Instructors('Mrunal, S', 'SFEN')))
        self.assertEqual(type(Columbia.university['instructor']['10445678']), type(Instructors('Aniruddha, P', 'CS')))
        self.assertEqual(type(Columbia.university['instructor']['10456789']), type(Instructors('Akash, D', 'MIS')))


    def test_university_processing(self):
        """ Verify if processing method in University class works properly """

        Columbia = University(r'C:\Users\mruna\Desktop\Stevens\test_files')

        student, instructor = Columbia.processing(debug=True)

        self.assertEqual(student, 10)
        self.assertEqual(instructor, 6)
        self.assertNotEqual(student, 11)
        self.assertNotEqual(instructor, 7)

    def test_university_student_table(self):
        """ Verify if student_table method in University class works properly """

        Columbia = University(r'C:\Users\mruna\Desktop\Stevens\test_files')
        Columbia.processing()

        self.assertEqual(Columbia.student_table(debug=True), 10)
        self.assertNotEqual(Columbia.student_table(debug=True), 11)

    def test_university_instructor_table(self):
        """ Verify if instructor_table method in University class works properly """

        Columbia = University(r'C:\Users\mruna\Desktop\Stevens\test_files')
        Columbia.processing()

        self.assertEqual(Columbia.instructor_table(debug=True), 12)
        self.assertNotEqual(Columbia.instructor_table(debug=True), 13)

    def test_student_init(self):
        """ Verify if __init__ method in Student class works properly """

        student1 = Students('Mrunal, S', 'SFEN')
        self.assertEqual(student1.name, 'Mrunal, S')
        self.assertEqual(student1.major, 'SFEN')
        self.assertEqual(type(student1.courses), type(defaultdict()))
        
        student2 = Students('Anirudha, P', 'CS')
        self.assertEqual(student2.name, 'Anirudha, P')
        self.assertEqual(student2.major, 'CS')
        self.assertEqual(type(student1.courses), type(defaultdict()))

    def test_student_add_course(self):
        """ Verify if add_course method in Student class works properly """

        student = Students('Mrunal, S', 'SFEN')
        student.add_course('SSW 810', 'A')
        student.add_course('SSW 540', 'A-')
        student.add_course('SSW 564')
        self.assertEqual(student.courses['SSW 810'], 'A')
        self.assertEqual(student.courses['SSW 540'], 'A-')
        self.assertEqual(student.courses['SSW 564'], '')
        self.assertNotEqual(student.courses['SSW 564'], 'A')

    def test_student_str(self):
        """ Verify if __str__ method in Student Class works properly """

        student = Students('Mrunal, S', 'SFEN')
        self.assertEqual(str(student), f'Name: {student.name} Major: {student.major}')

    def test_instructor_init(self):
        """ Verify if __init__ method in Instructor class works properly """

        instructor = Instructors('Mrunal, S', 'SFEN')
        self.assertEqual(instructor.name, 'Mrunal, S')
        self.assertEqual(instructor.department, 'SFEN')
        self.assertEqual(type(instructor.prof_course), type(defaultdict()))


    def test_instructor_course_taught(self):
        """ Verify if add_course method in Instructor class works properly """

        instructor = Instructors('Mrunal, S', 'SFEN')
        instructor.course_taught('SSW 810')
        instructor.course_taught('SSW 810')
        instructor.course_taught('SSW 564')
        self.assertEqual(instructor.prof_course['SSW 810'], 2)
        self.assertEqual(instructor.prof_course['SSW 564'], 1)
        self.assertNotEqual(instructor.prof_course['SSW 564'], 0)

    def test_instructor_str(self):
        """ Verify if __str__ method in Instructor class works properly """

        instructor = Instructors('Mrunal, S', 'SFEN')
        self.assertEqual(str(instructor), f'Name: {instructor.name} Department: {instructor.department}')


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
