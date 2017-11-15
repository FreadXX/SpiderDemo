import re

import urllib2
import time
from bs4 import BeautifulSoup
from urllib import urlencode
from urllib import quote
import urlparse


if __name__ == '__main__':
    url = 'http://trains.ctrip.com/TrainSchedule/dongche/'
    web_stream = urllib2.urlopen(url)
    html_doc = web_stream.read()

    url_comp = urlparse.urlparse("http://trains.ctrip.com/TrainBooking/TrainSchedule/Station2Station.aspx?from=hangzhou&to=chengdu&fromCn=%BA%BC%D6%DD&toCn=%B3%C9%B6%BC")

    #analysis bs4
    soup = BeautifulSoup(html_doc, 'lxml')
    # print(soup)
    # print(soup.prettify())

    a_node = soup.find_all('a')
    loc_list = []
    for node in a_node:
        if 'TrainSchedule' in node.attrs['href'] and len(node.attrs) > 1 and len(node.contents) > 0:
            print(node.attrs['href'])
            print(node.contents[0].strip())
            result = re.search(r'TrainSchedule/(\w*)/$', node.attrs['href'])
            if result is not None:
                loc_list.append(result.group(0).split('/')[1])
            # train_schedule = urllib2.urlopen(node.attrs['href'])
            
            # train_doc = train_schedule.read()
            # train_soup = BeautifulSoup(train_doc, 'lxml')
            # print(train_soup.prettify())
    
    print loc_list

    for loc_start in loc_list:
        for loc_end in loc_list:
            if loc_start != loc_end:
                url_query = 'http://trains.ctrip.com/TrainBooking/TrainSchedule/Station2Station.aspx?from=%s&to=%s&fromCn=%s&toCn=%s'%(loc_start, loc_end, ,)
                print(url_query)
                detail = urllib2.urlopen(url_query).read()
                detail_soup = BeautifulSoup(detail, 'lxml')
                # print(detail_soup.prettify())
                time.sleep(5)
