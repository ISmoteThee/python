import xml.etree.ElementTree as ET
#Safer file access:
#with open('country_data.xml', 'r') as file:
    #tree = ET.parse(file)
tree = ET.parse('country_data.xml')
root = tree.getroot()

print('Test 1')
for neighbor in root.iter('neighbor'):
    print(neighbor.attrib)

print('\nTest 2')
for country in root.findall('country'):
    rank = country.find('rank').text
    name = country.get('name')
    print(name, rank)

#for rank in root.iter('rank'):
#    new_rank = int(rank.text) + 1
#    rank.text = str(new_rank)
#   rank.set('updated', 'yes')
#tree.write('country_out.xml')

