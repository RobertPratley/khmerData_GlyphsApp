from khmerData import KD, abvm, blwm


def buildAccentLists(kd):
	for k, v in kd.items():
		if 'accents' in v:
			glyphAccents = ""
			if 'abvm' in v['accents']:
				for a in abvm:
					glyphAccents = glyphAccents + '{0}, '.format(a)
			if 'blwm' in v['accents']:
				for a in blwm:
					glyphAccents = glyphAccents + '{0}, '.format(a)
			kd[k]['accents'] = glyphAccents

def getCategories(kd):
	categories = set()
	for k, v in kd.items():
		if 'sideBar' in v:
			categories.add(v['sideBar'])
	return categories

def buildSideBarEntries(kd):
 	categories = getCategories(kd)
 	glyphCategoryListDict = {key:[] for key in categories}
	for k, v in kd.items():
		category = v['sideBar']
		glyphCategoryListDict[category].append(k)
	with open('khmer.plist', 'w') as kp:
		kp.write('{\n\tname = "Khmer";\n\tsubGroup = (\n')
		for k in glyphCategoryListDict:
			kp.write("\t\t{\n")
			kp.write('\t\t\tname = "{0}";\n'.format(k))
			kp.write("\t\t\tcoverage = (\n")
			for g in glyphCategoryListDict[k]:
				kp.write("\t\t\t\t{0},\n".format(g))
			kp.write("\t\t\t);\n\t\t},\n")
		kp.write('\t);\n}')


def buildGlyphsDataXML(kd):

	def setXMLAttr(e, a, d):
		if a in d.keys():
			e.set(a, d[a])

	import xml.etree.cElementTree as ET
	root = ET.Element('glyphData')
	for k, v in kd.items():
		e = ET.SubElement(root, 'glyph')	
		e.set('name', k)
		setXMLAttr(e, 'unicode', v)
		setXMLAttr(e, 'sortName', v)
		setXMLAttr(e, 'category', v)
		setXMLAttr(e, 'subCategory', v)
		setXMLAttr(e, 'script', v)
		setXMLAttr(e, 'description', v)
		setXMLAttr(e, 'production', v)	
		setXMLAttr(e, 'decompose', v)
		setXMLAttr(e, 'anchors', v)
		setXMLAttr(e, 'accents', v)
	kGD = ET.ElementTree(root)
	kGD.write("khmerGlyphsData.xml")

buildAccentLists(KD)
buildGlyphsDataXML(KD)
buildSideBarEntries(KD)



