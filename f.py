f = open('sonysongs.txt', 'r')
o = open('s.txt', 'w')

for item in f:
    item = item.strip()
    if '/media/pi/WALKMAN/' in item:
        item = item.replace('/media/pi/WALKMAN/', 'D:\\')
        item = item.replace('/','\\')
    o.write(item+'\n')
    
f.close()
o.close()
    