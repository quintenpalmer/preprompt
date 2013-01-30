from xml.dom.minidom import parseString

def parse_string(xml_string):
	return parseString(xml_string)

def parse_element(element,tag):
	print element.getElementsByTagName(tag)
