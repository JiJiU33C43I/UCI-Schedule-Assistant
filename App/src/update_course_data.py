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

##### update_course_data.py #####
# This is a python module that keeps updating course information by requesting the data from the server periodically

#=======================================
#==          IMPORTS MODULE           ==
#=======================================
import web_scrape_engine as ENGINE;
import time;

#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
USER_FILTER_OPTION_EXAMPLE = {"YearTerm":"2019-14", "Dept":"EECS"};
UPDATE_INTERVAL = 2;  # update the course data every {UPDATE_INTERVAL} seconds

#=======================================
#==            Source Code            ==
#=======================================

class update_course_data:
    update_interval = UPDATE_INTERVAL;

    def __init__(self, filter_dict: [dict], wait_time = update_interval):
        self.filter_dict = filter_dict;
        self.course_data = [];
        self.wait_time = wait_time;
        self._update_data();
        self.running = False;

    def _update_data(self):
        self.course_data = [];
        for filter in self.filter_dict:
            self.course_data.append(ENGINE.web_scrape_engine(filter).extract_data());

    def __str__(self):
        return '\n'.join([str(course) for course in self.course_data]);

    def start(self):
        self.running = True;
        self.run();

    def terminate(self):
        self.running = False;

    def run(self):
        while self.running:
            self._update_data();
            print(self);
            time.sleep(self.wait_time);



if __name__ == "__main__":
    update_engine = update_course_data([USER_FILTER_OPTION_EXAMPLE]);
    update_engine.start();


