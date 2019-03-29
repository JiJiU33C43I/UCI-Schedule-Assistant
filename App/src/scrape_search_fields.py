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


##### scrape_search_fields.py #####
# This is a python module that helps to scrape the search name and search value from the "Schedule of Classes" Page automatically

#=======================================
#==          IMPORTS MODULE           ==
#=======================================
import urllib.request
from bs4 import BeautifulSoup
from collections import defaultdict
import ssl


#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
SCHEDULE_OF_CLASSES_URL = "https://www.reg.uci.edu/perl/WebSoc/";
SEARCH_FIELDS = ("YearTerm","Dept");


#=======================================
#==            Source Code            ==
#=======================================

class InvalidSelectTag(Exception):
    pass;

class scrape_fields:
    default_url = SCHEDULE_OF_CLASSES_URL;
    default_search_fields = SEARCH_FIELDS;

    def __init__(self, url = default_url, search_fields = default_search_fields):
        self._url = url;
        self._search_fields = search_fields;
        self._field_option_dict = defaultdict(dict);
        self._ssl_context = ssl.SSLContext();

    def start_to_scrape(self):
        HTTP_response = urllib.request.urlopen(self._url, context = self._ssl_context);
        schedule_search_soup = BeautifulSoup(HTTP_response.read(), "html.parser");
        for search_field in self._search_fields:
            select_tag_lst = schedule_search_soup.find_all("select", {"name":search_field});
            if ( len(select_tag_lst) == 1 ):
                for option in select_tag_lst[0].find_all("option"):
                    self._field_option_dict[search_field][option.text] = option['value'];

    def get_fields_dict(self):
        return self._field_option_dict;

#=======================================
#==       DEBUGGING AND TESTING       ==
#=======================================
if __name__ == "__main__":
    scrape_search_engine = scrape_fields();
    scrape_search_engine.start_to_scrape();
    for k,d in scrape_search_engine.get_fields_dict().items():
        print(k);
        for a,b in d.items():
            print("{}       :        {}".format(a,b))
        print();
