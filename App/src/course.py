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


class Course:
    def __init__(self, coursename, formalname = None):
        self.set_coursename(coursename);
        self.set_formalname(formalname);
        self._derived_classes = list();

    def __str__(self):
        name = self.name()
        return f"{name[0]}: {name[1]}";

    def __iter__(self):
        for classes in self._derived_classes:
            yield classes;

    def __len__(self):
        return len(self._derived_classes);

    def add(self, value):
        if not isinstance(value, Course):
            raise InvalidCourseException(f"{type(self)}.add(self, {value}): \
ONLY Course instance object can be added to the derived class list; \
argument = {value}");
        self._derived_classes.append(value);

    def name(self):
        return (self._coursename, self._formalname);

    def set_coursename(self, coursename:str):
        self._coursename = (''.join(coursename.split()));

    def set_formalname(self, formalname:str):
        self._formalname = formalname;


