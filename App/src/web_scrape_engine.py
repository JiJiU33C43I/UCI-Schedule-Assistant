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
import ssl



#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
base_schedule_of_classes_url = "https://www.reg.uci.edu/perl/WebSoc";
BeautifulSoup_Parser = "html.parser"    # LXML Parser requires the third party library <lxml> to be installed
course_info_header = ["Code", "Type", "Sec", "Units", "Instructor", "Time", "Place", "Final","Max", "Enr", "WL", "Req", "Rstr", "Textbooks", "Web", "Status"];
DEBUGGING = False;


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

class ClassHasInconsistentNumberofHeaders(Exception):
    pass;

class web_scrape_engine:
    base_url = base_schedule_of_classes_url;
    parser = BeautifulSoup_Parser;
    ch = course_info_header;

    def __init__(self, user_input_dict: dict):
        self._user_input_dict = user_input_dict;
        self._user_input_dict["ShowFinals"] = "on";
        self._ssl_context = ssl.SSLContext();
        self.parse_url();
        self.soup = self.request_page();
        self._replace_special_character();


    def __str__(self):
        return self.soup.prettify();

    def _replace_special_character(self):
        for linebreak in self.soup.find_all('br'):
            linebreak.replaceWith('\n');

    def parse_url(self):
        try:
            parsed_url = urllib.parse.urlencode(self._user_input_dict);
        except:
            raise ParseUrlError(f"{type(self).parse_url()}: Unable to parse url; \nuser_input_dict = {self._user_input_dict}");
        self.parsed_url = self.base_url + "?" + parsed_url;

    def request_page(self):
        try:
            if DEBUGGING: print(f"Sending Request to '{self.base_url + self.parsed_url}'...")
            HTTP_response = urllib.request.urlopen(self.parsed_url, context = self._ssl_context);
            if DEBUGGING: print("HTTP Response Received!\nStart to Decode Response...\nIt might take a few minutes, please wait...");
            html_page_source = HTTP_response.read();
            if DEBUGGING: print("Succesfully Read and Decode Response!")
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

                    check_list = [(len(td_tags_lst[0].string) == 5), (type(int(td_tags_lst[0].string)) is int), \
                                  ((td_tags_lst[1].string.upper()) in ['ACT','COL','DIS','FLD','LAB','LEC','QIZ','RES','SEM','STU','TAP','TUT'])];
                    #print("\nvalid? ->", check_list);
                    if all(check_list):
                        return True;
                    else:
                        return False;
                except:
                    return False;

            def _generate_new_class(td_tags_list:list):
                course_info = [];
                course_info = [i.text.replace('\xa0', '\n') for i in td_tags_list];
                if ( len(td_tags_lst) == 16 ):
                    return zip(self.ch, course_info);
                elif ( len(td_tags_lst) == 15 ):
                    return zip([h for h in self.ch if h != "WL"], course_info);
                elif ( len(td_tags_lst) == 14 ):
                    return zip([h for h in self.ch if h != "WL" and h != "Status"], course_info);
                else:
                    raise ClassHasInconsistentNumberofHeaders(f"get a class that has only {len(td_tags_lst)} number of headers");

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
                #print("\n\n",td_tags_lst);
                #print("Here: ", td_tags_lst)
                if _is_a_valid_class(td_tags_lst):
                    #print("\n valid class")
                    #print(td_tags_lst);
                    class_lst.append(dict(_generate_new_class(td_tags_lst)));
                    #print(class_lst, '\n\n\n')
                next_tr_row = next_tr_row.find_next_sibling();


        try:
            if DEBUGGING: print("Start to Extract Data... This might take a while...")
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
            return course_data;
        except Exception as E:
            if DEBUGGING: raise E;
            return None;






#=======================================
#==       DEBUGGING AND TESTING       ==
#=======================================
if __name__ == '__main__':

    user_input_dict = {"YearTerm":"2019-14", "Dept":"EECS"}
    # You Might change/alter/add to the ^user_input_dict^ for the purpose of further testing

    engine = web_scrape_engine(user_input_dict);

    #print(engine.soup);

    course_data = engine.extract_data();
    print("\n\ncourse_data = ",course_data);
    print("\n\n")
    for courses in course_data:
        for v in courses.values():
            print(v)
            if type(v) is list:
                for i in v:
                    print(f"{i['Code']} {i['Type']} {i['Sec']}")
        print('\n\n\n')
    print(f'\n\n\n--------------Number of Found Courses: {len(course_data)}--------------\n');


