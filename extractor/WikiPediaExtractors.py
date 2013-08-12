import re
import urllib2
import StringIO, gzip
from bs4 import BeautifulSoup

class ExtractionError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

class WikiPediaAbstractExtractor:
	def __init__(self, user_agent='Mozilla/5.0'):
		self.headers = {'User-Agent' : user_agent, 'Accept-Encoding' : 'gzip, defalte' }
		
		self.src_pattern = re.compile('^source-([a-zA-Z]+)$')
		self.pseudo_src_pattern = re.compile('^source-pli$')
		
	def search_page(self, url):
		self.url = url
		
		request = urllib2.Request(self.url, None, self.headers)
		try:
			response = urllib2.urlopen(request)
		except Exception, e:
			raise ExtractionError("Error retreiving: " + str(url))
		
		data = self.decode(response)
		
		self.pool = BeautifulSoup(data)
		print "Fetched : " + str(self.url)
	
	def get_alg_name(self):
		page_name = re.split('/', self.url)[-1]
		words = re.split('[-_]', page_name)
		words = map(lambda x: x.capitalize(), words)
	
		beautiful_name = ' '.join(words)
		
		return beautiful_name
	
	def get_alg_about(self):
		#div = self.pool.find("div", {"id" : 'mw-content-text' })
		div = self.pool.find("div", {"class" : "mw-content-ltr" })
		about = div.find('p')
		return about.text
		
	def get_alg_pseudo_code(self):
		
		pseudo_srcs = []
		
		divs = self.pool.findAll("div", {"class" : "mw-geshi mw-code mw-content-ltr" })
		for div in divs:
			language = div.find('div')
			match = self.pseudo_src_pattern.match(language['class'][1])
			if match:
				pseudo_code = language.find('pre')
				
				#pseudo_srcs.append((match.group(1),pseudo_code.text))
				pseudo_srcs.append((match.group(1),pseudo_code))
			
			match = self.src_pattern.match(language['class'][1])
			if match:
				pseudo_code = language.find('pre')
				#pseudo_srcs.append((match.group(1),pseudo_code.text))
				pseudo_srcs.append((match.group(1),pseudo_code))
				
		return pseudo_srcs
		
	#print pool
	
	def get_alg_implementations(self):
		
		pt_div = self.pool.find("li", {"class" : "interwiki-pt"})
		
		if pt_div:
			pt_a_tag = pt_div.find("a")
			
			pt_wiki_link = "http:" + pt_a_tag['href']
			
			pt_wiki_extractor = WikiPediaAbstractExtractor()
			pt_wiki_extractor.search_page(pt_wiki_link)
			implementations = pt_wiki_extractor.pt_get_implementations()
		else:
			# no pt page, bye bye
			return None
			
	
	def pt_get_implementations(self):
		implementations = []
		
		divs = self.pool.findAll("div", {"class" : "mw-geshi mw-code mw-content-ltr" })
		for div in divs:
			language = div.find('div')
			match = self.src_pattern.match(language['class'][1])
			if match:
				pseudo_code = language.find('pre')
				language = match.group(1)
				#implementations.append((language, pseudo_code.text))
				implementations.append((language, pseudo_code))
				
		return implementations
		
		
		
	def decode(self, page):
		encoding = page.info().get("Content-Encoding")    
		if encoding in ('gzip', 'x-gzip', 'deflate'):
			content = page.read()
			if encoding == 'deflate':
				data = StringIO.StringIO(zlib.decompress(content))
			else:
				data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(content))
		page = data.read()

		return page