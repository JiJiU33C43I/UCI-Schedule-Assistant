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
from course_data_decoder import CourseDecoder
import time;
import threading;
import queue;

#=======================================
#==          GLOBAL CONSTANTS         ==
#=======================================
USER_FILTER_OPTION_EXAMPLE_1 = ("2019-14", "34000");
USER_FILTER_OPTION_EXAMPLE_2 = ("2019-14", "34001");
UPDATE_INTERVAL = 2;  # update the course data every {UPDATE_INTERVAL} seconds

#=======================================
#==            Source Code            ==
#=======================================

class tracking_targets_change_error(Exception):
    pass;

class update_course_data:
    update_interval = UPDATE_INTERVAL;

    def __init__(self, filter_dict: [tuple], wait_time = update_interval, FIFO_queue = queue.Queue()):
        self.filter_dict = filter_dict;
        self.course_data = [];
        self.synced_queued = FIFO_queue;
        self.wait_time = wait_time;
        self._update_data();
        self.running = False;

    def _update_data(self):
        self.new_course_data = [];
        for filter in self.filter_dict:
            quarter, coursecode = filter;
            user_input_dict = {"YearTerm": quarter, "CourseCodes": coursecode}
            course_data = ENGINE.web_scrape_engine(user_input_dict).extract_data();
            for course in CourseDecoder(quarter, course_data):
                self.new_course_data.append(course);

    def _compare_data(self):
        if (len(self.course_data) != len(self.new_course_data)) and self.course_data != []:
            raise tracking_targets_change_error(f"length of two course lists is inconsistent: self.course_data(:={len(self.course_data)}) while self.new_course_data(:={len(self.new_course_data)})")
        changed_status = False;
        changed_course_lst = [];
        for i in range(len(self.course_data)):
            if self.course_data[i] != self.new_course_data[i]:
                print("\n")
                print("The old data is: ", self.course_data[i], [str(derived_class) for derived_class in self.course_data[i]]);
                print("The new data is: ", self.new_course_data[i], [str(derived_class) for derived_class in self.new_course_data[i]]);
                print("\n")
                changed_course_lst.append(self.new_course_data[i]);
                changed_status = True;
        self.course_data = self.new_course_data;
        self.synced_queued.put((changed_status, changed_course_lst));

    def __str__(self):
        return '\n'.join([str(course) for course in self.course_data]);

    def start(self):
        self.running = True;
        self.run();

    def terminate(self):
        self.running = False;

    def run(self):
        while self.running:
            #print('running...')
            self._update_data();
            self._compare_data();
            #print(self);
            time.sleep(self.wait_time);




def get_queue_status(q, update_engine):
    while update_engine.running:
        print("getting...")
        while not q.empty():
            print("one object is got from queue:", q.get());
            q.task_done();
        time.sleep(UPDATE_INTERVAL);


if __name__ == "__main__":
    common_q = queue.Queue();
    update_engine = update_course_data([USER_FILTER_OPTION_EXAMPLE_1, USER_FILTER_OPTION_EXAMPLE_2], FIFO_queue=common_q);
    a = threading.Thread(target = update_engine.start);
    b = threading.Thread(target = get_queue_status, args = (common_q,update_engine));
    a.start();
    b.start();


