#!/usr/bin/env python

import wikipedia
import urllib
import os

for name in open("people_list.txt"):
	name = name[:-1]
	try:
		print "Get page: ", name
		wiki = wikipedia.WikipediaPage( name )	# get wiki page
	except:
		print "Can't get image: ", name
		continue

	if not os.path.exists(name):
		print "Create folder: ", name
		os.mkdir(name)	# create folder for personal

	image_num = 0
	image_count = len( wiki.images )
	# load all images from wiki page
	for imageUrl in wiki.images:
		print "Load image: ", image_num, image_count
		fname = name + "/" + str(image_num) + ".jpg"
		if not os.path.exists( fname ):
			urllib.urlretrieve(imageUrl, filename = fname )	# load image
		image_num += 1

		if 30 == image_num:
			break
	
	summary_info = wikipedia.summary(name)		# get summary info
	summary_file = open(name + "/summary.txt", "a")	# create file for info
	summary_file.write( summary_info.encode('utf8') )		# write info into file
	summary_file.close()
