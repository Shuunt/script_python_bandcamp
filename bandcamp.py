import os
import sys
import shutil
import zipfile

path = os.getcwd()
for file in sys.argv:
    if "bandcamp" not in file:
        print ("The current working directory is %s" % path)
        print("The dir is %s" % os.path.splitext(file)[0])
        dir = os.path.splitext(file)[0]
        try:
            os.mkdir(dir)
        except OSError:
            print ("Creation of the directory %s failed" % dir)
        else:
            print ("Successfully created the directory %s " % dir)
            shutil.move(file, dir + "\\" + file)
            with zipfile.ZipFile(dir + "\\" + file, 'r') as zip_ref:
                zip_ref.extractall(dir)
            os.remove(dir + "\\" + file)
