from urllib.parse import urlparse

# Comments by Arpit Agrawal 19-Jan-2019 for version 1.0

# Get Domain name like (arpitagr.in)
def get_domain_name(url):
	try:
		results = get_sub_domain_name(url).split('.')
		return results[-2] + '.' + results[-1]
	except:
		return ''


# Get Sub Domain Names like (profile.arpitagr.in) 
def get_sub_domain_name(url):
	try:
		return urlparse(url).netloc
	except:
		return ''

# print(get_domain_name('https://myname.xyz.arpitagr.in/login.php'))