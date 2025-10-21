import xml.etree.ElementTree as ET

inp = '''
<stuff>
<users>
<user x="2">
<id>001</id>
<name>Chuck</name>
</user>
<user x="7">
<id>009</id>
<name>Brent</name>
</user>
</users>
</stuff>'''

tree = ET.fromstring(inp)
lst1 = tree.findall("users/user")
print(len(lst1))
