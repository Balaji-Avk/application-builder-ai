import os

def createFile(filename,content):

    curr = os.getcwd()

    path = os.path.join(curr,'project')

    if not os.path.exists(path):
        os.makedirs(path)

    path =  os.path.join(path,filename)

    file = open( path,"w")

    file.write(content)
