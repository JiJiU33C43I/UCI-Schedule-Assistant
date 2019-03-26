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

##### dis_lab.py #####
# This is a python module that defines the dis_lab class

#=======================================
#==            IMPORTS LIB            ==
#=======================================
from lecture import Lecture, InvalidClassAttribute



#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================

Type_set = set() ####### Incomplete Definition Check Back Later



#=======================================
#==            Source Code            ==
#=======================================

class Dis_Lab(Lecture):
    def __init__(self, coursename=None, tpe = 'Dis', instructor=None, coursecode=None, section= None, units=4, day=None, place=None, \
                 max=0, enr=0, wl=0, req=0, rstr=None, status='OPEN'):
        Lecture.__init__(coursename, instructor, coursecode, section, units, day, place, max, enr, wl, req, rstr, status);
        self.set_type(tpe);

    def type(self):
        return self._type;

    def set_type(self, tpe:str):
        if tpe not in {'Lab', 'Dis'}:
            raise InvalidClassAttribute(f"{type(self)}.set_type(self, {tpe}): \
            Type of a course class must either be 'Lec', 'Dis', 'Lab';");
        self._type = tpe;
