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


