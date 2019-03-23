import os

# Each Website We Crawl is a seperate Project. 
# Comments by Arpit Agrawal 19-Jan-2019 for version 1.0

def create_project_dir(directory) :
	if not os.path.exists(directory) :
		print('Creating Project ' + directory)
		os.makedirs(directory)

# Create Queue and Crawled Files if Not created 
def create_data_files(project_name, base_url) :
	queue = project_name + '/queue.txt'
	crawled = project_name + '/crawled.txt'
	if not os.path.isfile(queue) :
		write_file(queue, base_url)
	if not os.path.isfile(crawled) :
		write_file(crawled, '')

#Create A New File using Base functions and defining it in write_file function
def write_file(path, data):
	f = open(path, 'w')
	f.write(data)
	f.close()

# Append content to the files having links or urls
def append_to_file(path,data) :
	with open(path, 'a') as file :
		file.write(data + '\n')

#Delete Content of the File 
def delete_file_content(path):
	with open(path, 'w'):
		pass

# Read A file and convert each link in sets
def file_to_set(filename):
	results = set()
	with open(filename, 'rt') as f:
		for line in f:
			results.add(line.replace('\n',''))
		return results

# Iterate through set each item will be a new line in set
def set_to_file(links, file):
	delete_file_content(file)
	for link in sorted(links):
		append_to_file(file,link)