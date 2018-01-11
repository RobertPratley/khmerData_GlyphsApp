import sys
import csv
from collections import defaultdict as dd

def buildSideBarData(d):

    # Get category data:
    def getCD(g):
        if 'sideBar' in g.keys():
            c = g['sideBar']
            if '/' in c:
                c, s = c.split('/')
                c = (c, s)
            return c

    # Get category names
    categories = set() 
    for g in d:
        c = getCD(g)
        categories.add(c)

    # Build dictionary
    catDict = dd(dict) 
    for c in categories:
        if type(c) == tuple:
            catDict[c[0]][c[1]] = []
        else:
            catDict.setdefault(c, [])

    # Populate dictionary
    for g in d:
        c = getCD(g)
        if type(c) == tuple:
            catDict[c[0]][c[1]].append(g['name'])
        else:
            catDict[c].append(g['name'])

    return catDict


def buildGroupsPlist(catDict):
    with open('Groups.plist', 'w') as plist:
        plist.write('{\nlanguages = (\n{\n\tname = "Khmer";\n\tsubGroup = (\n')
        for k, v in catDict.items():
            plist.write('\t\t{\n')
            plist.write('\t\t\tname = "{0}";\n'.format(k))
            if type(v) == dict:
                plist.write('\t\t\tsubGroup = (\n')
                for s in v.keys():
                    plist.write('\t\t\t\t{\n')
                    plist.write('\t\t\t\t\tname = "{0}";\n\t\t\t\t\tcoverage = (\n'.format(s))
                    for g in v[s]:
                        plist.write('\t\t\t\t\t\t{0},\n'.format(g))
                    plist.write('\t\t\t\t\t);\n\t\t\t\t},\n')
                plist.write('\t\t\t);\n')
            else:
                plist.write('\t\t\tcoverage = (\n')
                for g in v:
                    plist.write('\t\t\t\t{0},\n'.format(g))
                plist.write('\t\t\t);\n')
            plist.write('\t\t},\n')
        plist.write('\t);\n},);}')


f = sys.argv[1]

d = [i for i in csv.DictReader(open(f), delimiter=',')]

catDict = buildSideBarData(d)

buildGroupsPlist(catDict)
