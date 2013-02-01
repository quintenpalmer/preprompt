from xml.dom.minidom import parseString

def parse_xml(xml_string):
	return parseString(xml_string)

def parse_element(element,tag):
	return element.getElementsByTagName(tag).item(0)

def parse_string(element,tag):
	return element.getElementsByTagName(tag).item(0).firstChild.nodeValue

def parse_bool(element,tag):
	return bool(parse_string(element,tag))

def parse_int(element,tag):
	return int(parse_string(element,tag))
