
from share.pyplib.xml_parser import parse_elements, parse_element,parse_string,parse_int,parse_xml,parse_bool

xml = '<game><name>are</name></game>'
ele = parse_xml(xml)
print parse_string(ele,'name')
#print parse_string(ele,'fame')
print parse_int(ele,'name')
print ele.toprettyxml()
