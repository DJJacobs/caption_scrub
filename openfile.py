# File Objects
import linecache

with open('/Local/python/test_file.txt','r+') as f:

	date = f.readline()
	print date[23:]

	f.seek(148)
	first_name = f.readline()
	print first_name

	f.seek(156)
	last_name = f.readline()
	print last_name


