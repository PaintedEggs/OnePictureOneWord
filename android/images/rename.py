import os

i = 0
for filename in os.listdir("."):
	if "jpg" != filename[-3:]:
		print ">>> next"
		continue

	if "_" == filename[0:1]:
		newFileName = filename[1:]

		os.rename(filename, newFileName )
		print "<<< ", filename
		print ">>> ", newFileName
		i += 1