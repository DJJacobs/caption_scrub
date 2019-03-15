import linecache
import fileinput
import sys
import os
import re
import io


def replace_chevrons(s, sub, repl):
	s = s.replace(sub, repl)
	return s

# replace nth instance of >> 
def nth_repl_all(s, sub, repl, nth):
    find = s.find(sub)
    # loop until we find no match
    i = 1
    while find != -1:
        # if i  is equal to nth we found nth matches so replace
        if i == nth:
            s = s[:find]+repl+s[find + len(sub):]
            i = 0
        # find + len(sub) + 1 means we start after the last match
        find = s.find(sub, find + len(sub) + 1)
        i += 1
    s = replace_chevrons(s,sub, "Q:")
    return s


# Accepts srt and vtt files
input_file = ''
if len(sys.argv) > 1:
	input_file = sys.argv[1]
	print("working on file: " + os.path.basename(input_file))
	myfile = io.open(input_file, 'r+',encoding='utf-16')
	text = myfile.read()
	print(myfile)
	transcript = nth_repl_all(text,">>","A:",2)
	newfile = open(input_file[0:-4]+'-scrubbed.txt','w')
	newfile.io.write(transcript)
	myfile.close()

else:
    print 'No file!'



