from xml.etree.ElementTree import Element, fromstring, SubElement, tostring

xml = '<a></a>'
b = Element('b')
a = fromstring(xml)
a.append(b)
print(tostring(a))