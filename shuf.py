#!/usr/bin/env python3
import subprocess
'''
    song shuffler.

'''
import sys
import random

# f = open('TonySoft.m3u','r')
# o = open('out.m3u','w')

# we're getting a file like Playlist.m3u
inFile = sys.argv[1]
# the output file will be called Playlist_Shuffled.m3u
outFile = inFile[:-4] + "_Shuffled.m3u"
#
# before processing - change the path separator
# 
# sed_command = "'s/\//\\/g'"
# result = os.popen(fr"sed -i 's/\//\\/g' {inFile}")
# in Python 3 - use the subprocess.Popen() command to run a shell command.
# in this case, we are changing forward-slashes (/) to backslashes (\) which is
# what the Sony needs for the playlist.
sed_process = subprocess.Popen(fr"sed -i 's/\//\\/g' {inFile}", shell=True)
# note that subprocess.Popen() does not wait, so we have to wait for it to complete the 
# string replacement.
sed_process.wait()
# shuffle to a different file
f = open(inFile, 'r')
o = open(outFile, 'w')

items = []

# discard header.
f.readline()
counter = 0
for song in f:
    counter += 1
    
songcount = counter // 2

while counter > 0:
    items.append(counter)
    counter -= 1
    
# display

# print("{}".format(items))

random.shuffle(items)

# print("{}".format(items))

o.write('#EXTM3U\n')
counter = 0
song = 0
head = ''
title = ''
while counter < len(items):
    f.seek(0)
    f.readline()
    song = items[counter]
    while song > 0:
        head = f.readline()
        title = f.readline()
        song -= 1
    o.write("{}{}".format(head,title))
    
    counter += 1
 
f.close()
o.close()

print("shuffled {}\n".format(inFile))
