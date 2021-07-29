import zipfile
import itertools
import string
import sys
import getopt
import time
from threading import Thread

start = time.time()

opts, rest = getopt.getopt(sys.argv[1:], "m:a:f:")


for opt, arg in opts:
    if opt == '-f':
        zipIn = arg
    if opt == '-m':
        minimal = arg
    if opt == '-a':
        maximal = arg

def crack(zip, pwd):
    try:
        zip.extractall(pwd=str.encode(pwd))
        print('Success: Password is ' + pwd)
        end = time.time()
        file = open('data.txt', 'w')
        file.write("Filename: " +  zipIn + "\nThe password is: " + pwd + "\nIt tooks " +  str(end-start) + " seconds to finish")
        file.close()
        print("Finished in ", end - start, "seconds")
        quit()
    except:
        pass

myLetters = string.ascii_letters + string.digits +  string.punctuation
zipFile = zipfile.ZipFile(zipIn)

for i in range(int(minimal), int(maximal)):
    for j in map(''. join, itertools.product(myLetters, repeat=i)):
        t = Thread(target=crack, args=(zipFile, j))
        t.start()
