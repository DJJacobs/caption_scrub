# File Objects


with open('/Local/python/test_file.txt','r') as f:
     for line in f:
        if 'First' in line:
            firstname =line[18:-1]
            
        if 'Last' in line:
            lastname =line[17:-1]
            
            print "%s %s" % (firstname, lastname)
    # for line in f: 



print "ID HERE| Captions|Transcribe| %s %s | " % (firstname, lastname)