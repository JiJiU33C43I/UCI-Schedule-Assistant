from bs4 import BeautifulSoup
import requests

#only for cs class
res = requests.get('http://catalogue.uci.edu/donaldbrenschoolofinformationandcomputersciences/departmentofcomputerscience/#majorstext')
soup = BeautifulSoup(res.text, 'lxml')


def get_course_title(soup):
    course_info = soup.find_all('tr', {'class': 'even'})
    result = []
    for course in course_info:
        if course.a != None:
            result.append(course.a.text)

    return result



#print list of cs classes
#for i in get_course_title(soup):
#    print(i)


'''
can't figure out how to get course description
实在想不出了， 查也查不到， YouTube也没有。。。。期待着你们
'''
bubble = soup.find_all('div', {'class':'courseblock'})
for i in bubble:
   # print(i.prettify())
    print(i.p)





