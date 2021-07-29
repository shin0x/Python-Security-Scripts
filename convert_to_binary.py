import os, sys

def usage():
    print 'Please type "python', sys.argv[0], ' sourcefile outputfile"'
    sys.exit(0)

if not (len(sys.argv)>2):
    usage()
filename = sys.argv[1]
outputfile = sys.argv[2]
if not(os.path.exists(filename)):
    print 'Sourcefile', filename, 'does not exist! Please give valid source path'
    sys.exit(1)
arr=[]
source = open(filename, 'rb')
for line in source:
    content = line.split()
for i in content:
        arr.append(int(i))
outbytes = bytearray(arr)
source.close
if os.path.exists(outputfile):
    print'Choosen output filename already exist'
    sys.exit(0)
else:
    out = open(outputfile, 'wb')
    out.write(outbytes)
out.close
