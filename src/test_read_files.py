#import os module
import os
#folder path
folder ="../data/iphone_photos"
#os.lisdir take the folder path as argument
files = os.listdir(folder) #return a list of all filenames of the folder

#go through each file of the files list
for f in files:
    print(f)