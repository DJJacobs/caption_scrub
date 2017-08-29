# File Objects
import linecache
import fileinput
import sys

filename = sys.argv[1]
print(filename)

myfile = open(filename, 'r+')
text = myfile.read()
newText = text.replace("&gt;&gt;",">>").replace("(mumbles)","(inaudible)").replace("turnt","turned").replace("acknowledgement","acknowledgment").replace("&amp;","&")


# print(newText)
newfile = open(filename[0:-4]+'-scrubbed.srt','w') 
newfile.write(newText)
myfile.close()
newfile.close()


