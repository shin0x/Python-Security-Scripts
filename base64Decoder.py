import base64, sys, os

def usage():
        print ('Please type python', sys.argv[0], 'Base64 sourcefile Decoded outputfilename')
        sys.exit(0)
if not (len(sys.argv)>2):
    usage()
filename = sys.argv[1]
outputfile = sys.argv[2]
if not(os.path.exists(filename)):
    print ('Sourcefile', filename, 'does not exist! Please give valid source path')
    sys.exit(1)
encodedSource = ''
source = open(filename, 'rb')
for line in source:
    encodedSource += line        
source.close()
 
if os.path.exists(outputfile):
    print('Chosen output filename already exist')
    sys.exit(0)
else:
    decodedData = base64.b64decode(encodedSource)
    print (decodedData)
    out = open(outputfile, 'wb')
    out.write(decodedData)
    out.close()
