import threading 
from queue import Queue
from spider import Spider 
from link_finder import LinkFinder
from general import *
from domain import *

# Comments by Arpit Agrawal 19-Jan-2019 for version 1.0

PROJECT_NAME = 'pythonanywhere'
HOMEPAGE = 'https://www.pythonanywhere.com/'
DOMAIN_NAME = get_domain_name(HOMEPAGE)
QUEUE_FILE = PROJECT_NAME + '/queue.txt'
CRAWLED_FILE = PROJECT_NAME + '/crawled.txt'
NUMBER_OF_THREADES = 8
queue = Queue()
Spider(PROJECT_NAME,HOMEPAGE,DOMAIN_NAME)

# Create Worker Threads (Will die when main exists)
def create_workers():
	for _ in range(NUMBER_OF_THREADES):
		t = threading.Thread(target = work )
		t.daemon = True
		t.start()


# Stop Here Video : https://www.youtube.com/watch?v=ciwWSedS1XY 
# Time  : 6:12 

# Do the next Job in the queue
def work():
	while True:
		url = queue.get()
		#Spider.crawl_page()
# Stop Here Video : https://www.youtube.com/watch?v=ciwWSedS1XY 
# Time  : 6:12 


# Each Queued link is a new job
def create_jobs():
	for link in file_to_set(QUEUE_FILE):
		queue.put(link)
	queue.join()
	crawl()

#check if there are items in the queue
def crawl():
	queued_links = file_to_set(QUEUE_FILE)
	if len(queued_links) > 0:
		print(str(len(queued_links)) + ' links in the queue') 
		create_jobs()