from html.parser import HTMLParser
from urllib import parse

# Comments by Arpit Agrawal 19-Jan-2019 for version 1.0

class LinkFinder(HTMLParser):
	def __init__(self,base_url,page_url):
		super().__init__()
		self.base_url = base_url
		self.page_url = page_url
		self.links = set()

	def handle_starttag(self,tag,attrs):
		#print(tag)
		if tag == 'a':
			for(attribute,value) in attrs:
				if attribute == 'href':
					url = parse.url.join(self.base_url,value)
					self.links.add(url)

	def page_links(self):
		return self.links


	def error(self,message):
		pass