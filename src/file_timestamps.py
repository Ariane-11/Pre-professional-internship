#import built in python module
import os #to list files, get file infos, builds file path safely
import time # helps convert timestamps into human-readable dates
#create a variable to store the path of the photo folder
folder ="../data/iphone_photos"
# os.listdir(folder) returns a list of filenames inside the folder
for filename in os.listdir(folder): #loop to take one filename at the time
    file_path = os.path.join(folder, filename) #create a full path to the file
    if os.path.isfile(file_path): #is this path actually a file?
        stats = os.stat(file_path)
        #os.stat() asks the OS to give all the metadata about this file(file size, permissions, timestamps)
        created_time = time.ctime(stats.st_ctime) 
        #stats.st.ctime  --> raw creation time (system timestamp)
        #time.ctime(...) --> converts it into readable string 
        modified_time = time.ctime(stats.st_mtime)
        #stats.st.mtime --> last modification time
        print("File: ", filename)
        print("created: ", created_time)
        print("Modified ", modified_time)
        print()

