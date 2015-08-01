# Task2:
# Write a python program to find all the articles that have "History" in their title in the enwiki-latest-stub-articles1.xml and save all of their attributes in a CSV file.
# This code is by Hank Mushinski, W205, Summer 2015 and borrowed here for more detailed examination
import csv, re, sys
from xml.etree import ElementTree as ET
 
class WikiParse(object):
	def __init__(self, infile):
		print "Initialize WikiParse"
		self._infile = infile
 
	def _parseTree(self):
		# assign parsed XML tree to self._tree
		try:
			self._tree = ET.parse(self._infile).getroot()
			print "Parsed file: '%s'" % str(self._infile)
		except Exception, e:
			print "EXCEPTION: File could not be parsed", '\n', e
			sys.exit(1)
 
	def _getTreeData(self, parent):
		""" recursive method to get labels and data from subtrees """
		data = []
		children = list(parent)
		if len(children) > 0: # if current XML node has children
			childdata = []
			for child in children:
				childdata += self._getTreeData(child) # recursively look for more child nodes
			for i in xrange(0,len(childdata), 1):
				childdata[i][0] = "_".join([parent.tag, childdata[i][0]]) # write labels of child nodes as parenttag_childtag
			data += childdata
		else:
			attributes = parent.attrib
			if len(attributes) > 0: # if XML node has attributes instead of text, do same as above
				for i in sorted(attributes.keys()):
					data += [[ '_'.join([parent.tag, i]), attributes[i] ]]
			else:
				data += [[parent.tag, parent.text]]
		return data
 
	def _extractHistoryPages(self):
		hasHistory = re.compile('(History)')
		pages = self._tree.findall('page')
		historydata = []
		headers = set()
		for page in pages:
			if hasHistory.search(page.find('title').text): # if "History" is in page title
				pagedatalist = self._getTreeData(page)
				pagedatadict = {} # assign page data to dictionary to make writing csv file easier
				for i in pagedatalist:
					headers.add(i[0])
					try:
						pagedatadict[i[0]] = i[1].encode('utf-8')
					except AttributeError:
						pass # if data cannot be encoded with utf-8, ignore data
				historydata.append(pagedatadict)
		self._finalData = (headers, historydata)
		print 'Extracted History Pages'
 
	def _writeToCSV(self, outfilename):
		with open(outfilename, 'wb') as f:
			writer = csv.DictWriter(f, fieldnames=self._finalData[0])
			writer.writeheader()
			for d in self._finalData[1]:
				writer.writerow(d)
		f.close()
		print "Output Complete"
 
	def run(self, outfilename):
		if outfilename.split('.')[-1] != 'csv':
			raise Exception('Output filename must end with ".csv"')
		self._parseTree()
		self._extractHistoryPages()
		self._writeToCSV(outfilename)
 
if __name__ == "__main__":
	p = WikiParse('./enwiki-latest-stub-articles1.xml')
	p.run('wiki-history.csv')
