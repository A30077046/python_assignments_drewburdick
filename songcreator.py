print "--Song Creator--"
print "Enter the first verse:", ##This is where you enter the 1st line of your song
frst = raw_input()
print "Enter the second verse:", #This is where you enter the 2nd line of your song
scnd = raw_input()
print "Enter the third verse:", #This is where you enter the 3rd line of your song
thrd = raw_input()
print "Enter the fourth verse:", #This is where you enter the 4th line of your song
frth = raw_input()
print "Enter the chourus:", #This is where you enter the chourus for your song
chrs = raw_input()
print "Enter the chourus repeat:" #This is how many time the chorus will repeat
rpt = input() #This gets an input because it is a numerical value it is expecting
print ""
song = []; #This defines a string that will use the bellow appended values
song.append(frst); #This is a segment of the formentioned string
song.append(scnd);
song.append(thrd);
song.append(frth);
song.append(chrs*rpt); # This takes the raw input that you enter for chrous and miltiplies it by the int provided
song.append(frst);
song.append(scnd);
song.append(thrd);
song.append(frth);
song.append(chrs*rpt);
print song
print ""
print("\n".join(map(str, song))) #This line will break the string
# \n is the value that defines new line