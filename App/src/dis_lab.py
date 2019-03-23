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
