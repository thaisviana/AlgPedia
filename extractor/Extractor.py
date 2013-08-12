class CSVColumnExtractor:
	def __init__(self, file_name):
		self.file_name = file_name
		
	def extract_column(self, column_index):
		F_H = open(self.file_name, 'r')
		
		lines = F_H.readlines()
		
		F_H.close()
		
		column = map(lambda x: x.split(';')[column_index], lines)
		
		return column