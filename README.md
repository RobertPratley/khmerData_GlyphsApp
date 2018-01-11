Work in progress to establish a naming protocol for Khmer in GlyphsApp.

See discussion at: https://forum.glyphsapp.com/t/missing-khmer-submenu-letters-marks-symbols/7072

--

How to use:

Data is stored in a csv file, containing relevant fields for building of new glyphData.xml data (to be handled at a later stage).

sortNames, and accents are currently stripped. These can be injected later via classes whilst names are being sorted.

Running 'python buildGroupsPlist.py khmer.csv' will build a Groups.plist file that can be places in ~/Library/Application Support/Glyphs/Info for testing in the sidebar. Order is currently messed up whilst category names and groupings are discussed.
