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

##### course.py #####
# This is a python module that defines the Course class

#=======================================
#==            IMPORTS LIB            ==
#=======================================



#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================




#=======================================
#==            Source Code            ==
#=======================================
class InvalidCourseException(Exception):
    pass;

class InvalidOperandforCourse(Exception):
    pass;

class Course:
    def __init__(self, quarter, coursename, formalname = None):
        self.set_coursename(coursename);
        self.set_formalname(formalname);
        self.set_quarter(quarter);
        self._derived_classes = list();

    def __str__(self):
        name = self.name()
        return f"{self.quarter()} {name[0]}: {name[1]}";

    def __iter__(self):
        for classes in self._derived_classes:
            yield classes;

    def __getitem__(self, item:int):
        if type(item) != int:
            raise KeyError("'Course' object can only accept integer indexing")
        else:
            index = 0;
            for classes in self:
                if index == item:
                    return classes;
                else:
                    index+= 1;
            return None;


    def __len__(self):
        return len(self._derived_classes);

    def __eq__(self, right):
        if type(right) != Course:
            raise InvalidOperandforCourse("== operators only works when both sides are of type 'Course'")
        else:
            if self.name() == right.name() and len(self) == len(right):
                index = 0;
                for i in range(len(self)):
                    if self[i] != right[i]:
                        return False
                    i += 1;
                return True;

            else:
                return False

    def __ne__(self, right):
        return not self.__eq__(right)

    def add(self, value):
        if not isinstance(value, Course):
            raise InvalidCourseException(f"{type(self)}.add(self, {value}): \
ONLY Course instance object can be added to the derived class list; \
argument = {value}");
        self._derived_classes.append(value);

    def set_coursename(self, coursename:str):
        self._coursename = (''.join(coursename.split()));

    def set_formalname(self, formalname:str):
        self._formalname = formalname;

    def name(self):
        return (self._coursename, self._formalname);

    def set_quarter(self, quarter:str):
        self._quarter = quarter;

    def quarter(self):
        return self._quarter;





