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
