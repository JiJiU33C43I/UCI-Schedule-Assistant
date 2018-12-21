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

    def add(self, value):
        if not isinstance(value, Course):
            raise InvalidCourseException(f"{type(self)}.add(self, {value}): \
            ONLY Course instance object can be added to the derived class set; \
            argument = {value}");
        self._derived_classes.add(value);

    def name(self):
        return (self._coursename, self._formalname);

    def set_coursename(self, coursename:str):
        self._coursename = (''.join(coursename.split())).upper();

    def set_formalname(self, formalname:str):
        self._formalname = formalname;


