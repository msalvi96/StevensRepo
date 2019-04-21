"""
Author: @MrunalSalvi
SSW 810 - Homework 09 
Date: April 3, 2019 

"""

import unittest
from TheLionKing import University, Students, Instructors, file_reader
from prettytable import PrettyTable
from collections import defaultdict
import os

class TestStevensRepo(unittest.TestCase):
    """ Test class for the Stevens Repository System """

    def test_university_init(self):
        """ Verify if __init__ method in  University class works properly """

        Columbia = University(r'C:\Users\mruna\Desktop\StevensRepo', web=True)

        self.assertEqual(Columbia.directory, r'C:\Users\mruna\Desktop\StevensRepo')
        self.assertEqual(type(Columbia.student), type(dict()))
        self.assertEqual(type(Columbia.instructor), type(dict()))
        self.assertEqual(type(Columbia.majors), type(defaultdict(lambda: defaultdict(list))))
        self.assertEqual(type(Columbia.student_data), type(list()))
        self.assertEqual(type(Columbia.instructor_data), type(list()))

        with self.assertRaises(FileNotFoundError):
            Rutgers = University(r'C:\Users\mruna\Desktop\Steve')

    def test_university_add_student(self):
        """ Verify if add_student method in University class works properly """

        Columbia = University(r'C:\Users\mruna\Desktop\StevensRepo', pt=False) 
        Columbia.add_student('10440989', 'Mrunal, S', 'SFEN')
        Columbia.add_student('10445678', 'Aniruddha, P', 'CS')
        Columbia.add_student('10456789', 'Akash, D', 'MIS')

        self.assertEqual(type(Columbia.student['10440989']), type(Students('10440989', 'Mrunal, S', 'SFEN')))
        self.assertEqual(type(Columbia.student['10445678']), type(Students('10445678', 'Aniruddha, P', 'CS')))
        self.assertEqual(type(Columbia.student['10456789']), type(Students('10456789','Akash, D', 'MIS')))

    def test_university_add_instructor(self):
        """ Verify if add_instructor method in University class works properly """

        Columbia = University(r'C:\Users\mruna\Desktop\StevensRepo', pt=False)
        Columbia.add_instructor('10440989', 'Mrunal, S', 'SFEN')
        Columbia.add_instructor('10445678', 'Aniruddha, P', 'CS')
        Columbia.add_instructor('10456789', 'Akash, D', 'MIS')

        self.assertEqual(type(Columbia.instructor['10440989']), type(Instructors('10440989','Mrunal, S', 'SFEN')))
        self.assertEqual(type(Columbia.instructor['10445678']), type(Instructors('10445678','Aniruddha, P', 'CS')))
        self.assertEqual(type(Columbia.instructor['10456789']), type(Instructors('10456789', 'Akash, D', 'MIS')))

    def test_student_init(self):
        """ Verify if __init__ method in Student class works properly """

        student1 = Students('10440989', 'Mrunal, S', 'SFEN')

        self.assertEqual(student1.name, 'Mrunal, S')
        self.assertEqual(student1.major, 'SFEN')
        self.assertEqual(student1.cwid, '10440989')
        self.assertEqual(type(student1.courses), type(defaultdict()))
        self.assertEqual(type(student1.remaining_required), type(list()))
        self.assertEqual(type(student1.remaining_electives), type(list()))
        
        student2 = Students('10345678', 'Anirudha, P', 'CS')
        self.assertEqual(student2.name, 'Anirudha, P')
        self.assertEqual(student2.major, 'CS')
        self.assertEqual(student2.cwid, '10345678')
        self.assertEqual(type(student2.courses), type(defaultdict()))
        self.assertEqual(type(student2.remaining_required), type(list()))
        self.assertEqual(type(student2.remaining_electives), type(list()))

    def test_student_add_course(self):
        """ Verify if add_course method in Student class works properly """

        student1 = Students('10440989', 'Mrunal, S', 'SFEN')
        student1.add_course('SSW 810','A')
        student1.add_course('SSW 540','C')
        student1.add_course('SSW 564','F')

        self.assertEqual(len(student1.courses), 2)

        student2 = Students('10456789', 'Soham, S', 'SYEN')
        student2.add_course('SSW 540','C')
        student2.add_course('SYS 650','F')
        student2.add_course('SSW 564','')

        self.assertEqual(len(student2.courses), 1)

    def test_student_update_course(self):
        """ Verify if update_course method works properly """

        Stevens = University(r'C:\Users\mruna\Desktop\StevensRepo', pt=False)
        student = Students('10440989', 'Mrunal, S', 'SFEN')
        student.add_course('SSW 689','A')
        student.update_course(Stevens.majors)

        expected_required = ['SSW 540', 'SSW 564', 'SSW 555', 'SSW 567']
        expected_electives = ['CS 501', 'CS 513', 'CS 545']

        self.assertEqual(student.remaining_required, expected_required)
        self.assertEqual(student.remaining_electives, expected_electives)

    def test_student_pt_row(self):
        """ Verify if pt_row method works properly """

        Stevens = University(r'C:\Users\mruna\Desktop\StevensRepo', pt=False)
        student = Students('10440989', 'Mrunal, S', 'SFEN')
        student.add_course('SSW 689','A')
        student.update_course(Stevens.majors)

        self.assertEqual([student.cwid, student.name, student.major, sorted(list(student.courses)), student.remaining_required, student.remaining_electives], student.pt_row())

    def test_instructor_init(self):
        """ Verify if __init__ method in Instructor class works properly """

        instructor = Instructors('97654', 'Mrunal, S', 'SFEN')
        self.assertEqual(instructor.name, 'Mrunal, S')
        self.assertEqual(instructor.department, 'SFEN')
        self.assertEqual(type(instructor.prof_course), type(defaultdict()))

    def test_instructor_course_taught(self):
        """ Verify if add_course method in Instructor class works properly """

        instructor = Instructors('98765', 'Mrunal, S', 'SFEN')
        instructor.course_taught('SSW 810')
        instructor.course_taught('SSW 810')
        instructor.course_taught('SSW 564')
        self.assertEqual(instructor.prof_course['SSW 810'], 2)
        self.assertEqual(instructor.prof_course['SSW 564'], 1)
        self.assertNotEqual(instructor.prof_course['SSW 564'], 0)


if __name__ == '__main__':
    unittest.main(exit=False, verbosity=2)
