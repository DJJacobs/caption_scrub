# File Objects
import linecache
import fileinput
import sys

filename = sys.argv[1]
print("working on: " + filename)


myfile = open(filename, 'r+')
text = myfile.read()
first_timecode = linecache.getline(filename,5)
print(first_timecode[0:12])

if first_timecode[0:12] == '00:00:00.000':
  print "Beginning timecode add: not necessary"
else:
  print "Adding a blank caption at 00:00:00.000"
  newText = text.replace("WEBVTT\n\nNOTE Paragraph\n\n","WEBVTT\n\nNOTE Paragraph\n\n00:00:00.000 --> 00:00:00.001\n\n").replace("&gt;&gt;",">>")
    # newText = text.replace("(WEBVTT\n\nNOTE Paragraph\n\n)","\100:00:00.000")
# newText2 = newText.replace("&gt;&gt;",">>")
linecache.clearcache()

# print(newText)
newfile = open(filename[0:-4]+'-scrubbed.vtt','w') 
newfile.write(newText)
myfile.close()
newfile.close()
