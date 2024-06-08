import shutil
import os
import time

def zipFile():

    curr = os.getcwd()
    path = os.path.join(curr,'project')
    
    if os.path.exists(path):
        shutil.make_archive('project',root_dir=path,format='zip')
        shutil.rmtree(path)
        time.sleep(2)
        print('Successfully zipped \n')
    else:
        print('path not found')
