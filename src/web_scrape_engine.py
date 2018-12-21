##### web_scrape_engine.py #####
# This is a python module that takes in a given and presumably correct user_input string and extract course information out of that

#=======================================
#==            IMPORTS LIB            ==
#=======================================
import bs4
from bs4 import BeautifulSoup
from collections import defaultdict
import urllib.request
import urllib.parse



#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
base_schedule_of_classes_url = "https://www.reg.uci.edu/perl/WebSoc";
BeautifulSoup_Parser = "html.parser"
course_info_header = ["Code", "Type", "Sec", "Units", "Instructor", "Time", "Place", "Final","Max", "Enr", "WL", "Req", "Rstr", "Textbooks", "Web", "Status"];
debugging = True;


#=======================================
#==            Source Code            ==
#=======================================

class ParseUrlError(Exception):
    pass;

class RequestFailedError(Exception):
    pass;

class FindNewCourseError(Exception):
    pass;

class InvalidTrRow(Exception):
    pass;

class web_scrape_engine:
    base_url = base_schedule_of_classes_url;
    parser = BeautifulSoup_Parser;
    ch = course_info_header;

    def __init__(self, user_input_dict: dict):
        self._user_input_dict = user_input_dict;
        self._user_input_dict["ShowFinals"] = "on";
        self.parse_url();
        self.soup = self.request_page();
        self.extract_data();

    def __str__(self):
        return self.soup.prettify();

    def parse_url(self):
        try:
            parsed_url = urllib.parse.urlencode(self._user_input_dict);
        except:
            raise ParseUrlError(f"{type(self).parse_url()}: Unable to parse url; \nuser_input_dict = {self._user_input_dict}");
        self.parsed_url = self.base_url + "?" + parsed_url;

    def request_page(self):
        try:
            print(f"Sending Request to '{self.base_url + self.parsed_url}'...")
            HTTP_response = urllib.request.urlopen(self.parsed_url);
            print("HTTP Response Received!\nStart to Decode Response...\nIt might take a few minutes, please wait...");
            html_page_source = HTTP_response.read();
            print("Succesfully Read and Decode Response!")
        except:
            raise RequestFailedError("Something is wrong with the request. Please RE-CREATE a NEW Web Scrape Engine Object!");
        return BeautifulSoup(html_page_source, self.parser);

    def extract_data(self):

        def _find_first_course(soup):
            try:
                course_title= soup.find("td", {"class": "CourseTitle"});
                if course_title == None:
                    return None;
                else:
                    return course_title;
            except:
                raise FindNewCourseError();

        def _generate_new_course(course_title_row):
            title_string_lst = [i for i in course_title_row.strings];
            coursename = ' '.join((title_string_lst[0].replace('\xa0', ' ').split()));
            formalname = ' '.join((title_string_lst[1].replace('\xa0', ' ').split()));
            return {"coursename": coursename, "formalname": formalname,
                                          "_derived_classes": list()};

        def _find_new_classes(tr_row):

            def _is_a_valid_class(td_tags_lst):
                '''This is a function that tries to PREDICT/GUESS whether a <tr> row is actually containing the course info.
                    This prediction/guess might go wrong and may need to be adjusted in the future
                     because it is highly dependent on pattern/order of the html page source'''
                try:
                    check_list = [(len(td_tags_lst) == 16), \
                                  (len(td_tags_lst[0].string) == 5), (type(int(td_tags_lst[0].string)) is int), \
                                  ((td_tags_lst[1].string.upper()) in ['ACT','COL','DIS','FLD','LAB','LEC','QIZ','RES','SEM','STU','TAP','TUT'])];
                    #print("Following: ",check_list)
                    if all(check_list):
                        return True;
                    else:
                        return False;
                except:
                    return False;

            def _generate_new_class(td_tags_list:list):
                course_info = [i.string for i in td_tags_list];
                return zip(self.ch, course_info);

            all_classes_searched = False;
            class_lst = [];
            next_tr_row = tr_row.find_next_sibling();
            while not all_classes_searched:
                try:
                    if next_tr_row == None:
                        return (class_lst, next_tr_row);
                    elif type(next_tr_row) == bs4.NavigableString or type(next_tr_row) == bs4.Comment:
                        raise InvalidTrRow()
                    elif (next_tr_row.find("td") != None) and (next_tr_row.find("td")["class"][0] == "CourseTitle"):
                        all_classes_searched = True;
                        return (class_lst, next_tr_row);
                except InvalidTrRow:
                    next_tr_row = next_tr_row.find_next_sibling();
                    continue;
                except KeyError:
                    pass;
                ## Below is the Algorithm for determining whether a tr row contains COURSE INFO and extract correct data ##
                #print("Before: ", next_tr_row)
                td_tags_lst = next_tr_row.find_all("td");
                #print("Here: ", td_tags_lst)
                if _is_a_valid_class(td_tags_lst):
                    class_lst.append(dict(_generate_new_class(td_tags_lst)));
                    #print(class_lst, '\n\n\n')
                next_tr_row = next_tr_row.find_next_sibling();

        print("Start to Extract Data... This might take a while...")
        courses_found = 0;
        course_data = [];
        soup = self.soup;
        course_title = _find_first_course(soup)
        course_title_row = course_title.parent;
        #print(course_title)
        while course_title_row != None:
            course_data.append(_generate_new_course(course_title_row));
            class_lst,course_title_row = _find_new_classes(course_title_row);
            course_data[courses_found]["_derived_classes"].extend(class_lst);
            courses_found += 1;
        self.course_data = course_data;

    def get_data(self):
        return self.course_data;




#=======================================
#==       DEBUGGING AND TESTING       ==
#=======================================
if __name__ == '__main__' and debugging:

    user_input_dict = {"YearTerm":"2019-03", "Dept":"COMPSCI"}
    # You Might change/alter/add to the ^user_input_dict^ for the purpose of further testing


    engine = web_scrape_engine(user_input_dict);
    course_data = engine.get_data();
    print("\n\n")
    for courses in course_data:
        for v in courses.values():
            print(v)
            if type(v) is list:
                for i in v:
                    print(f"{i['Code']} {i['Type']} {i['Sec']}")
        print('\n\n\n')
    print(f'\n\n\n--------------Number of Found Courses: {len(course_data)}--------------\n');
