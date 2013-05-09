from xml.dom.minidom import parseString

from pplib.errors import XML_Parser_Error

def parse_xml(xml_string):
	try:
		return parseString(xml_string)
	except Exception:
		raise XML_Parser_Error('Error parsing the input string from the user :: \n\n%s\n\n'%xml_string)

def parse_element(element,tag):
	ele = element.getElementsByTagName(tag).item(0)
	if ele == None:
		raise XML_Parser_Error('The tag %s was not present in the element %s!'%(tag,element.toxml()))
	return ele

def parse_elements(element,tag):
	return list(element.getElementsByTagName(tag))

def parse_ints(element,tag):
	return [int(x.firstChild.nodeValue) for x in parse_elements(element,tag)]

def parse_string(element,tag):
	return parse_element(element,tag).firstChild.nodeValue

def parse_bool(element,tag):
	try:
		return parse_string(element,tag) == 'true'
	except ValueError:
		raise XML_Parser_Error('That tag "%s" contains "%s" which is not a bool'%(tag,string_repr))

def parse_int(element,tag):
	try:
		return int(parse_string(element,tag))
	except ValueError:
		raise XML_Parser_Error('That tag "%s" contains "%s" which is not an int'%(tag,string_repr))
