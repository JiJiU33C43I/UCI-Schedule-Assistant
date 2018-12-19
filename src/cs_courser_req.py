# -------------------- IMPORTS START HERE --------------------
from bs4 import BeautifulSoup
import urllib.request
# -------------------- IMPORTS END HERE --------------------


# -------------------- GLOBAL CONSTANTS START HERE --------------------




# user_input_url is a string object and is defined as below:
# user_input_url = "search_name=search_value" + "&" + "search_name=search_value" + "&" + and so on


## For example, say,
## I would like to get the page source of schedule of CS courses in 2019 Winter Quarter:

user_input_url = "YearTerm=2019-03&Dept=COMPSCI";
HTTP_response = urllib.request.urlopen("https://www.reg.uci.edu/perl/WebSoc/" + "?" + user_input_url);
page_source = HTTP_response.read();

# user_input_url presented here will be referred to as the name "user input data" for convenience of communication

easily_readable_page_source = (BeautifulSoup(page_source, "html.parser")).prettify();
# -------------------- GLOBAL CONSTANTS END HERE --------------------



# -------------------- Source Code --------------------

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
