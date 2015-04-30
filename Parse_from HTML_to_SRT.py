#!/usr/bin/env python
# -*- coding: utf-8 -*-


# This converts a subtitle file which contains html to a plain subtitle file, this is useful, especiall watching the video on the TV


from bs4 import BeautifulSoup
import codecs
import sys

# for while the subtitle file needs to be under the same folder as the code
# will create later on a function that asks for the input filename
with open('Two.Days.One.Night.srt') as file:
	data = file.read().decode('iso8859-1') ##this took some time, if I knew the right decode first, would be much, much less time consume
	
soup = BeautifulSoup(data)
	#print(soup.prettify())
	#print "-" * 60
print (soup.get_text())



# Next version will create a code that transform the normal subtitle to html where has colours, font size, etc....