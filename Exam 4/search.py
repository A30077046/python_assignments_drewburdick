import os # Calling Action

text = os.listdir(".") #Declaring Syntax
index = [] #Naming action
print "Enter a search term:", 
search = raw_input().upper() #Takes seach term
for t in text:
    if t.endswith(".txt"):
        for line in open(t, 'r'):
            line = line.upper().strip();
            if search in line:
                index.append("%s: %s" % (t, line))
display = len(index)
print "I found % results" % display #Why wont this display the information I want CORREEEEEECCCCTTTTTLLLLLLYYYYYY!!!!!
for hit in index:
    print hit 
