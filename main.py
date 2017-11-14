import urllib2
import time
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://trains.ctrip.com/TrainSchedule/dongche/'
    web_stream = urllib2.urlopen(url)
    html_doc = web_stream.read()

    #analysis bs4
    soup = BeautifulSoup(html_doc, 'lxml')

    # print(soup)
    # print(soup.prettify())

    a_node = soup.find_all('a')
    for node in a_node:
        if 'TrainSchedule' in node.attrs['href'] and len(node.attrs) > 1 and len(node.contents) > 0:
            print(node.attrs['href'])
            print(node.contents[0].strip())
            time.sleep(5)
            train_schedule = urllib2.urlopen(node.attrs['href'])
            train_doc = train_schedule.read()
            train_soup = BeautifulSoup(train_doc, 'lxml')
            # print(train_soup.prettify())