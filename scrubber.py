# Now deletes original (careful!) and replaces with scrubbed. No renaming necessary.
# Now converts to TXT
# ADD THIS ON EACH REPLACE count(str, beg= 0,end=len(string))

import linecache
import fileinput
import sys
import os
import re
import collections
from collections import Counter

#items to replace
replace = { "&gt;" : ">",
	"&lf;" : "<",
	"&quot;" : "\"",
	"'&apos;" : "\'",
	"&amp;" : "&",
	"(mumbles)" : "(inaudible)",
	"(mumbling)" : "(indistinct)",
	"turnt" : "turned",
	"learnt" : "learned",
	"acknowledgement" : "acknowledgment",  #preferred American version
	"teh" : "the",
	"judgement": "judgment",
	"sizeable": "sizable"
	}

def vtt_func(path):
	myfile = open(path, 'r+') #opens up input file for reading
	text = myfile.read() #reads content into 'text'
	#Remove NOTE Paragraph if present and grab first timecode to compare in next step
	if "NOTE Paragraph" in text:
		text01 = text.replace("NOTE Paragraph\n\n","")
		print("Removed NOTE Paragraph")
		first_timecode = linecache.getline(input_file,5)
		print("first timecode: " + first_timecode[0:12])
	else:
		text01 = text
		print("does not contain NOTE Paragraph")
		first_timecode = linecache.getline(input_file,3)
		print("first timecode: " + first_timecode[0:12])

	# Test if first caption is zero. If not add blank cap at zero.
	if first_timecode[0:12] == '00:00:00.000':
		print "First timecode is already 00:00:00.000"
		captions = replace_all(text01,replace)
	else:
		print "Adding a blank caption at 00:00:00.000"
		scrubbed_text = text01.replace("WEBVTT","WEBVTT\n\n00:00:00.000 --> 00:00:00.001\n")

	captions = replace_all(scrubbed_text, replace)
	linecache.clearcache()
	delete_file()
	newfile = open(path[0:-4]+'.vtt','w')
	newfile.write(captions)
	myfile.close()
	newfile.close()

	#Call the converter function with the scrubbed text
	vtt_to_txt(path,captions)

def srt_func(path):
	myfile = open(path, 'r+') #opens up input file for reading
	text = myfile.read() #reads content into 'text'
	captions = replace_all(text, replace) #calls replace function on text
	newfile = open(path[0:-4]+'.srt','w')
	newfile.write(captions)
	myfile.close()
	newfile.close()
	delete_file()
	srt_to_txt(path,captions) #Call the converter function with the scrubbed text


# replacing function
def replace_all(text, dic):
	replace_dict = {}
	cnt = 1
	for i, j in dic.iteritems():
		#use this to increment a counter for each i:key_count
		if text.find(i) > 0:
			# print(i+":"+str(text.find(i)))
			replace_dict.update({i : cnt} )
			cnt +=1
		text = text.replace(i, j)

	for (key, value) in replace_dict.items() :
		print("Replaced \033[92m" + key + "\033[00m"  " (" +str(value) + ")" )
	return text



def srt_to_txt(path,captions):
	strip_r = re.sub('\r','',captions) #strip our all /r's - some srt files have /r and /n.
	regex = r'\d+\n\d+\:\d+\:\d+\,\d+.+\n'
	substr = ''
	plainText = re.sub(regex, substr, strip_r)
	# print(plainText)
	txt = open(path[0:-4]+'.txt','w')
	txt.write(plainText)
	txt.close()

def vtt_to_txt(path,captions):
	strip_r = re.sub('\r','',captions) #strip our all /r's - some vtt files have /r and /n.
	strip_vtt = re.sub('WEBVTT\n','',strip_r) #remove WEBVTT heading
	strip_1st_line = re.sub('\n\n\n','',strip_vtt)
	regex = r'^\d+\:\d+\:\d+\.\d+.+\n' #vtt specific match pattern
	substr = ''
	plainText = re.sub(regex, substr, strip_1st_line,0, re.MULTILINE)
	txt = open(path[0:-4]+'.txt','w')
	txt.write(plainText)
	txt.close()


def delete_file():
	if os.path.isfile(file_path):
		os.remove(file_path)
	else:
		print("Error: %s file not found" % file_path)

# Accepts srt and vtt files
input_file = ''
if len(sys.argv) > 1: #check that there's at least something for an arugment
	file_path = sys.argv[1] #set variable to path/filename
	filename = os.path.basename(file_path) #set filename only variable

	#if vtt
	if filename.lower().endswith('.vtt'):
		print("working on vtt file: " + filename)
		vtt_func(file_path)

	# if srt
	elif filename.lower().endswith('.srt'):
		print("working on srt file: " + filename)
		srt_func(file_path)
	# other file types - not valid
	else:
		print('please provide a valid file.')

else:
	print('No file!')
