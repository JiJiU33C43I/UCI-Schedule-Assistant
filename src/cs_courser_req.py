##### cs_course_req.py #####
# ??

#=======================================
#==            IMPORTS LIB            ==
#=======================================
from bs4 import BeautifulSoup
import urllib.request



#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================

user_input_url = "YearTerm=2019-03&Dept=COMPSCI";
HTTP_response = urllib.request.urlopen("https://www.reg.uci.edu/perl/WebSoc/" + "?" + user_input_url);
page_source = HTTP_response.read();
easily_readable_page_source = (BeautifulSoup(page_source, "html.parser")).prettify();


#=======================================
#==            Source Code            ==
#=======================================

source = BeautifulSoup(page_source, "html.parser")
course_title = source.find_all('td', {'class':'CourseTitle'})

#print all class title
#for i in course_title:
#    print(i.text)

remaining_info = source.find_all('td')
#print(temp)


#print all other information
for i in remaining_info:
    print(i.text, type(i.text), len(i.text))
