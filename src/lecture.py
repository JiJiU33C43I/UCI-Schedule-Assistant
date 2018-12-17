##### lecture.py #####
# This is a python module that defines the lecture class

# -------------------- IMPORTS START HERE --------------------
from course import Course
import datetime
# -------------------- IMPORTS END HERE --------------------

# -------------------- GLOBAL CONSTANTS START HERE --------------------
Monday = 'M';
Tuesday = 'TU';
Wednesday = 'W';
Thursday = 'TH';
Friday = 'F';
Saturday = 'SAT';
Sunday = 'SUN';
Week = {Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday};
# -------------------- GLOBAL CONSTANTS END HERE --------------------

# -------------------- Source Code --------------------


class InvalidClassAttribute(Exception):
    pass;


class Lecture(Course):
    _type = 'Lec';

    def __init__(self, coursename=None, instructor=None, coursecode=None, section='A', units = 4, day=None, place=None,\
                 max = 0, enr = 0, wl = 0, req = 0, rstr = None, status = 'OPEN'):
        Course.__init__(self, coursename);
        self.set_coursename(coursename);
        self.set_instructor(instructor);
        self.set_coursecode(coursecode);
        self.set_section(section);
        self.set_units(units);
        self.set_day(day);
        self.set_place(place);
        self.set_max(max);
        self.set_enr(enr);
        self.set_wl(wl);
        self.set_req(req);
        self.set_rstr(rstr);
        self.set_status(status);

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
            raise InvalidClassAttribute(f"{type(self)}.set_units: units must be type integer; \
            argument = {unit}");
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
                raise InvalidClassAttribute(f"{type(self)}.set_time: arguments must be type tuple; \
                 argument = {t}");
            if len(t) != 2:
                raise InvalidClassAttribute(f"{type(self)}.set_time: length of arguments must be exactly 2; \
                argument = {t}");
            hrs,min = t;
            if type(hrs) is not int or type(min) is not int:
                raise InvalidClassAttribute(f"{type(self)}.set_time: elements in the tuple must all be type int; \
                argument = {t}");

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
            raise InvalidClassAttribute(f"{type(self)}.set_day: Invalid Day Argument; \
            argument = {day}");
        self._day = ''.join(sorted(_separate_day(day), key=sort_week))

    def place(self):
        return self._place;

    def set_place(self, place:str):
        self._place = place;

    def max(self):
        return self._max;

    def set_max(self, max:int):
        if type(max) is not int:
            raise InvalidClassAttribute(f"{type(self)}.set_max: max must be type integer; \
            argument = {max}");
        self._max= max;

    def enr(self):
        return self._enr;

    def set_enr(self, enr:int):
        if type(enr) is not int:
            raise InvalidClassAttribute(f"{type(self)}.set_enr: enr must be type integer; \
            argument = {enr}");
        self._enr= enr;

    def wl(self):
        return self._wl;

    def set_wl(self, wl:int):
        if type(wl) is not int:
            raise InvalidClassAttribute(f"{type(self)}.set_wl: wl must be type integer; \
            argument = {wl}");
        self._wl= wl;

    def req(self):
        return self._req;

    def set_req(self, req:int):
        if type(req) is not int:
            raise InvalidClassAttribute(f"{type(self)}.set_req: req must be type integer; \
            argument = {req}");
        self._req= req;

    def rstr(self):
        return self._rstr;

    def set_rstr(self, rstr:str):
        #### Missing Exception Check Back Later ####
        self._rstr= rstr;

    def status(self):
        return self._status;

    def set_status(self, status:str):
        #### Missing Exception Check Back Later ####
        self._status= status;



