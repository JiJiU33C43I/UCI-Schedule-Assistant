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

##### lecture.py #####
# This is a python module that defines the lecture class

#=======================================
#==            IMPORTS LIB            ==
#=======================================
from course import Course
import datetime




#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
Monday = 'M';
Tuesday = 'TU';
Wednesday = 'W';
Thursday = 'TH';
Friday = 'F';
Saturday = 'SAT';
Sunday = 'SUN';
Week = {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday};
Rstr_set = set();          ####### Incomplete Definition Check back later
Status_set = set();        ####### Incomplete Definition Check back later




#=======================================
#==            Source Code            ==
#=======================================


class InvalidClassAttribute(Exception):
    pass;


class Lecture(Course):
    _type = 'Lec';

    def __init__(self, course_obj: Course, Code, Sec, Units, Instructor, time, day, Place, Max, Enr, WL, Req, Rstr, Status):
        Course.__init__(self, *(course_obj.name()));
        self.set_coursecode(Code);
        self.set_section(Sec);
        self.set_units(Units);
        self.set_instructor(Instructor);
        self.set_time(time);
        self.set_day(day);
        self.set_place(Place);
        self.set_max(Max);
        self.set_enr(Enr);
        self.set_wl(WL);
        self.set_req(Req);
        self.set_rstr(Rstr);
        self.set_status(Status);

    def __str__(self):
        start,end = self.time();
        time_info = f"{start.hour}:{start.minute} - {end.hour}:{end.minute}";
        return Course.__str__(self) + f"\nClass Type:{self.type}\n{self.instructor()}\n{self.day()}:{time_info}\n\n"

    def instructor(self):
        return self._instructor;

    def set_instructor(self, instructor:str):
        self._instructor = instructor;

    def coursecode(self):
        return self._coursecode;

    def set_coursecode(self, coursecode:str):
        self._coursecode = coursecode;

    def units(self):
        return self._units;

    def set_units(self, units:int):
        if type(unit) is not int:
            raise InvalidClassAttribute(f"{type(self)}.set_units(self,{units}): \
            units must be type integer;");
        self._units = units;

    def section(self):
        return self._section;

    def set_section(self, section:str):
        self._section = section;

    def time(self):
        return self._time;

    def set_time(self, start: (int,), end:(int,)):
        def _check_valid_time(t:(int,)):
            if type(t) is not tuple:
                raise InvalidClassAttribute(f"{type(self)}.set_time(self,{start}, {end}): \
                arguments must be type tuple;");
            if len(t) != 2:
                raise InvalidClassAttribute(f"{type(self)}.set_time(self,{start}, {end}): \
                length of arguments must be exactly 2;");
            hrs,min = t;
            if type(hrs) is not int or type(min) is not int:
                raise InvalidClassAttribute(f"{type(self)}.set_time(self,{start}, {end}): \
                elements in the tuple must all be type int;");

        _check_valid_time(start);
        _check_valid_time(end);
        start_hour, start_min = start;
        end_hour, end_min = end;
        self._time = (datetime.time(start_hour, start_min), datetime.time(end_hour, end_min));

    def day(self):
        return self._day;

    def set_day(self, day:str):
        day = (''.join(day.split())).upper();

        def _check_valid_day(day:str):
            if day == []:
                return True;
            if day[0] in Week:
                return _check_valid_day(day[1:]);
            elif day[0:2] in Week:
                return _check_valid_day(day[2:]);
            elif day[0:3] in Week:
                return _check_valid_day(day[3:]);
            else:
                return False;

        def _separate_day(day):
            result = set();
            if day[0] in Week:
                result.union({day[0].upper()}, _separate_day(day[1:]));
            elif day[0:2] in Week:
                result.union({day[0:2].upper()}, _separate_day(day[2:]));
            elif day[0:3] in Week:
                result.union({day[0:3].upper()}, _separate_day(day[3:]));
            return result;

        def _sort_week(day:str):
            if day == Monday:
                return 1;
            elif day == Tuesday:
                return 2;
            elif day == Wednesday:
                return 3;
            elif day == Thursday:
                return 4;
            elif day == Friday:
                return 5;
            elif day == Sarturday:
                return 6;
            elif day == Sunday:
                return 7;

        if not _check_valid_day(day):
            raise InvalidClassAttribute(f"{type(self)}.set_day(self, {day}): \
            Invalid Day Argument;");
        self._day = ''.join(sorted(_separate_day(day), key=sort_week))

    def place(self):
        return self._place;

    def set_place(self, place:str):
        self._place = place;

    def max(self):
        return self._max;

    def set_max(self, max:int):
        if type(max) is not int:
            raise InvalidClassAttribute(f"{type(self)}.set_max(self, {max}): \
            max must be type integer;");
        self._max= max;

    def enr(self):
        return self._enr;

    def set_enr(self, enr:int):
        if type(enr) is not int:
            raise InvalidClassAttribute(f"{type(self)}.set_enr(self,{enr}): \
            enr must be type integer;");
        self._enr= enr;

    def wl(self):
        return self._wl;

    def set_wl(self, wl:int):
        if type(wl) is not int:
            raise InvalidClassAttribute(f"{type(self)}.set_wl(self, {wl}): \
            wl must be type integer;");
        self._wl= wl;

    def req(self):
        return self._req;

    def set_req(self, req:int):
        if type(req) is not int:
            raise InvalidClassAttribute(f"{type(self)}.set_req(self,{req}): \
            req must be type integer;");
        self._req= req;

    def rstr(self):
        return self._rstr;

    def set_rstr(self, rstr:str):
        if rstr not in Rstr_set:
            raise InvalidClassAttribute(f"{type(self)}.set_rstr(self, {rstr}): \
            unable to set restriction because restriction given is invalid;");
        self._rstr= rstr;

    def status(self):
        return self._status;

    def set_status(self, status:str):
        if status not in Status_set:
            raise InvalidClassAttribute(f"{type(self)}.set_status(self, {status}): \
            unable to set status because status given is Invalid")
        self._status= status;



