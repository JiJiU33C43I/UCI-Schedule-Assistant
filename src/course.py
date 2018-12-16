##### course.py #####
# This is a python module that defines the Course class

# -------------------- IMPORTS START HERE --------------------
# -------------------- IMPORTS START HERE --------------------

# -------------------- GLOBAL CONSTANTS START HERE --------------------
# -------------------- GLOBAL CONSTANTS END HERE --------------------


# -------------------- Source Code --------------------
class Course:
    def __init__(self, coursename, formalname = None):
        self.set_coursename(coursename);
        self.set_formalname(formalname);
        self._derived_classes = set()

    def __str__(self):
        name = self.name()
        return f"{name[0]}: {name[1]}";

    def __iter__(self):
        for classes in self._derived_classes:
            yield classes;

    def add(self, value):
        self._derived_classes.add(value);

    def name(self):
        return (self._coursename, self._formalname);

    def set_coursename(self, coursename:str):
        self._coursename = (''.join(coursename.split())).upper();

    def set_formalname(self, formalname:str):
        self._formalname = formalname;

