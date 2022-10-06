import os, shutil, time, sys

scanFolder = "/home/BeemYo/Downloads/"
maxFileAge = 4 #days

print("\a")

def getDestFolder(file):
    extension = os.path.splitext(file)[1].lower()
    if not extension:
        return (True, None)
    extension = os.path.splitext(file)[-1].lower()
    folders = [k for k, v in locations.items() if extension in v]
    return (False, folders[0] if folders else "Other")

def moveFiles():
    global cache
    
    for file in os.listdir(scanFolder):
        try:
            isDirectory, destFolder = getDestFolder(file)
            if isDirectory:
                if not file in locations.keys():
                    shutil.move(scanFolder+file, scanFolder+"Folders/"+file)
                continue
        
            elif not file in cache:
                shutil.copy2(scanFolder+file, scanFolder+destFolder)
                cache += file+"\n"
            fileAge = time.time() - os.path.getmtime(scanFolder + file)
            if fileAge > 60*60*24*maxFileAge:
                os.remove(scanFolder+file)
        except:
            pass

with open("/home/BeemYo/Documents/hacking/DownloadsOrganizer/locations.txt", "r") as locfile:
    locations = eval(locfile.read().replace("\n", ""))
    if not os.path.exists("/home/BeemYo/Documents/hacking/DownloadsOrganizer/cache.txt"):
        open("/home/BeemYo/Documents/hacking/DownloadsOrganizer/cache.txt", "x").close()
        for folder in locations.keys():
            os.system("mkdir '" + scanFolder+folder + "'")
        
    with open("/home/BeemYo/Documents/hacking/DownloadsOrganizer/cache.txt", "r") as cacheFile:
        cache = cacheFile.read()
        if len(sys.argv) > 1:
        	cache = ""
        	print("No Cache")
        moveFiles()

with open("/home/BeemYo/Documents/hacking/DownloadsOrganizer/cache.txt", "w") as cacheFile:
    cacheFile.write(cache)
