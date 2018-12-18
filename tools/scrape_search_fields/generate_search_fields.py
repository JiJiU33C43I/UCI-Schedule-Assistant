##### generate_search_fields.py #####
# This is a python module that helps to scrape the search name and search value from the "Schedule of Classes" Page automatically

# -------------------- IMPORTS START HERE --------------------
import urllib.request
from bs4 import BeautifulSoup
# -------------------- IMPORTS START HERE --------------------

# -------------------- GLOBAL CONSTANTS START HERE --------------------
Schedule_of_Classes_url = "https://www.reg.uci.edu/perl/WebSoc/";
search_name_dict = {"Term":"YearTerm",
                    "Display Options 1":"ShowComments",
                    "Display Options 2":"ShowFinals",
                    "General Education (Breadth)":"Breadth",
                    "Department Name":"Dept",
                    "Course Number or Range":"CourseNum",
                    "Course Level":"Division",
                    "Course Code or Range":"CourseCodes",
                    "Instructor":"InstrName",
                    "Course Title Contains":"CourseTitle",
                    "Course Type":"ClassType",
                    "Units":"Units",
                    "Days":"Days",
                    "Starting Time After":"StartTime",
                    "Ending Time Before":"EndTime",
                    "Maximum Capacity":"MaxCap",
                    "Course Full Options":"FullCourses",
                    "Web Font Size Percentages":"FontSize",
                    "Cancelled Courses":"CancelledCourses",
                    "Meeting Place 1":"Bldg",
                    "Meeting Place 2":"Room"};
# -------------------- GLOBAL CONSTANTS END HERE --------------------


# -------------------- Source Code --------------------

class InvalidSelectTag(Exception):
    pass;

HTTP_response = urllib.request.urlopen(Schedule_of_Classes_url);
schedule_search_soup = BeautifulSoup(HTTP_response.read(), "html.parser");

try:
    f = open("search_format.txt", "x");
except FileExistsError:
    f = open("search_format.txt", "w");

for displayed_name, search_name in search_name_dict.items():
    f.write(f"***\n### {displayed_name}\n");
    f.write(f"Search_name | {search_name} \n ---------- | ---------- \n\n");
    select_tag_lst = schedule_search_soup.find_all("select", {"name":search_name});
    f.write("User Selection Option | Search_value \n ---------- | ---------- \n");
    if len(select_tag_lst) == 0:
        f.write(" This Input Tag is not a selection tag | None \n\n")
    elif len(select_tag_lst) == 1:
        for option in select_tag_lst[0].find_all("option"):
            try:
                value = option['value'];
            except KeyError:
                value = option.text;
            f.write(f"{option.text} | {value} \n")
    else:
        raise(InvalidSelectTag("Exception: multiple select tags corresponds to one name"))
    f.write("\n\n<br>\n\n")

f.close()
