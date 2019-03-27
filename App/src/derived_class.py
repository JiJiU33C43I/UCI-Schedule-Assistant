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

##### derived_class.py #####
# This is a python module that defines the derived_class

#=======================================
#==            IMPORTS LIB            ==
#=======================================
from course import Course

#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
RSTR_SET = {'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','S','R','X', ''};
STATUS_SET = {'OPEN', 'NEWONLY', 'WAITL','FULL'};

#=======================================
#==            Source Code            ==
#=======================================


class InvalidClassAttribute(Exception):
    pass;


class DerivedClass(Course):

    def __init__(self, course_obj: Course, Code = None, Type = None, Sec = None, Units = None, Instructor = None, Time = None,
                 Place = None, Final = None, Max = None, Enr = None, WL = None, Req = None, Rstr = None,
                 Textbooks = None, Web = None, Status = None):
        Course.__init__(self, *(course_obj.name()));
        self.set_coursecode(Code);
        self.set_type(Type);
        self.set_section(Sec);
        self.set_units(Units);
        self.set_instructor(Instructor);
        self.set_time(Time);
        self.set_place(Place);
        self.set_final(Final);
        self.set_max(Max);
        self.set_enr(Enr);
        self.set_wl(WL);
        self.set_req(Req);
        self.set_rstr(Rstr);
        self.set_textbooks(Textbooks);
        self.set_web(Web);
        self.set_status(Status);

        self._sub_classes = [];

    def __iter__(self):
        for classes in self._sub_classes:
            yield classes;

    def __len__(self):
        return len(self._sub_classes);

    def add(self, value):
        if not isinstance(value, DerivedClass):
            raise InvalidCourseException(f"{type(self)}.add(self, {value}): \
ONLY DerivedClass instance object can be added to the derived class set; \
argument = {value}");
        self._sub_classes.append(value);

    def __str__(self):
        return f"{self.coursecode()} {self.type()}";

    def set_coursecode(self, coursecode:str):
        self._coursecode = coursecode;

    def coursecode(self) -> str:
        return self._coursecode;

    def set_type(self, type:str):
        self._type = type.upper();

    def type(self) -> str:
        return self._type;

    def set_section(self, section:str):
        self._section = section;

    def section(self) -> str:
        return self._section;

    def set_units(self, units:str):
        try:
            int_units = int(units);
            self._units = int_units;
        except:
            self._units = None;

    def units(self) -> int:
        return self._units;

    def set_instructor(self, instructor:str):
        #self._instructor = [lecturer.upper() for lecturer in instructor.split('\n') if lecturer.upper() not in ('STAFF', 'TBA', 'TBD')];
        self._instructor = instructor.replace(' ', '').split('\n');

    def instructor(self) -> list:
        return self._instructor;

    def set_time(self, time:str):
        try:
            self._day, self._hour = time.replace(' ', '').split('\n');
        except Exception:
            self._day = None;
            self._hour = None;

    def time(self) -> tuple:
        return (self._day, self._hour);

    def set_place(self, place:str):
        self._place = place;

    def place(self) -> str:
        return self._place;

    def set_final(self, final:str):
        self._final = final;

    def final(self) -> str:
        return self._final;

    def set_max(self, max:str):
        try:
            int_max = int(max);
            self._max = int_max;
        except Exception:
            self._max = None;

    def max(self) -> int:
        return self._max;

    def set_enr(self, enr:str):
        try:
            int_enr = int(enr);
            self._enr = int_enr;
        except Exception:
            self._enr = None;

    def enr(self) -> int:
        return self._enr;

    def set_wl(self, wl:str):
        try:
            int_wl = int(wl);
            self._wl = int_wl;
        except Exception:
            self._wl = None;

    def wl(self) -> int:
        return self._wl;

    def set_req(self, req:str):
        try:
            int_req = int(req);
            self._req = int_req;
        except Exception:
            self._req = None;

    def req(self) -> int:
        return self._req;

    def set_rstr(self, rstr:str):
        if rstr != None:
            list_rstr = rstr.replace(' ', '').replace('and','\n').upper().split('\n')
            if any([(r not in RSTR_SET) for r in list_rstr]):
                raise InvalidClassAttribute(f"{type(self)}.set_rstr(self, {rstr}): unable to set restriction because restriction given is invalid;");
            self._rstr= list_rstr;
        else:
            self._rstr = None;

    def rstr(self) -> list:
        return self._rstr;

    def set_textbooks(self, textbooks:str):
        self._textbooks = textbooks;

    def textbooks(self) -> str:
        return self._textbooks;

    def set_web(self, web:str):
        self._web = web;

    def web(self) -> str:
        return self._web;

    def set_status(self, status:str):
        if status != None:
            if status.upper() not in STATUS_SET:
                raise InvalidClassAttribute(f"{type(self)}.set_status(self, {status}): unable to set status because status given is Invalid")
            self._status= status.upper();
        else:
            self._status = None;

    def status(self) -> str:
        return self._status;





