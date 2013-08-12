from bs4 import BeautifulSoup	
import urllib2
import re
import gzip, StringIO
#from FileWriters import RDFWriter

def doMain():

#	rdf_writer = RDFWriter()
	
#	rdf_writer.generate_RDF_text()
	
	url = "http://en.wikipedia.org/wiki/Bubble_sort"
	
	headers = {'User-Agent' : 'Mozilla/5.0', 'Accept-Encoding' : 'gzip, defalte' }
	request = urllib2.Request(url, None, headers)
	try:
		response = urllib2.urlopen(request)
	#except urllib2.HTTPError, e:
	except Exception, e:
		raise ExtractionError("Error retreiving: " + str(url))
	
	data = decode(response)
	
	pool = BeautifulSoup(data)
	
	pseudo_src_pattern = re.compile('^source-pli$')
	
	divs = pool.findAll("div", {"class" : "mw-geshi mw-code mw-content-ltr" })
	for div in divs:
		language = div.find('div')
		lang_src = language['class'][1]
		match = pseudo_src_pattern.match(lang_src)
		if match:
			pseudo_code = language.find('pre')
			
			print pseudo_code.text
		
		else:
			print "No pseudo code"
			
			
	
	pt_div = pool.find("li", {"class" : "interwiki-pt"})
		
	if pt_div:
		pt_a_tag = pt_div.find("a")
		
		pt_wiki_link = "http:" + pt_a_tag['href']
		
		print pt_wiki_link
		
	

	url = "http://pt.wikipedia.org/wiki/Bubble_sort"
	
	headers = {'User-Agent' : 'Mozilla/5.0', 'Accept-Encoding' : 'gzip, defalte' }
	request = urllib2.Request(url, None, headers)
	try:
		response = urllib2.urlopen(request)
	#except urllib2.HTTPError, e:
	except Exception, e:
		raise ExtractionError("Error retreiving: " + str(url))
	
	data = decode(response)
	
	pool = BeautifulSoup(data)
	
	src_pattern = re.compile('^source-([a-zA-Z]+)$')
	
	implementations = []
		
	divs = pool.findAll("div", {"class" : "mw-geshi mw-code mw-content-ltr" })
	for div in divs:
		language = div.find('div')
		match = src_pattern.match(language['class'][1])
		if match:
			pseudo_code = language.find('pre')
			language = match.group(1)
			implementations.append((language, pseudo_code.text))
			
	
	for (language, code) in implementations:
		print language.upper() + ":"
		print code
			
	
	#divs = pool.findAll("div", {"class" : "mw-geshi mw-code mw-content-ltr" })
	
	#for div in divs:
		#print div
	#	language = div.find('div')
		#print language
	#	print language['class']
	
	#print pool
	
	
def decode(page):
	encoding = page.info().get("Content-Encoding")    
	if encoding in ('gzip', 'x-gzip', 'deflate'):
		content = page.read()
		if encoding == 'deflate':
			data = StringIO.StringIO(zlib.decompress(content))
		else:
			data = gzip.GzipFile('', 'rb', 9, StringIO.StringIO(content))
	page = data.read()

	return page
		
doMain()