import os
from os import walk
print os.getcwd()
mypath="C:\Documents and Settings\Pooja21\Desktop\NEW SONGS\Aashiqui 2 (2013)\\songs"
#print mypath
#a=os.listdir(mypath)
#print a

for (dirpath, dirnames, filenames) in walk(mypath):
    print dirpath,dirnames,filenames

#for files in a:
# print isfile(join(mypath,files))
# print files

