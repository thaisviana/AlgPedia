import sys
sys.path.append('../')
from WikiPediaExtractors import WikiPediaAbstractExtractor
from Extractor import CSVColumnExtractor

file_name = '../temp/dbpedia_fetch_0.csv'
col_extractor = CSVColumnExtractor(file_name)
	
# wiki links are the 3rd (2 in 0-based) column in the .csv
wiki_links = col_extractor.extract_column(2)

wiki_alg_extractor = WikiPediaAbstractExtractor()
for link in wiki_links:
	wiki_alg_extractor.search_page(link)
	pseudo_code = wiki_alg_extractor.get_alg_pseudo_code()
	
	if(pseudo_code == []):
		print("No pseudo-code")
	else:
		print("About: ", wiki_alg_extractor.get_alg_about())
		print("Name: ", wiki_alg_extractor.get_alg_name())
		print("Pseudo-code: ", pseudo_code[0])
	print("===========================================================")

