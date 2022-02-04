# Adapted from https://www.geeksforgeeks.org/create-xml-documents-using-python/
from xml.dom import minidom
import os

root = minidom.Document()

xml = root.createElement('root')
root.appendChild(xml)

productChild = root.createElement('product')
productChild.setAttribute('name', 'Geeks for Geeks')

productChild2 = root.createElement('product2')
productChild2.setAttribute('name', 'Geeks for Geeks')

productChild.appendChild(productChild2)

xml.appendChild(productChild)

xml_str = root.toprettyxml(indent="\t")

save_path_file = "gfg.xml"

with open(save_path_file, "w") as f:
    f.write(xml_str)
