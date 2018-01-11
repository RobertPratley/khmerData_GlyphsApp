In progress work for updates to Khmer script data in GlyphsApp. 

Notes on process:

Data is currently stored in khmerData.py and built with build.py. Glyph data is stored in an ordered dictionary, with accent classes in separate lists that are added to the main dictionary via build.py. The latter script also outputs a rough plist file for the sidebar and an xml file containing new glyphData entries. Order of categories in the plist file and order of attributes in each xml <glyph> element is currently not set. 

The python code is rough and ready, but the reason for this approach is to attempt to reduce the amount of find/replace whilst certain naming issues are resolved. 

A modified Glyphs file of the Noto khmer font is included in this repo to show extent of default script coverage. glyphs marked black are missing from current data as they may be more design-dependant. Colours indicate sidebar categories and ahoukd be relatively self-evident. Amendments by someone more experienced is welcome. 

This data does make changes to the glyphData.xml entries. Having not worked on Khmer in Glyphs for over a year, others may be in a better position to decide if such (if any) modifications are necessary for getting a step closer to producing Khmer fonts through Glyphs. 



Points for discussion:

Sidebar entries are currently organised along similar lines to other SE Asian scripts hence Ben’s moniker ‘subjoined’ is used for subconsonants. 

Need to review whether any glyphs marked black in the Noto sample file should be candidates for inclusion as sidebar entries. 

Another look over what classifies as a letter vs a mark needs to take place. At the moment dependent vowels are classed as ‘Marks’ for the sidebar, even when they may have category=“Letter” and subCategory=“Spacing” attributes in their respective glyphData xml element. 

Subsequent consonant form in clusters are currently named in the format ‘ka-khmer.below’. It may be better to follow the model of Noto Khmer and name these according to input sequence (‘coeng_ka-khmer’) as this is semantically still correct for characters like ro-khmer and ba-khmer whose subconsonant forms sit mostly adjacent to the base consonant.

ie-khmer and ya-khmer PSTS forms are named as per Noto with a .right# suffix.

Few alternate glyphs are present, except for .low versions of subconsonant forms of characters such as ro-khmer, ba-khmer etc, the .right forms of ie-khmer and ya-khmer, and a .less version of nyo-khmer (following the naming pattern for yoYing-thai). Depending on name scheme for subjoined glyphs, ‘*.low’ may want to change to a numbered scheme (as is present in ie-khmer and ya-khmer) for the sake of consistency. I’m unfamiliar with whether an alternate nyo-khmer.below is required. 

Anchor/accents need review. The current set up is pretty much taken from Noto. 

Description attributes (especially) for subjoined glyphs need to change. 

Decomposition rules have been added to some characters (such as ya-khmer and aa-khmer). qaa-khmer currently has a subcategory of ‘ligature’ as per noto, though this may likely change as design choices may not permit composition from components. 






