'''
MIT License

Copyright (c) 2019 JiJiU33C43I Contributors

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''

##### course_data_decoder.py #####
# This is a python module that defines the CourseDecoder class, which is able to take in the course_data dictionary and
# generate corresponding course objects

#=======================================
#==            IMPORTS LIB            ==
#=======================================
from course import Course
from derived_class import DerivedClass


#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================

PRIMARYCLASS_TYPE = ('ACT', 'COL', 'FLD', 'LEC', 'QIZ', 'RES', 'SEM', 'STU', 'TAP', 'TUT');
SECONDARYCLASS_TYPE = ('DIS', 'LAB');

DEBUGGING = False;


#=======================================
#==            Source Code            ==
#=======================================

class DecodeCourseError(Exception):
    pass;


class CourseDecoder:

    def __init__(self, quarter, course_data):
        self.course_obj_list = [];
        self.quarter = quarter;
        self.generate_course_lists(course_data);

    def __len__(self):
        return len(self.course_obj_list);

    def __iter__(self):
        for course in self.course_obj_list:
            yield course;

    @staticmethod
    def secondary_class_exists(derived_class_lst: list):
        ''' The Algorithm of this function might seem WEIRD and UNREASONABLE at the beginning.
        1. If there are "primary classes" detected, then there may be possibility of secondary class exists  -> Function returns True
        2. If all derived classes are "secondary class", then "secondary class" are actually interpreted as primary class for this course,
           then we can deduce that there is NOT ANY secondary class  -> Function returns False
        '''
        for derived_class in derived_class_lst:
            if derived_class["Type"].upper() in PRIMARYCLASS_TYPE:
                return True;
        return False;

    @staticmethod
    def decode_one_course(quarter, course:dict) -> Course:
        '''
        course = { 'coursename': 'xxx', 'formalname':'xxx', '_derived_classes': [dict] }
        '''
        current_course = Course(quarter, course['coursename'], course['formalname']);
        current_primary_class = None;

        if CourseDecoder.secondary_class_exists(course['_derived_classes']):
            #print("secondary classes exist")
            for derived_class in course['_derived_classes']:
                if derived_class['Type'].upper() in PRIMARYCLASS_TYPE:
                    try:
                        current_primary_class = DerivedClass(current_course, **derived_class);
                        current_course.add(current_primary_class);
                    except Exception as E:
                        if DEBUGGING: raise E;
                        continue;
                elif derived_class['Type'].upper() in SECONDARYCLASS_TYPE:
                    try:
                        current_secondary_class = DerivedClass(current_course, **derived_class);
                        current_primary_class.add(current_secondary_class);
                    except Exception as E:
                        if DEBUGGING: raise E;
                        continue;
                else:
                    raise DecodeCourseError('Unrecognized Class Type : class with type {} in course {}??'.format(derived_class['Type'], current_course.name()));

        else:
            for derived_class in course['_derived_classes']:
                current_course.add(DerivedClass(current_course, **derived_class));

        return current_course;


    def generate_course_lists(self, course_data):
        if course_data != None:
            for course in course_data:
                current_course = CourseDecoder.decode_one_course(self.quarter, course);
                self.course_obj_list.append(current_course);

    def get_course_lists(self):
        return self.course_obj_list;


#=======================================
#==       DEBUGGING AND TESTING       ==
#=======================================
import web_scrape_engine

if __name__ == '__main__':

    user_input_dict = {"YearTerm":"2019-14", "Dept":"CHEM"}
    # You Might change/alter/add to the ^user_input_dict^ for the purpose of further testing

    engine = web_scrape_engine.web_scrape_engine(user_input_dict);
    course_data = engine.extract_data();
    CD = CourseDecoder(user_input_dict["YearTerm"], course_data);

    print("\n\n",course_data, "\n\n")

    print(f'---------------------- START DECODING ----------------------')
    for course in CD:
        print(course);
        for primary_class in course:
            print('\tprimary:', primary_class);
            for secondary_class in primary_class:
                print('\t\tsecondary:', secondary_class);

    print(f'-------------------- DECODED {len(CD)} COURSES --------------------');