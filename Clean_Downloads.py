import shutil, os
def cleanDirectory():
    dirto = "C:\\Users\\hp\\Downloads"
    os.chdir(dirto)
    a = os.listdir()
    for item in a:
        filen, fileext = os.path.splitext(item)
        itempath = dirto +"\\"+ item
        fileext = fileext.lower()
        imgpath = "D:\\E Drive\\Images"
        vidpath = "D:\\E Drive\\Videos"
        zipath = "D:\\E Drive\\Zip Files"
        exepath = "D:\\E Drive\\ Setups"
        mp3path = "D:\\E Drive\\Music"
        if fileext == ".zip" or fileext == ".rmskin":
            shutil.move(itempath, zipath)
        elif fileext == ".png" or fileext == ".jpg" or fileext == "jpeg" or fileext==".jfif":
            shutil.move(itempath, imgpath)
        elif fileext == ".mp4" or fileext==".mkv":
            shutil.move(itempath, vidpath)
        elif fileext == ".exe":
            shutil.move(itempath, exepath)
        elif fileext == ".mp3":
            shutil.move(itempath, mp3path)



cleanDirectory()
print("Cleaned Your Downloads Folder, Sir!")
